from time import perf_counter

from file_opener import open_instance, open_from_cli
from greedy import greedy, value
from graph_generator import generate_graph as chart
from genetic_algorithm import run_processes


def main():
    task_count, processor_count, instance = open_from_cli()

    greedy_result = greedy(instance, processor_count)
    # print(greedy_result)
    print("Greedy: " + str(value(greedy_result)))
    # chart(greedy_result)

    genetic_result = run_processes(instance, processor_count)
    print("Genetic: " + str(value(genetic_result)))
    # print(genetic_result)
    # chart(genetic_result)


if __name__ == "__main__":
    main()
