import matplotlib
from comparesignals import SignalSamplesAreEqual
import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter.filedialog import askopenfile
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# reads signal file
def read_signal_data(file_name):
    x, y = [], []
    with open(file_name) as f:
        text = f.readlines()
        for i in range(int(text[2]) + 1):
            data = text[i + 3].strip().split(' ')
            x.append(float(data[0]))
            y.append(float(data[1]))
    return x, y


def plot_signal(frame):
    filename = askopenfile()
    if filename is not None:
        print("File selected:", filename.name)
        x, y = read_signal_data(filename.name)

        continuoius_fig = Figure(figsize=(4, 3), dpi=100)
        continuoius_fig.suptitle("Continuous Signal")
        if int(x[0]) == 0:
            continuoius_fig.supxlabel('Time')
        else:
            continuoius_fig.supxlabel('Frequency')
        a = continuoius_fig.add_subplot(111)
        a.plot(x, y)
        continuoius_fig.tight_layout()
        canvas = FigureCanvasTkAgg(continuoius_fig, frame)
        canvas.get_tk_widget().place(relx=0.2, rely=0.09, anchor='nw')
        canvas._tkcanvas.place(relx=0.2, rely=0.09, anchor='nw')

        discrete_fig = Figure(figsize=(4, 3), dpi=100)
        discrete_fig.suptitle("Discrete Signal")
        if int(x[0]) == 0:
            discrete_fig.supxlabel('Time')
        else:
            discrete_fig.supxlabel('Frequency')
        a = discrete_fig.add_subplot(111)
        a.stem(x, y)
        discrete_fig.tight_layout()
        canvas = FigureCanvasTkAgg(discrete_fig, frame)
        canvas.get_tk_widget().place(relx=0.6, rely=0.09, anchor='nw')
        canvas._tkcanvas.place(relx=0.6, rely=0.09, anchor='nw')


def display_file_signal(samples, rate):
    plt.figure(figsize=(10, 10))
    if rate==0:
     time = np.linspace(0, 2 * np.pi, num=1000)
     plt.subplot(2, 1, 1)
     plt.plot(time, samples, label='Continuous Signal')
     plt.title('Continuous Signal')
     plt.xlabel('Time (s)')
     plt.grid()

    else:
     time1 = np.arange(0, len(samples)) / rate
     plt.subplot(2, 1, 2)
     plt.stem(time1, samples, use_line_collection=True, basefmt=" ", label='Discrete Signal')
     plt.subplot(2, 1, 1)
     plt.plot(time1, samples, label='Continuous Signal')
     plt.title('Discrete and continuous Signal')
     plt.xlabel('Time (s)')
     plt.grid(True)
     plt.legend()

    plt.tight_layout()
    plt.show()


# generating sin & cos waves from user input
def generate_signal(signal_type, a, theta, f, fs):
    fs = float(fs)
    if fs == 0 and signal_type == 'sine':
        t = np.linspace(0, 2 * np.pi, num=1000)
        signal = a * np.sin(2 * np.pi * f * t + theta)
    elif fs==0 and signal_type == 'cosine':
        t = np.linspace(0, 2 * np.pi, num=1000)
        signal = a * np.cos(2 * np.pi * f * t + theta)
    elif signal_type == 'sine':
        time = np.arange(0, 1, 1 / fs)
        signal= a * np.sin(2 * np.pi * f * time + theta)
    elif signal_type== 'cosine':
        time = np.arange(0, 1, 1 / fs)
        signal = a * np.cos(2 * np.pi * f * time + theta)


    return signal


# show_frame()



























