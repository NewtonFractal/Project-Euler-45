import math
import time
start = time.time()

def Tri_Pen_Hex(number):
    if ((math.sqrt(24*number+1)+1)/6).is_integer() == True:
            print(int(number))
            end = time.time()
            print(end - start)
            exit()
    else:
        return None

def Hex_Number_Geberator():
    for x in range(286,100000000):
        y = x*(2*x-1)
        Tri_Pen_Hex(y)

Hex_Number_Geberator()


