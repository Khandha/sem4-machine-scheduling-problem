import os

from greedy import Greedy
from graph_generator import generate_graph as chart
# from generator import Generator
import tkinter as tk
from tkinter import filedialog
from os import getcwd


array = []

root = tk.Tk()
root.withdraw()
file_path = filedialog.askopenfilename(initialdir=os.getcwd(), title="Select file", filetypes=[("Text Files", "*.txt")])
with open(file_path) as f:
    for line in f:
        array.append(int(line.rstrip()))
processor_count = array.pop(0)
task_count = array.pop(0)

greedy = Greedy()
greedy_result = greedy(array, processor_count)
chart(greedy_result)