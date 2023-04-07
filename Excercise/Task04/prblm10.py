tuple = [(20, 6), (100, 3), (15, 12), (300, 9)]

def Sort(tuple): 
    return(sorted(tuple, key = lambda a: a[1]))  

print(Sort(tuple))