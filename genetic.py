from math import inf
from random import random, randint, randrange
from greedy import greedy

POPULATION_SIZE = 40
MUTATION_PROBABILITY = 0.1
NO_PROGRESS_BAILOUT_COUNT = 5000


def encode(task_array, individual):
    genotype = []

    for process in task_array:
        for index, processor in enumerate(individual):
            if process in processor:
                genotype.append(index)
                process_index = processor.index(process)
                processor[process_index] = -1
                break
    return genotype


def decode(task_array, processor_count, genotype):
    processors = [[] for _ in range(processor_count)]

    for process_index, processor_index in enumerate(genotype):
        processors[processor_index].append(task_array[process_index])
    return processors


def fittness(task_array, processor_count, genotype):
    individual = decode(task_array, processor_count, genotype)
    maximum = 0
    for processor in individual:
        time = sum(processor)
        if time > maximum:
            maximum = time
    return -1 * sum(max(individual, key=lambda i: sum(i)))


def selection(task_array, processor_count, population):
    by_fittest = sorted(population, key=lambda genotype: fittness(
        task_array, processor_count, genotype), reverse=True)
    return by_fittest[:2]


def crossover(genotype_a, genotype_b):
    length = len(genotype_a)
    half_length = round(length)
    first_child = genotype_a[:half_length] + genotype_b[half_length:]
    second_child = genotype_a[half_length:] + genotype_b[:half_length]

    return first_child, second_child


def mutation(processor_count, population):
    for genotype in population:
        if random() < MUTATION_PROBABILITY:
            index = randint(0, len(genotype) - 1)
            new_processor_index = randint(0, processor_count - 1)
            genotype[index] = new_processor_index


def pc_max_random(processor_count, task_array):
    result = [[] for _ in range(processor_count)]
    for process in task_array:
        processor = randint(0, processor_count - 1)
        result[processor].append(process)
    return result


def setup(processor_count, task_array):

    initial_population = []
    for i in range(POPULATION_SIZE):
        individual = pc_max_random(processor_count, task_array)
        genotype = encode(task_array, individual)
        initial_population.append(genotype)

    return initial_population


def loop(initial_population, task_array, processor_count):
    population = initial_population
    best_fittness = inf
    best_genotype = None
    no_progress_counter = 0
    generation_counter = 0
    fittest_individuals = None

    while no_progress_counter < NO_PROGRESS_BAILOUT_COUNT:
        # selection
        fittest_individuals = selection(task_array, processor_count, population)

        # crossover
        first_child, second_child = crossover(
            fittest_individuals[0], fittest_individuals[1])

        least_fit = min(population, key=lambda genotype: fittness(
            task_array, processor_count, genotype))
        least_fit_index = population.index(least_fit)
        population[least_fit_index] = first_child

        second_least_fit = min(population, key=lambda genotype: fittness(
            task_array, processor_count, genotype))
        second_least_fit_index = population.index(second_least_fit)
        population[second_least_fit_index] = second_child

        # mutation
        mutation(processor_count, population)

        current_best = abs(
            fittness(task_array, processor_count, fittest_individuals[0]))
        if current_best < best_fittness:
            best_fittness = current_best
            best_genotype = fittest_individuals[0]
            no_progress_counter = 0
            print(best_fittness)
        else:
            no_progress_counter += 1

        generation_counter += 1
    return decode(task_array, processor_count, fittest_individuals[0])


def run(task_array, processor_count):
    initial_population = setup(processor_count, task_array)

    return loop(initial_population, task_array, processor_count)
