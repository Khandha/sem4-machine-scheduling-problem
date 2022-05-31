from random import shuffle, randrange, sample
from greedy import greedy, value
from utils import pairwise

POPULATION_SIZE = 10
SELECTION_PAIRS = 2
MUTATION_PROBABILITY = 0.1
NO_PROGRESS_BAILOUT_COUNT = 5000
CHILDREN_COUNT = round(POPULATION_SIZE / SELECTION_PAIRS)


def create_initial_population(processor_count, task_array, genome_length):
    population = []
    for _ in range(POPULATION_SIZE):  # create a pool of populations
        single_genotype = list(range(genome_length))
        shuffle(single_genotype)
        population.append(single_genotype)
    return population


def decode(genotype, task_array):
    for genotype_index, task_index in enumerate(genotype):
        genotype[genotype_index] = task_array[task_index]
    return genotype


def evaluate(genotype, task_array, processor_count):
    a = decode(genotype, task_array)
    return value(greedy(a, processor_count))


def selection(population, task_array, processor_count):
    fittest = sorted(population, key=lambda genome: evaluate(genome, task_array, processor_count))
    return fittest[:SELECTION_PAIRS * 2]


def crossover(fittest, genome_length):
    for first, second in pairwise(fittest):

        splice_point = sorted(sample(range(genome_length), 2))  # [5:10]
        tmp = first[splice_point[0]:splice_point[1]]
        first[splice_point[0]:splice_point[1]] = second[splice_point[0]:splice_point[1]]
        second[splice_point[0]:splice_point[1]] = tmp
    return fittest

def run(task_array, processor_count):
    genome_length = len(task_array)
    # create the initial population
    population = create_initial_population(processor_count, task_array, genome_length)
    # select SELECTION_PAIRS of best individuals
    fittest = selection(population, task_array, processor_count)
    # crossover the best individuals
    children = crossover(fittest, genome_length)
