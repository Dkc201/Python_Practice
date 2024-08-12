##Factorial

def fact(n):
    if n == 1:
        return 1
    else:
      return  n*fact(n-1)
n = 5
print(f"factorial of {n} = ",fact(n))

def fibo(n):
    if n==1:
        return 0
    if n==2:
        return 1
    return (fibo(n-2) + fibo(n-1))
n = 8
print(f"fibonacci number of {n} =  ",fibo(n))

for i in range(1,n+1):
    print(fibo(i),end= " ")



