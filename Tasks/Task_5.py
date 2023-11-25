from helper_functions import *
from Task4 import *

def moving_average(x, window_size):
    
    y = []  # List to store the moving averages
    i = 0
    while i<len(x)-window_size+1:
        window = x[i : i+window_size]
        window_avg=(sum(window)/window_size)
        y.append(window_avg)
        i+=1
    return y


def fold_signal(signal):
    folded_signal=signal[::-1]
    return folded_signal

def remove_dc_time_domain():
    x,y=get_signal_TimeDomain()
    # comp=dft(y)
    # print(comp)
    # comp[0]=0
    # print(comp)
    amp,faze,N=DFT(y)
    amp[0]=0
    faze[0]=0
    print(amp)
    print(faze)
    
    
# Example usage:
signal = [3, 1, 4, 2, 5, 6, 7, 9, 8, 10]  # Replace this with your signal data
window_size = int(input("Enter the window size for moving average calculation: "))

moving_avg_result = moving_average(signal, window_size)
sig=fold_signal(signal)
# print(sig)
# print("Moving averages:", moving_avg_result)
remove_dc_time_domain()
