from greedy import Greedy
from graph_generator import generate_graph as chart
# from generator import Generator


array = []
with open('m50n200.txt') as f:
    for line in f:
        array.append(int(line.rstrip()))
processor_count = array.pop(0)
task_count = array.pop(0)

greedy = Greedy()
greedy_result = greedy(array, processor_count)
chart(greedy_result)