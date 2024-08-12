#Factorial
result = 1
n = 8
for i in range(1,n+1):
    result = result*i
print(result)

#Fibonacci
fibo_series = [0,1]
n = 10
for i in range(2,n+1):
    fibo_series.append(fibo_series[i-2]+fibo_series[i-1])
print(fibo_series[n])

