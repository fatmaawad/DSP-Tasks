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

  
x1, y1 = get_signal_TimeDomain()
x2, y2 = get_signal_TimeDomain()
# corr=Corr(y1,y2)

c = normalized_cross_correlation(y1, y2)
Compare_Signals('Correlation\CorrOutput.txt', x1, c)
# Compare_Signals('Correlation\CorrOutput.txt',x1,c)

# Example usage:
signal = [3, 1, 4, 2, 5, 6, 7, 9, 8, 10]  # Replace this with your signal data
window_size = int(input("Enter the window size for moving average calculation: "))

moving_avg_result = moving_average(signal, window_size)
sig = fold_signal(signal)
# print(sig)
# print("Moving averages:", moving_avg_result)
# remove_dc_time_domain()



arr = np.array([3, 2, 1, 1, 5])
shifted_list = shift_list(arr)
print(shifted_list)

for item in shifted_list:
    print(*item)
