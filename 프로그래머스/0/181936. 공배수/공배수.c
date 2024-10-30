#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

int solution(int number, int n, int m) {
    int answer = 0;
    return ((number % n) || (number % m)) == 0 ? 1 : 0 ;
}