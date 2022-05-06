import random
import os
from time import localtime, strftime

current_time = strftime("%Y%m%d%H%M%S", localtime())
output_file_name = os.path.join(current_time + '.txt')


def main(processor_count, process_count, min_process_time,
         max_process_time):
    with open(output_file_name, 'w') as output_file:
        process_times = [str(random.randint(int(min_process_time), int(max_process_time))) for r in
                         range(int(process_count))]
        output_file.write(str(processor_count) + '\n')
        output_file.write(str(process_count) + '\n')
        output_file.write('\n'.join(process_times))
    print("Generated instance file: " + output_file_name)
    return output_file_name
