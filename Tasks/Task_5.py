from helper_functions import *
from Task4 import *
from Correlation.CompareSignal import Compare_Signals


# def Corr (X1,X2):
#     #correlation
#         x1 = X1
#         x2 = X2
#         N = len(x1)
#         sum_X1 = 0
#         sum_X2 = 0
#         for i in range(len(x1)):
#             sum_X1 += x1[i] ** 2
#         for i in range(len(x2)):
#             sum_X2 += x2[i] ** 2

#         bottom_Num = ((sum_X1*sum_X2) ** 0.5)/N

#         corr = []
#         for _ in range(N):
#             Cur_Res = np.sum(x1 * x2)
#             corr.append((Cur_Res / N) / bottom_Num)

#             x2 = np.roll(x2, 1)
#         # for j in range(N):
#         #     Cur_Res = 0
#         #     for i in range(N):
#         #         Cur_Res += (x1[i]*x2[i])

#         #     tem = x2[0]
#         #     x2.pop(0)
#         #     x2.append(tem)
#         #     corr.append(((Cur_Res)/N)/bottom_Num)

#         return corr
def Corr(X1, X2):
    x1 = X1
    x2 = X2
    N = len(x1)

    # Ensure both signals are of the same length
    if len(x2) != N:
        raise ValueError("Signals must have the same length")

    sum_X1 = sum(x1)
    sum_X2 = sum(x2)

    sum_X1_sq = sum(val ** 2 for val in x1)
    sum_X2_sq = sum(val ** 2 for val in x2)

    bottom_Num = ((sum_X1_sq * sum_X2_sq) ** 0.5) / N

    corr = []

    for shift in range(N):
        cur_res = sum(x1[i] * x2[i - shift] for i in range(N))

        corr.append(cur_res / bottom_Num)

    return corr

def shift_list(arr):
    output = []
    for _ in range(len(arr)):
        arr = arr[1:] + [arr[0]]
        output.append(arr)
        
    shifted_arr = np.roll(arr, -1)
    return shifted_arr

def normalized_cross_correlation(x1, x2):
    # Calculate the length of the signals
    N = len(x1)

    count_x1 = np.sum(np.square(x1))
    count_x2 = np.sum(np.square(x2))

    correlation = np.zeros(len(x1))
    denominator = (1 / N) * ((count_x1 * count_x2) ** 0.5)
    print(denominator)
    ncc_values = []

    for shift in range(len(x1)):
       
        correlation = (1/N) * np.sum(x1 * x2)
        ncc = correlation/ denominator
        ncc_values.append(ncc)
        x2=np.roll(x2,-1)

        
        print(ncc_values)
    return ncc_values



def moving_average(x, window_size):
    y = []  # List to store the moving averages
    i = 0
    while i < len(x) - window_size + 1:
        window = x[i: i + window_size]
        window_avg = (sum(window) / window_size)
        y.append(window_avg)
        i += 1
    return y


def fold_signal(signal):
    folded_signal = signal[::-1]
    return folded_signal


def remove_dc_time_domain():
    x, y = get_signal_TimeDomain()
    # comp=dft(y)
    # print(comp)
    # comp[0]=0
    # print(comp)
    amp, faze, N = DFT(y)
    amp[0] = 0
    faze[0] = 0
    print(amp)
    print(faze)


import numpy as np
from Task4 import *
import cmath
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


def DFT(sig):
    N =len(sig)
    n=np.arange(N)
    xK=np.zeros(N,dtype=np.complex128)
    for i in range(N):
        xK[i]+=np.sum(sig*np.exp(-2j*np.pi*i*n/N))
    return xK

def amp_and_faze(xK):
    A=[]
    phase=[]
    for x in xK:
        A.append(np.sqrt((x.real**2) + (x.imag**2)))
        phase.append( math.atan2(x.imag,x.real))
    return A,phase

def fast_auto_correlation(signal):
    sig1=DFT(signal)
    sig1_conj=np.conjugate(sig1)
    sig2=sig1_conj
    sig1=np.array(sig1)
    sig2=np.array(sig2)
    mult=sig1*sig2
    amp,faze=amp_and_faze(mult)
    result=IDFT(amp,faze)
    return result

def fast_cross_correlation(signal1,signal2):
    sig1=DFT(signal1)
    print(sig1)
    sig1_conj=np.conjugate(sig1)
    # print(sig1_conj)
    sig1=sig1_conj
    sig2=DFT(signal2)
    sig1=np.array(sig1)
    sig2=np.array(sig2)
    N=len(signal1)
    mult=sig1*sig2
    amp,faze=amp_and_faze(mult)
    result=IDFT(amp,faze)
    result=[x/N for x in result]
    print (result)
    # Compare_Signals(file_name,Your_indices,Your_samples)
    return result
   
    
    
    


x1, y1 = get_signal_TimeDomain()
x2, y2 = get_signal_TimeDomain()
# corr=Corr(y1,y2)

c = fast_cross_correlation(y1, y2)
Compare_Signals('Fast_Correlation\Corr_Output.txt', x1, c)
# Compare_Signals('Correlation\CorrOutput.txt',x1,c)

# Example usage:




