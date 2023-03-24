# 1. Keep the first, middle, and last characters of an input string.
import math
string = str(input("Enter a string: "))
def position(name):
    l = len(name)
    print("First , middle and last character are: ")
    print(name[0],name[math.ceil((l/2))-1],name[l-1])

position(string)

