from functools import reduce

def sum(a,b):
    return a+b

def mult(a,b):
    return a*b

def max1(a,b):
    return a if a>b else b

def min1(a,b):
    return a if a<b else b

lst = [1,4,5,7,2,6,3,6,9]

total = reduce(sum, lst)
print(total)

maxnum = reduce(max1,lst)
print(maxnum)
minnum = reduce(min1,lst)
print(minnum)
multnum = reduce(mult,lst)
print(multnum)
