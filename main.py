from file_opener import open_instance
from greedy import Greedy
from graph_generator import generate_graph as chart

greedy = Greedy()

instance = open_instance()
processor_count = instance.pop(0)
task_count = instance.pop(0)

greedy_result = greedy(instance, processor_count)
chart(greedy_result)
