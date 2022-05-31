VALUE_LARGER_THAN_MAXIMUM_TIME = 1000000


def greedy(task_array, processor_count):
    processor_array = [[entry] for entry in task_array[:processor_count]]
    for elem in task_array[processor_count:]:  # remaining tasks in task array [58, 59, 31, ...]
        minimal_index, minimal_sum = 0, VALUE_LARGER_THAN_MAXIMUM_TIME
        for index, processor in enumerate(processor_array):
            sum_of_processor = sum(processor)
            if sum_of_processor < minimal_sum:
                minimal_index = index
                minimal_sum = sum_of_processor
        processor_array[minimal_index].append(elem)

    return processor_array


def value(processor_array):
    maximal_sum = 0
    for processor in processor_array:
        sum_of_processor = sum(processor)
        if sum_of_processor > maximal_sum:
            maximal_sum = sum_of_processor
    return maximal_sum

