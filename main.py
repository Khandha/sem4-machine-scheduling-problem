from time import perf_counter

from file_opener import open_instance
from greedy import greedy
from graph_generator import generate_graph as chart
from genetic_algorithm import run

instance = open_instance()
processor_count = instance.pop(0)
task_count = instance.pop(0)


# greedy_result = greedy(instance, processor_count)
# print(sum(max(greedy_result, key=lambda i: sum(i))))
# chart(greedy_result)

run(instance, processor_count)
