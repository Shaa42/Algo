def fibonacci(n):
    if n < 0:
        return None
    
    # Base case
    if n == 0:
        return 0
    if n == 1:
        return 1
    
    # If already in memory, return the value
    if mem[n] != -1:
        return mem[n]
    
    else :    
        # Fibonacci recursion
        fibo = fibonacci(n-1) + fibonacci(n-2)
        
        # Put the value in memory
        mem[n] = fibo
        return fibo

n = 19
mem = [-1] * (n+1)
nombre = fibonacci(n)
print(nombre)