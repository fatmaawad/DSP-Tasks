from helper_functions import *
from comparesignals import SignalSamplesAreEqual
from Task2 import *
from Task4 import *

def smoothing(window_size): 
    indecies,samples=get_signal_TimeDomain()
    y = []  
    i = 0
    while i<len(indecies)-window_size+1:
        window = samples[i : i+window_size]
        window_avg=(sum(window)/window_size)
        y.append(window_avg)
        i+=1
    SignalSamplesAreEqual("D:\DSP\Tasks\TestCases_task6\Moving Average\MovAvgTest1.txt", indecies, y)
    SignalSamplesAreEqual("D:\DSP\Tasks\TestCases_task6\Moving Average\MovAvgTest2.txt", indecies, y)

    return y

# def shift_sig(signal,con):
#     x=[i+con for i in signal]
#     return x

# Shifting
def shifting(x,y,shift_value):
    shifted_signal = (x + shift_value, y)
    return shifted_signal


def fold_signal(signal):
    folded_signal=signal[::-1]

    return folded_signal

def remove_dc_time_domain():
    x,y=get_signal_TimeDomain()
    amp,faze,N=DFT(y)
    amp[0]=0
    faze[0]=0    
    real=IDFT(amp,faze)
    SignalSamplesAreEqual("D:\DSP\Tasks\Remove DC component\DC_component_output.txt", x, real)

    return real



    
