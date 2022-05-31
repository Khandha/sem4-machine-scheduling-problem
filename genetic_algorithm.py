from random import shuffle, sample, randint
from greedy import greedy, value
from utils import pairwise
from time import time
from math import ceil
import multiprocessing
import os

TIME_MAX = 60 * 5
POPULATION_SIZE = 12
SELECTION_PAIRS = 2
MUTATION_PROBABILITY = 5
NO_PROGRESS_SHUFFLE_COUNT = 1000
NO_PROGRESS_BAILOUT_COUNT = 30000
CHILDREN_COUNT = ceil(POPULATION_SIZE / SELECTION_PAIRS)


def create_initial_population(processor_count, task_array, genome_length):
    """
    Creates a random population of POPULATION_SIZE individuals.
    """
    population = []
    for _ in range(POPULATION_SIZE):  # create a pool of populations
        single_genotype = list(range(genome_length))
        shuffle(single_genotype)
        population.append(single_genotype)
    return population


def decode(genotype, task_array):
    """
    From a genotype coded with indexes of tasks, returns a decoded list of tasks.
    """
    for genotype_index, task_index in enumerate(genotype):
        genotype[genotype_index] = task_array[task_index]
    return genotype


def evaluate(genotype, task_array, processor_count):
    """
    Given a genotype, returns the numeric value of the solution.
    """
    a = decode(genotype[:], task_array)
    return value(greedy(a, processor_count))


def sort(population, task_array, processor_count):
    return sorted(population, key=lambda genome: evaluate(genome, task_array, processor_count))


def selection(population, task_array, processor_count):
    return sort(population, task_array, processor_count)[:SELECTION_PAIRS * 2]


def crossover(fittest, genome_length):
    """
    Given a list of individuals, returns a POPULATION_SIZE large list of randomly crossed and mutated individuals.
    """
    children = []
    for first, second in pairwise(fittest):
        for _ in range(CHILDREN_COUNT):
            splice_point = sorted(sample(range(genome_length), 2))  # [5:10]
            child = first.copy()  # copy of first
            child[splice_point[0]:splice_point[1]] = second[splice_point[0]:splice_point[1]]  # swap
            children.append(child)  # add child to children

    return mutate(children, genome_length)


def mutate(genomes, genome_length):
    """
    Mutates random genes in a given genome list by reference based on MUTATION_PROBABILITY.
    """
    for index, genome in enumerate(genomes):
        if randint(0, 100) < MUTATION_PROBABILITY:
            mutation_point = sorted(sample(range(genome_length), 2))
            tmp = genome[mutation_point[0]]
            genome[mutation_point[0]] = genome[mutation_point[1]]
            genome[mutation_point[1]] = tmp
            genomes[index] = genome

    return genomes


def run(task_array, processor_count, population, genome_length, time_end):
    # select SELECTION_PAIRS of the best individuals
    fittest = selection(population, task_array, processor_count)

    base_line = evaluate(fittest[0], task_array, processor_count)
    base_genome = fittest[0]
    # crossover the best individuals
    # returns mutated SELECTION_PAIRS * CHILDREN_COUNT of children
    children = crossover(fittest, genome_length)
    new_population = sort(children, task_array, processor_count)[0:POPULATION_SIZE]

    no_progress_count = 0
    bailout_exit = False
    while time_end > time():  # returns SELECTION_PAIRS of best individuals
        new_fittest_evaluation = evaluate(new_population[0], task_array,
                                          processor_count)  # returns the value of the fittest individual
        if new_fittest_evaluation < base_line:
            # progress made
            no_progress_count = 0
            base_line = new_fittest_evaluation
            base_genome = new_population[0]
            print(str(os.getpid()) + ': ' + str(base_line))

        else:
            no_progress_count += 1
            if no_progress_count > NO_PROGRESS_SHUFFLE_COUNT:
                shuffle(new_population[-3])
                shuffle(new_population[-4])
            if no_progress_count > NO_PROGRESS_BAILOUT_COUNT:
                bailout_exit = True
                break

        # crossover only the best individuals
        children = crossover(new_population[0:SELECTION_PAIRS * 2], genome_length)
        # evaluate the list of children
        sorted_children = sort(children, task_array, processor_count)
        # replace 2 worst individuals in population with 2 best children
        new_population[-2:] = sorted_children[:2]
        new_population = sort(new_population, task_array, processor_count)

    print("Bailout exit: " + str(os.getpid())) if bailout_exit else print("Timeout exit: " + str(os.getpid()))
    return base_genome


# def setup(task_array, processor_count):
#     genome_length = len(task_array)
#     time_end = time() + 60 * 5
#
#     # create the initial population
#     population = create_initial_population(processor_count, task_array, genome_length)
#     best_genome = run(task_array, processor_count, population, genome_length, time_end)
#
#     a = decode(best_genome, task_array)
#     decoded_best_genome = greedy(a, processor_count)
#     # print(decoded_best_genome)
#     # print(value(decoded_best_genome))
#
#     return decoded_best_genome


def process_run(task_array, processor_count, time_end, population, queue, genome_length):

    best_genome = run(task_array, processor_count, population, genome_length, time_end)

    a = decode(best_genome, task_array)
    decoded_best_genome = greedy(a, processor_count)

    queue.put(decoded_best_genome)


def run_processes(task_array, processor_count):
    time_end = time() + TIME_MAX

    start = time()
    genome_length = len(task_array)

    queue = multiprocessing.Queue()
    jobs = []
    for _ in range(4):
        population = create_initial_population(processor_count, task_array, genome_length)
        p = multiprocessing.Process(target=process_run, args=(task_array, processor_count, time_end,
                                                              population, queue, genome_length))
        jobs.append(p)
        p.start()
    for proc in jobs:
        proc.join()
    best_processes = []
    best_times = []
    for _ in range(4):
        decoded_best_genome = queue.get()
        print(value(decoded_best_genome))
        print("time" + str(time() - start) + "\n")

        best_processes.append(decoded_best_genome)
        best_times.append(value(decoded_best_genome))

    best = [x for _, x in sorted(zip(best_times, best_processes))]
    return best[0]
