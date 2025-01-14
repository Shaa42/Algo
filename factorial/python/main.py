def factorial(n):
    if n < 0:
        return None
    if n == 0 or n == 1:
        return 1
    
    if memo[n] != -1:
        return memo[n]
    
    else :
        fact = factorial(n-1) * n
        memo[n] = fact
        return fact

n = 20
memo = [-1] * (n+1)
nombre = factorial(n)
print(nombre)