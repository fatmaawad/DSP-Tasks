def moving_average(x, window_size):
    
    y = []  # List to store the moving averages
    i = 0
    while i<len(x)-window_size+1:
        window = x[i : i+window_size]
        window_avg=(sum(window)/window_size)
        y.append(window_avg)
        i+=1
    return y

# Example usage:
signal = [3, 1, 4, 2, 5, 6, 7, 9, 8, 10]  # Replace this with your signal data
window_size = int(input("Enter the window size for moving average calculation: "))

moving_avg_result = moving_average(signal, window_size)
print("Moving averages:", moving_avg_result)
