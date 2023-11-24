import matplotlib.pyplot as plt
import numpy as np
import tkinter as tk
from tkinter import *
from tkinter import filedialog
from comparesignals import SignalSamplesAreEqual
from helper_functions import *


#filename = filedialog.askopenfilename()
# def read_signal_file(file_path):
#     try:
#         with open(file_path, 'r') as file:
#             # Skip the first 3 lines (header information)
#             for _ in range(3):
#                 next(file)
            
#             # Read the data as pairs of values
#             signal_data = np.genfromtxt(file, delimiter=' ', dtype=float)
#             signal_x = signal_data[:, 0]
#             signal_y = signal_data[:, 1]
#             return signal_x, signal_y
#     except FileNotFoundError:
#         print(f"{file_path} not found. Make sure it exists in the same folder.")
#         return None, None


def plot_signal(x,y,label):
    plt.figure(figsize=(10,6))
    plt.plot(x,y)
    plt.title(label)
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.show()


def addition(x1, x2, y1, y2):
    result_x = x1
    result_y = y1 + y2
    return result_x, result_y


# ///////////////////////////
def subtraction(x1, x2, y1, y2):
    result_x = x1
    result_y = y2 - y1
    return result_x, result_y


def multiplication(x, y, constant):
    result_y = y * constant
    return x, result_y


def squaring(x, y):
    result_y = y ** 2
    return x, result_y


def shift_signal(x, y, costant):
    result_x = x + costant
    return result_x, y


def accumlation(x, y):
    result_y = np.cumsum(y)
    return x, result_y


def normalize_signal(x , y, range_min, range_max):
    min_val = np.min(y)
    max_val = np.max(y)
    
    if min_val < range_min or max_val > range_max:
        normalized_signal = (y - min_val) / (max_val - min_val)
    else:
        normalized_signal = min_val
        result_x = x
    
    if range_min == -1 and range_max == 1:
        normalized_signal = 2 * normalized_signal - 1
    elif range_min == 0 and range_max == 1:
        normalized_signal = normalized_signal
    else:
        raise ValueError("Invalid range specified. Choose either (-1, 1) or (0, 1).")
    
    return normalized_signal

