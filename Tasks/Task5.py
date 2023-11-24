import numpy as np
from comparesignals import SignalSamplesAreEqual

from helper_functions import *

def plot_freq(x, y, x_lable, y_lable, fig, canv, flg=False):
    fig.clear()
    fig.supxlabel(x_lable)
    fig.supylabel(y_lable)
    ax=fig.add_subplot(111)
    if flg:
        fig.supxlabel("Time")
        ax.plot(x,y)
    else:
        ax.stem(x, y)
    canv.draw()

def write_file(indecies,samples):
  with open('dct_output.txt', 'w') as f:
    f.write('0\n')
    f.write('1\n')
    f.write(str(len(indecies))+'\n')
    for index,line in enumerate(indecies):
      if(index==(len(indecies)-1)):
        f.write(str(line)+' '+str(samples[index]))
      else:
        f.write(str(line)+' '+str(samples[index])+'\n')
  f.close()
  
  
def compute_dct(m_first_coefficients):
    data_index, domain_samples = get_signals()
    if data_index is not None and domain_samples is not None:  # Ensure valid data is retrieved
        indecies = list(data_index)
        samples = np.array(domain_samples, dtype=float)

        if samples.size > 0:  # Check if samples is not empty
            N = len(samples)
            Yk = []

            for k in range(N):
                summation = 0
                for n in range(N):
                    summation += samples[n] * np.cos((np.pi / (4 * N)) * (2 * n - 1) * (2 * k - 1))

                Y_current = np.sqrt(2 / N) * summation
                Yk.append(Y_current)

            SignalSamplesAreEqual("D:\DSP\Task 1\DCT\DCT_output.txt", indecies, Yk)
            plot_signal(indecies, Yk, "dct")
            write_file(indecies[:m_first_coefficients], samples[:m_first_coefficients])
        else:
            print("Samples are empty or invalid.")
    else:
        print("No valid data retrieved.")
    
    
def remove_dc_component():
    data_index, domain_samples = get_signals()
    if data_index is not None and domain_samples is not None:  # Ensure valid data is retrieved
        indecies = list(data_index)
        samples = domain_samples

        mean_sample = np.mean(samples)
        N = len(samples)
        after_remove = [samples[k] - mean_sample for k in range(N)]

        SignalSamplesAreEqual("D:\DSP\Task 1\Remove DC component\DC_component_output.txt", indecies, after_remove)
    else:
        print("No valid data retrieved.")