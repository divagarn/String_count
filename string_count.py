import tkinter as tk
from tkinter import filedialog
import csv

def remove_square_brackets(s):
    return s.strip("[]")

def process_files():
    csv_file = csv_entry.get()
    source_file = source_entry.get()


    with open(csv_file, "r") as f:
        reader = csv.reader(f)
        data = list(reader)


    data = [[remove_square_brackets(s) for s in row] for row in data]

   
    with open(source_file, "r") as f:
        source_data = f.read()

    counts = {}
    for row in data:
        string = row[0]
        if string in counts:
            continue
        count = source_data.count(string)
        counts[string] = count

    with open(csv_file, "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([])
        writer.writerow(["Search String", "Count"])
        for string, count in counts.items():
            writer.writerow([string, count])

    tk.messagebox.showinfo("Complete", "File processing complete.")


root = tk.Tk()
root.title("String Searcher")


csv_label = tk.Label(root, text="Input CSV File:")
csv_label.pack()
csv_entry = tk.Entry(root, width=50)
csv_entry.pack()
csv_button = tk.Button(root, text="Browse", command=lambda: csv_entry.insert(0, filedialog.askopenfilename()))
csv_button.pack()

source_label = tk.Label(root, text="Source File:")
source_label.pack()
source_entry = tk.Entry(root, width=50)
source_entry.pack()
source_button = tk.Button(root, text="Browse", command=lambda: source_entry.insert(0, filedialog.askopenfilename()))
source_button.pack()

process_button = tk.Button(root, text="Process Files", command=process_files)
process_button.pack()

root.mainloop()
