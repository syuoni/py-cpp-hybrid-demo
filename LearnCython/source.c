#include <math.h>
#include <stdio.h>
#include <malloc.h>

double c_mean(double* in_array, int size)
{
    int i;
    double sum=0;
    for(i=0;i<size;i++){
        sum += in_array[i];
    }
    return sum/size;
}
