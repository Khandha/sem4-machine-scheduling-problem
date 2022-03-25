from bokeh.io import output_file, show
from bokeh.plotting import figure


def generate_graph(processor_array):
    longest = find_max_list(processor_array)
    list_of_size_of_max_elements = list(range(0, longest))
    for i in range(0, len(list_of_size_of_max_elements)):
        list_of_size_of_max_elements[i] = []
    for i in range(0, len(processor_array)):
        for ii in range(0, longest):
            if ii > len(processor_array[i]) - 1:
                list_of_size_of_max_elements[ii].append('x')
            else:
                list_of_size_of_max_elements[ii].append(processor_array[i][ii])

    output_file("stacked.html")

    processes = list(range(0, len(processor_array)))
    processes = [str(i) for i in processes]
    order = ["0", "1", "2"]
    colors = ["#c9d9d3", "#718dbf", "#e84d60"]

    data2 = {str(i): list_of_size_of_max_elements[i] for i in range(0, longest)}
    data2['processes'] = processes
    p = figure(y_range=processes, height=650, width=1200, title="Processes",
               toolbar_location=None, tools="")
    p.hbar_stack(order, y='processes', color=colors, height=0.8, source=data2,
                 legend_label=order)
    p.y_range.range_padding = 0.1
    p.ygrid.grid_line_color = None
    p.legend.location = "top_left"
    p.axis.minor_tick_line_color = None
    p.outline_line_color = None
    show(p)


def find_max_list(arr):
    arr_len = [len(i) for i in arr]
    return max(arr_len)


def sum_of_processes(processor_array):
    sum_of_lengths = []
    for element in processor_array:
        sum_of_lengths.append(sum(element))
    return sum_of_lengths
