import numpy as np


def add_signals(x1,y1,y2,y3):
    result_x=x1
    result_y=y1+y2+y3
    return result_x, result_y



def subtract_signals(x1,y1,y2,y3):
    result_x=x1
    result_y=y3-y2-y1
    return result_x, result_y


def multiply_signal(x, y, constant):
    result_y = y * constant
    return x, result_y

def square_signal(x, y):
    result_y = y ** 2
    return x, result_y

def shift_signal(x,y,cons):
    result_y=y+cons
    return x, result_y
def accumulate_signal(x,y):
    result = np.cumsum(y)
    return result