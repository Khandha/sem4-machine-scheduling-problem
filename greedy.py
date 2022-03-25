import sys


def findmin(array):
    min_val = sys.maxsize
    element = 0
    for elem in array:
        if sum(elem) < min_val:
            min_val = sum(elem)
            element = elem
    return array.index(element)


class Greedy:
    def __init__(self):
        print("Greedy")

    def __call__(self, task_array, processor_count):
        processor_array = []
        for i in range(0, processor_count):
            a = [task_array.pop(0)]
            processor_array.append(a)

        while task_array:
            empty_process = (findmin(processor_array))
            processor_array[empty_process].append(task_array.pop())

        return processor_array
