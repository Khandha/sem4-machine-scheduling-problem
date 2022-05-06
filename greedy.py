def findmin(array):
    return array.index(min(array, key=sum))


class Greedy:
    def __call__(self, task_array, processor_count):


        processor_array = []
        for i in range(0, processor_count):
            a = [task_array.pop(0)]
            processor_array.append(a)

        while task_array:
            empty_process = (findmin(processor_array))
            processor_array[empty_process].append(task_array.pop())

        print(sum(max(processor_array, key=sum)))
        return processor_array
