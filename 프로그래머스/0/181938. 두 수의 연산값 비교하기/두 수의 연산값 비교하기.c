#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

int solution(int a, int b) {
    char ab[10];
    sprintf(ab, "%d%d", a, b);
    int ab_val = atoi(ab);
    int ab2_val = 2 * a * b;
    
    return ab_val > ab2_val ? ab_val : ab2_val;
}