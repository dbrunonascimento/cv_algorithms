def fibonacci(n):
    r = [-1]*(n + 1)
    return fibonacci_h(n, r)
 
 
def fibonacci_h(n, r):
  
    if r[n] >= 0:
        return r[n]
 
    if (n == 0 or n == 1):
        q = n
    else:
        q = fibonacci_h(n - 1, r) + fibonacci_h(n - 2, r)
    r[n] = q
 
    return q
 
 
n = int(input('Enter n: '))
 
answer = fibonacci(n)
print('The nth Fibonacci number:', answer)
