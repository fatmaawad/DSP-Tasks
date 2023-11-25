from helper_functions import *
from comparesignals import SignalSamplesAreEqual
from Task2 import *

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

def shift_sig(signal,con):
    x=[i+con for i in signal]
    return x

def fold_signal(signal):
    folded_signal=signal[::-1]
    return folded_signal



    
