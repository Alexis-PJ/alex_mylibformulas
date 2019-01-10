
import math


def fibon_sequence(n):# this the definiton of the function
    x = 1
    y = 1
    cont = 1
    while cont <= n: # is the parameter of the function, that should be given
                     # when the funtion is new
        print('a fibon number is:', x + y)

        temp = x
        x = y
        y = y + temp
        cont = cont + 1
fibon_sequence(20)

def swap(a,b):
    temp = a
    a = b
    b = temp
    return print(a,b)