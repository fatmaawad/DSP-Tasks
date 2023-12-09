import numpy as np
from Correlation.CompareSignal import Compare_Signals

def normalized_cross_correlation(x1, x2):
    N = len(x1)
    count_x1 = np.sum(np.square(x1))
    count_x2 = np.sum(np.square(x2))

    correlation = np.zeros(len(x1))
    denominator = (1 / N) * ((count_x1 * count_x2) ** 0.5)
    # print(denominator)
    ncc_values = []

    for _ in range(len(x1)):
        correlation = (1/N) * np.sum(x1 * x2)  #numerator 
        ncc = correlation/ denominator
        ncc_values.append(ncc)
        x2=np.roll(x2,-1)        
        # print(ncc_values)

    return ncc_values