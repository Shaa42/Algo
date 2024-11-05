from math import sqrt

def isPrime(number):
    if number <= 1:
        return False
    
    for i in range(2, round(sqrt(number)) + 1):
        if number % i == 0:
           return False
       
    return True 

if __name__ == "__main__":
    jdt = [x for x in range(100)]
    for nombre in jdt:
        if isPrime(nombre):
            print(nombre, " est un nombre premier.")
