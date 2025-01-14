def factorial(n):
    """
    Estimated complexity : O(n)
    """
    
    if n < 0:
        return None
    
    # Base case
    if n == 0 or n == 1:
        return 1
    
    # If already in memory, return the value
    if memo_fact[n] != -1:
        return memo_fact[n]
    
    else :
        # Factorial recursion
        fact = factorial(n-1) * n
        
        # Memoization
        memo_fact[n] = fact
        
        return fact

def coeff_bin(n, k):
    if k > n:
        return None
    
    coeff = factorial(n) // (factorial(k) * factorial(n-k))
    return coeff


if __name__ == '__main__':
    n = 20
    k = 4

    memo_fact = [-1] * (n+1)
    nombre = coeff_bin(n, k)
    print(nombre)