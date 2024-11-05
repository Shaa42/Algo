#include <stdio.h>

void bubble_sort(int array[], int array_size){
    for (int i = 0; i < array_size; i++){
        for (int j = 0; j < (array_size - 1); j++){
            if (array[j+1] < array[j]){
                int temp = array[j+1];
                array[j+1] = array[j];
                array[j] = temp;
            }
        }
    }
}

void print_intarray(int array[], int array_size){
    for (int i = 0; i < array_size; i++)
        printf("%d ", array[i]);
    printf("\n");
}

int main(){
    int array_tosort[6] = {2, 0, 1, 5, -2, 1};
    int length = 6;
    
    print_intarray(array_tosort, length);
    bubble_sort(array_tosort, length);
    print_intarray(array_tosort, length);

    return 0;
}