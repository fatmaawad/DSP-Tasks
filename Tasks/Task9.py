import numpy as np
from Task4 import *
import math
from Convolution.ConvTest import ConvTest
from Fast_Correlation.CompareSignal import Compare_Signals



def fast_convolution(signal, filter,ind1,ind2):

  # Zero-pad both signal and filter to equal length
  signal_length = len(signal)
  filter_length = len(filter)
  padded_length = signal_length + filter_length - 1
  padded_signal = np.pad(signal, (0, padded_length - signal_length), 'constant')
  padded_filter = np.pad(filter, (0, padded_length - filter_length), 'constant')


  # Apply DFT to both padded signal and filter
  dft_signal=np.round(dft(padded_signal),1)
  dft_filter=np.round(dft(padded_filter),10)

   # Multiply in frequency domain
  dft_result=np.array(dft_signal) * np.array(dft_filter)

  # Apply IDFT to obtain convolution result
  convolution_result=np.round(idft(dft_result),1)
  output = np.round(convolution_result[:signal_length + filter_length - 1],1)

 #compute indices
  newmin = int(min(ind1) + min(ind2))
  newmax = int(max(ind1) + max(ind2))
  new_indices = list(range(newmin, newmax + 1))
  #print(new_indices)

  ConvTest(new_indices, output)
  return output,new_indices

  

def fast_auto_correlation(signal):
    signal1 = DFT(signal)
    signal2 = signal1.conjugate()
    signal1 = np.array(signal1)
    signal2 = np.array(signal2)
    mult = signal1 * signal2
    amp,phase = amp_and_faze(mult)
    new_amp=[abs(s) for s in amp]
    result = IDFT(new_amp,phase)
    
    return result


def fast_cross_correlation(signal1,signal2):
    sig1 = DFT(signal1)
    print(sig1)
    n = len(sig1)
    sig1 = sig1.conjugate()
    # print(xk1)
    sig2 = DFT(signal2)
    sig1 = np.array(sig1)
    sig2 = np.array(sig2)
    mult = sig1 * sig2
    amp,phase = amp_and_faze(mult)
    new_amp=[abs(s) for s in amp]
  
    result = IDFT(new_amp,phase)
   
    result = [x/n for x in result]
    print (result)
    return result


def fast_correlation(signal1, signal2=None):
    # If only one signal is given, perform auto-correlation by default
    if signal2 is None:
        signal2 = signal1
    
    # Compute the Discrete Fourier Transform (DFT) of the signals
    sig1 = DFT(signal1)
    sig1_conj = sig1.conjugate()
    sig1 = np.array(sig1_conj)
    sig2 = DFT(signal2)
    sig1 = np.array(sig1)
    sig2 = np.array(sig2)
    
    # Calculate the element-wise multiplication of the transformed signals
    mult = sig1 * sig2
    
    # Compute the amplitude and phase of the multiplication result
    amp, phase = amp_and_faze(mult)
    
    # Calculate the absolute values of the amplitude
    new_amp = [abs(s) for s in amp]
    
    # Check if the input signals are equal for auto-correlation
    if np.array_equal(signal1, signal2):  # Auto-correlation case
        result = IDFT(new_amp, phase)
    else:  # Cross-correlation case
        n = len(sig1)
        result = IDFT(new_amp, phase)
        result = [x / n for x in result]
    
    return result
