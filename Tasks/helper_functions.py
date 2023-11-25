import matplotlib.pyplot as plt
import numpy as np
import re
from tkinter import filedialog


def read_signal_file(file_path):
    try:
        print("read signal file")
        with open(file_path, 'r') as file:
            for _ in range(3):
                next(file)

            signal_data = np.genfromtxt(file, delimiter=' ', dtype=float)
            signal_x = signal_data[:, 0]
            signal_y = signal_data[:, 1]
            print("before exception")
            return signal_x, signal_y
           
    except FileNotFoundError:
        print(f"{file_path} not found. Make sure it exists in the same folder.")
        return None, None

def get_signal_TimeDomain():
    print ("get signals")
    file_path = filedialog.askopenfilename(title="Choose a signal data file")
    signal_x=[]
    signal_y=[]
    if file_path:
            signal_x, signal_y = read_signal_file(file_path)
            return signal_x, signal_y
    else:
            return None, None, None
        
def get_signals():
    print ("get signals")
    file_path = filedialog.askopenfilename(title="Choose a signal data file")
    signal_x=[]
    signal_y=[]
    if file_path:
            signal_x, signal_y = read_signal_file_IDFT(file_path)
            return signal_x, signal_y
    else:
            return None, None, None
    
    
    
    
    
def read_signal_file_IDFT(file_path):
    signal_x = []
    signal_y = []

    with open(file_path, 'r') as file:
        for _ in range(3):
            next(file)

        for line in file:
                parts = line.strip().replace('f','').split(',')
                if len(parts) == 2:
                    signal_x.append(float(parts[0]))
                    signal_y.append(float(parts[1]))
    print(signal_x)
    print(signal_y)
    return signal_x, signal_y

def plot_signal_DFT(x,y,label):
    plt.figure(figsize=(10,6))
    # plt.bar(x,y,width=0.2, align='center', color='blue')
    plt.title(label)
    if label=='Amplitude spectrum':
        plt.xlabel('frequency')
        plt.ylabel('amplitude')
        plt.stem(x,y)

        plt.tight_layout()
        plt.show()
    elif label == 'Phase spectrum':
        plt.xlabel('frequency')
        plt.ylabel('phase-shift')
        plt.stem(x,y)

        plt.tight_layout()
        plt.show()
    elif label =='Time Domain': 
        plt.xlabel('time')
        plt.ylabel('amplitude')
        plt.stem(x,y)
        plt.tight_layout()
        plt.show()
        
    else:
        plt.xlabel('x')
        plt.ylabel('y')
        # plt.plot(x,y)
        plt.stem(x,y)

        plt.tight_layout()
        plt.show()
        
        
        

def plot_DFT(freq,amplitude,phase):
    plot_signal_DFT(freq,amplitude,"freq-amplitude")
    plot_signal_DFT(freq,phase,"freq-phase shift")
    
def plot_signal(x,y,label):
    plt.figure(figsize=(10,6))
    plt.plot(x,y)
    plt.title(label)
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.show()
