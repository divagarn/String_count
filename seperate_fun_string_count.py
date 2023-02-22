import tkinter as tk
from tkinter import filedialog
import csv
import re
from datetime import datetime

def processed_file(input_file, source_file):
    with open(input_file, 'r') as f:
        reader = csv.reader(f)
        data = list(reader)

    for i, row in enumerate(data):
    
        search_string = row[0].replace('[','').replace(']','')

        count = 0

        with open(source_file, 'r') as f:
            for line in f:
                if re.search(search_string, line):
                    count += 1

        data[i].append(count)

    output_file = f'output_{datetime.now().strftime("%Y-%m-%d_%H-%M-%S")}.csv'
    with open(output_file, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerows(data)

    return output_file

def browse_input_file():
    file_path = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])
    input_file_entry.delete(0, tk.END)
    input_file_entry.insert(0, file_path)

def browse_source_file():
    file_path = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv"), ("Log files", "*.log")])
    source_file_entry.delete(0, tk.END)
    source_file_entry.insert(0, file_path)

def process_files():
    input_file = input_file_entry.get()
    source_file = source_file_entry.get()
    if input_file and source_file:
        output_file = processed_file(input_file, source_file)
        status_label.config(text=f"Output file created: {output_file}")
    else:
        status_label.config(text="Please select input and source files")

window = tk.Tk()
window.title("String Count")
window.geometry("400x200")

input_file_label = tk.Label(window, text="Select input file (CSV):")
input_file_label.pack()
input_file_entry = tk.Entry(window)
input_file_entry.pack()
input_file_button = tk.Button(window, text="Browse", command=browse_input_file)
input_file_button.pack()

source_file_label = tk.Label(window, text="Select source file (CSV or log):")
source_file_label.pack()
source_file_entry = tk.Entry(window)
source_file_entry.pack()
source_file_button = tk.Button(window, text="Browse", command=browse_source_file)
source_file_button.pack()

process_button = tk.Button(window, text="Process Files", command=process_files)
process_button.pack()

status_label = tk.Label(window, text="")
status_label.pack()

window.mainloop()
