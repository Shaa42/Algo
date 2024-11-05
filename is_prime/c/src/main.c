#include <stdio.h>
#include <stdbool.h>
#include <math.h>

bool isPrime(int number){
    if (number <= 1) return false;

    int sqrt_number = (int)sqrt(number);
    for (int i = 2; i < sqrt_number + 1; i++ ){
        if (number % i == 0) return false;
    }

    return true;
}

int main(){
    for (int i = 0; i < 100; i++){
        bool prime = isPrime(i);
        if (prime)
            printf("%d est un nombre premier.\n", i);
    }
    
    return 0;
}