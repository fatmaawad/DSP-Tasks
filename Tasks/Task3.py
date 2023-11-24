import math
import numpy as np
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from tkinter import *
import QuanTest1
import QuanTest2
from helper_functions import *

def choose_signal_file():
    root = tk.Tk()
    root.withdraw()
    file_path = filedialog.askopenfilename(title="Choose a signal data file")

    if file_path:
        signal_x, signal_y = read_signal_file(file_path)
        return file_path, signal_x, signal_y
    else:
        return None, None, None

# def read_signal_file(file_path):
#     try:
#         with open(file_path, 'r') as file:
#             for _ in range(3):
#                 next(file)

#             signal_data = np.genfromtxt(file, delimiter=' ', dtype=float)
#             signal_x = signal_data[:, 0]
#             signal_y = signal_data[:, 1]
#             return signal_x, signal_y
#     except FileNotFoundError:
#         print(f"{file_path} not found. Make sure it exists in the same folder.")
#         return None, None

def convert_to_binary(num, bits):
    binary_num = ""
    for i in range(bits - 1, -1, -1):
        bit = (num >> i) & 1
        binary_num += str(bit)
    return binary_num

def update_table(frame, x, y, choice, value):
    if not value:
        value = 0
    value = int(value)
    l = value
    if choice == 0:
        l = 2 ** value
    min_val = min(y)
    max_val = max(y)
    delta = (max_val - min_val) / l
    error = []
    interval_index = []
    encoded_level = []
    sample_level_encoded = []
    sample_quantized = []

    for i in range(l):
        encoded_level.append(convert_to_binary(i, math.ceil(math.log2(l))))

    for val in y:
        level = (val - min_val) / delta
        level_apr = math.floor(level)
        if val != min_val and level - level_apr == 0:
            level_apr -= 1
        interval_index.append(level_apr + 1)
        sample_level_encoded.append(encoded_level[level_apr])
        new_val = level_apr * delta + delta / 2 + min_val
        error.append(new_val - val)
        sample_quantized.append(new_val)

    tree = ttk.Treeview(frame, columns=("Interval Index", "Encoded", "Quantized", "Error"))
    tree.heading("Interval Index", text="Interval Index")
    tree.heading("Encoded", text="Encoded")
    tree.heading("Quantized", text="Quantized")
    tree.heading("Error", text="Error")

    for i in range(len(x)):
        tree.insert('', tk.END, values=(interval_index[i], sample_level_encoded[i], sample_quantized[i], error[i]))

    tree.place(y=170, x=300, anchor="center")
    
    QuanTest2.QuantizationTest2("D:/DSP/Task 1/Quan2_Out.txt",
        interval_index, sample_level_encoded, sample_quantized, error)
    QuanTest1.QuantizationTest1("D:/DSP/Task 1/Quan1_Out.txt", sample_level_encoded, sample_quantized)

def quantize(frame):
    x = []
    y = []

    def choose_file():
        signal = choose_signal_file()
        nonlocal x, y
        x = signal[1]
        y = signal[2]

    button1 = tk.Button(frame, width=10, text="Choose File", command=choose_file)
    button1.grid(row=0, pady=20, padx=20)
    text = "Number of Bits"
    lvl = tk.Label(frame, text=text, bg="#000000", fg="white")
    lvl.grid(row=0, column=3, sticky='w', padx=80)
    user_input = tk.Entry(frame)
    user_input.grid(row=0, column=3, padx=200)

    def inputs():
        nonlocal text
        text = "Number of Bits" if choice.get() == 0 else "Number of Levels"
        lvl.configure(text=text)

    choice = tk.IntVar()
    btn1 = tk.Radiobutton(frame, text='Bits', value=0, variable=choice, selectcolor="black", background="#111111",
                        foreground="white", activebackground="#000000", command=inputs)
    btn2 = tk.Radiobutton(frame, text='Levels', value=1, variable=choice, selectcolor="black", background="#111111",
                        foreground="white", activebackground="#000000", command=inputs)
    choice.set(0)
    btn1.grid(row=0, column=1, pady=20)
    btn2.grid(row=0, column=2, pady=20)

    button2 = tk.Button(frame, width=15, text="Quantize Signal", command=lambda: update_table(frame, x, y,
                                                                                    choice.get(), user_input.get()))
    button2.place(y=20, x=600)

# root = tk.Tk()
# root.title("Signal Quantization")
# root.geometry("800x800")

# # Call quantize to create the GUI
# quantize(root)

# # Start the main event loop
# root.mainloop()
