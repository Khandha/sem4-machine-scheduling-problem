import os
import tkinter as tk
from tkinter import filedialog, simpledialog
from tkinter.messagebox import askyesno, showinfo
from instance_generator import main as instance_generator
from pathlib import Path


def open_instance():
    root = tk.Tk()
    # root.withdraw()
    root.tk.eval(f'tk::PlaceWindow {root._w} center')
    root.attributes('-alpha', 0)
    root.update_idletasks()
    file_path = None

    if tk.messagebox.askyesno('Instance generator', 'Would you like to generate an instance?'):

        processor_count = simpledialog.askinteger('Instance generator',
                                                  'How many processors would you like to generate the instance for?')

        process_count = simpledialog.askinteger('Instance generator',
                                                'How many processes would you like to generate the instance for?')

        min_process_time = simpledialog.askinteger('Instance generator',
                                                   'Minimum process time?')

        max_process_time = simpledialog.askinteger('Instance generator',
                                                   'Maximum process time?')

        file_name, relative_file_path = instance_generator(processor_count, process_count, min_process_time,
                                                           max_process_time)
        tk.messagebox.showinfo('Instance generator', 'Instance {} generated'.format(file_name))
        if not tk.messagebox.askyesno('Instance generator',
                                      'Would you like to run the generated instance? (selecting no will close the '
                                      'program)'):
            quit()
        else:
            file_path = relative_file_path
            print(relative_file_path)

    instance_from_file = []
    if file_path is None:
        file_path = filedialog.askopenfilename(initialdir=Path.cwd() / "instances", title="Select file",
                                               filetypes=[("Text Files", "*.txt")])
        if not file_path:
            quit()

    with open(file_path) as f:
        for line in f:
            instance_from_file.append(int(line.rstrip()))

    processor_count = instance_from_file.pop(0)
    task_count = instance_from_file.pop(0)
    return task_count, processor_count, instance_from_file


def open_from_cli():
    file_path = input()
    instance_from_file = []
    with open(file_path) as f:
        for line in f:
            instance_from_file.append(int(line.rstrip()))

    processor_count = instance_from_file.pop(0)
    task_count = instance_from_file.pop(0)
    return task_count, processor_count, instance_from_file