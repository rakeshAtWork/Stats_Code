import tkinter as tk
from tkinter import filedialog

def select_input_file():
    file_path = filedialog.askopenfilename(title="Select Input File")
    input_file_entry.delete(0, tk.END)
    input_file_entry.insert(tk.END, file_path)

def select_output_file():
    file_path = filedialog.asksaveasfilename(title="Select Output File")
    output_file_entry.delete(0, tk.END)
    output_file_entry.insert(tk.END, file_path)

def process_files():
    input_file = input_file_entry.get()
    output_file = output_file_entry.get()

    # Perform file processing here
    # Replace this with your own logic

    output_label.configure(text="Files processed successfully!")

# Create the main window
window = tk.Tk()
window.title("File Processing")

# Create input file selection widgets
input_file_label = tk.Label(window, text="Input File:")
input_file_label.pack()

input_file_entry = tk.Entry(window, width=50)
input_file_entry.pack()

input_file_button = tk.Button(window, text="Select Input File", command=select_input_file)
input_file_button.pack()

# Create output file selection widgets
output_file_label = tk.Label(window, text="Output File:")
output_file_label.pack()

output_file_entry = tk.Entry(window, width=50)
output_file_entry.pack()

output_file_button = tk.Button(window, text="Select Output File", command=select_output_file)
output_file_button.pack()

# Create process button
process_button = tk.Button(window, text="Process Files", command=process_files)
process_button.pack()

# Create output label
output_label = tk.Label(window, text="")
output_label.pack()

# Start the GUI event loop
window.mainloop()
