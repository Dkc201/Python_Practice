def square(fun):
    def inner(a,b):
        x = a*a
        y = b*b
        return add(x,y)
    return inner

@square
def add(a,b):
    return a+b
#addition = square(add)
print(add(2,3))
