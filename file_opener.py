import os
import tkinter as tk
from tkinter import filedialog, simpledialog
from tkinter.messagebox import askyesno, showinfo
from instance_generator import main as instance_generator
from pathlib import Path

def open_instance():
    root = tk.Tk()
    root.withdraw()
    if tk.messagebox.askyesno('Instance generator', 'Would you like to generate an instance?'):
        processor_count = simpledialog.askinteger('Instance generator',
                                                  'How many processors would you like to generate the instance for?')
        process_count = simpledialog.askinteger('Instance generator',
                                                'How many processes would you like to generate the instance for?')
        min_process_time = simpledialog.askinteger('Instance generator',
                                                   'Minimum process time?')
        max_process_time = simpledialog.askinteger('Instance generator',
                                                   'Maximum process time?')
        file_name = instance_generator(processor_count, process_count, min_process_time,
                                       max_process_time)
        tk.messagebox.showinfo('Instance generator', 'Instance {} generated'.format(file_name))
        quit()

    array = []

    file_path = filedialog.askopenfilename(initialdir=Path.cwd()/"instances", title="Select file",
                                           filetypes=[("Text Files", "*.txt")])
    if not file_path:
        quit()
    with open(file_path) as f:
        for line in f:
            array.append(int(line.rstrip()))
    return array
