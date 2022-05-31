from time import perf_counter

from file_opener import open_instance
from greedy import greedy
from graph_generator import generate_graph as chart
from genetic_algorithm import run_processes


def main():
    instance = open_instance()
    processor_count = instance.pop(0)
    task_count = instance.pop(0)

    #
    # greedy_result = greedy(instance, processor_count)
    # print(sum(max(greedy_result, key=lambda i: sum(i))))
    # chart(greedy_result)

    # chart(setup(instance, processor_count))
    chart(run_processes(instance, processor_count))


if __name__ == "__main__":
    main()