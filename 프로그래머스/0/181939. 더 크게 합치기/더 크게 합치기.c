#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

int solution(int a, int b) {
    char ab[10], ba[10];
    sprintf(ab, "%d%d",a,b);
    sprintf(ba, "%d%d", b, a);
    int ab_val = atoi(ab);
    int ba_val = atoi(ba);
    return ab_val > ba_val ? ab_val : ba_val;
}