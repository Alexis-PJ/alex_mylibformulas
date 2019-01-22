
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

def distance2d(x1,y1,x2,y2):
    d = math.sqrt((x1 -x2)**2 + (y1 -y2)**2)
    return d

def distance3d(x1,y1,z1,x2,y2,z2):
    b = math.sqrt((x1 -x2)**2 + (y1 -y2)**2 + (z1 -z2)**2)
    return b

def eliminate_repeats(oldlist):
    newlist = []
    for letter in oldlist:
        if letter not in newlist:
            newlist.append(letter)
    return newlist

def convert_list_2word(alist):
    n = len(alist)
    new_word = ''
    for i in range(n):
        new_word = new_word + alist[i]
    return new_word

def translate(text1,dict1):
    list_text = text1.split()
    new_list =[]
    for word in list_text:
        translation = dict1.get(word)
        new_list.append(translation if translation else word)
    return ' '.join(new_list)
