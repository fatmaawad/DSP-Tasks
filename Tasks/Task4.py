import math
import numpy as np
import cmath
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from tkinter import *
from helper_functions import *
from signalcompare import SignalComapreAmplitude, SignalComaprePhaseShift



def dft(signal):
    N = len(signal)
    X = []
    for k in range(N):
        real_part = 0
        imag_part = 0
        for n in range(N):
            angle = 2 * math.pi * k * n / N
            #Euler's
            real_part += signal[n] * math.cos(angle)
            imag_part -= signal[n] * math.sin(angle)
        X.append(complex(real_part, imag_part))
    return X


def DFT(signal):
    N = len(signal)
    X = []
    
    for k in range(N):
        real_part = 0
        imag_part = 0
        for n in range(N):
            angle = 2 * math.pi * k * n / N
            real_part += signal[n] * math.cos(angle)
            imag_part -= signal[n] * math.sin(angle)
        X.append(complex(real_part, imag_part))
    
    # Calculate amplitude and phase shift
    amplitude = [abs(x) for x in X]
    phase_shift = [math.atan2(x.imag, x.real) for x in X]
    # save_frequency_components(angle,amplitude,phase_shift)
    return amplitude, phase_shift,N

def idft(X):
    N = len(X)
    real_signal = []
    
    for n in range(N):
        real_part = 0
        imag_part = 0
        for k in range(N):
            angle = 2 * math.pi * k * n / N
            real_part += X[k].real * math.cos(angle) - X[k].imag * math.sin(angle)
            imag_part -= X[k].real * math.sin(angle) + X[k].imag * math.cos(angle)
        real_signal.append(real_part / N)
    save_time_domain_signal(real_signal)
    return real_signal
   
   
#2nd loop 
def IDFT(amp,phase):
    print("in IDFT")
    N =len(amp)
    xknew = np.zeros(N,dtype=np.complex128)
    for i in range(N):
        xknew[i] += complex(amp[i]*np.cos(phase[i]),amp[i]*np.sin(phase[i]))

    xN=np.zeros(N)
    xNtmp=np.zeros(N)
    N =len(xknew)
    n=np.arange(N)
    for i in range(N):
        for k in range(N):
             xNtmp[k]=xknew[k]*np.exp((2j*np.pi*i*k)/N)
        xN[i]=np.sum(xNtmp)/N
    return xN
     
def ang_freq_gen(freq,N):
    ang=2*np.pi*freq/N
    omegas=[]
    for i in range(N):
        omegas.append(ang*(i+1))
    return omegas

           
def apply_fourier_transform(sampling_frequency, signal_x, signal_y):
    n = len(signal_x)
    ang=2*np.pi*sampling_frequency/n
    angular=[]
    for i in range (n):
        angular.append(ang*(i+1))
    # frequencies = [i * sampling_frequency / n for i in range(n)]
    complex_spectrum = dft(signal_y)

    magnitude_spectrum = [abs(x) for x in complex_spectrum]
    phase_spectrum = [math.atan2(x.imag, x.real) for x in complex_spectrum]

    return angular, magnitude_spectrum, phase_spectrum

        


     


def save_frequency_components(frequencies, magnitudes, phases):
    with open("frequency_domin_output.txt", "w") as file:
        file.write("0\n")
        file.write("1\n")
        file.write(str(len(frequencies)) + "\n")
        for i in range(len(frequencies)):
            # Write the frequency, magnitude, and phase to the file.
            file.write(f"{frequencies[i]} {magnitudes[i]} {phases[i]}\n")
            
def save_time_domain_signal(signal):
    with open("time_domain_output.txt", "w") as file:
        file.write("0\n")
        file.write("0\n")
        file.write(str(len(signal)) + "\n")
        for index, value in enumerate(signal):
            if index == len(signal) - 1:
                file.write(f"{index} {value}")
            else:
                file.write(f"{index} {value}\n")
                

def apply_comp():
    print("comparing signals")
    idx_or_amp_me,sig_or_phase_me,isfreq_me=get_signals()
    idx_or_amp_u,sig_or_phase_u,isfreq_u=get_signals()
    if isfreq_me:
        new_amp_me=[float(format(x,'.12f')) for x in idx_or_amp_me]
        new_amp_u=[float(format(x,'.12f')) for x in idx_or_amp_u]
        ans=SignalComapreAmplitude(new_amp_me,new_amp_u)
        print(f'The amplitude compare = {ans}')
        new_phase_me=[float(format(x,'.12f')) for x in sig_or_phase_me]
        new_phase_u=[float(format(x,'.12f')) for x in sig_or_phase_u]
        anss=SignalComaprePhaseShift(new_phase_me,new_phase_u)
        print(f'The phase shift compare = {anss}')
    else:
        new_amp_me=[float(format(x,'.12f')) for x in idx_or_amp_me]
        new_amp_u=[float(format(x,'.12f')) for x in idx_or_amp_u]
        ans=SignalComapreAmplitude(new_amp_me,new_amp_u)
        print(f'The amplitude compare = {ans}')




    

