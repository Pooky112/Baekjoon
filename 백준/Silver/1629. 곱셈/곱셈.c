#include <stdio.h>

int solution(int a, int b, int c){
    if (b == 0){
        return 1;
    }

    long long half = solution(a, b / 2, c);
    half = (half * half) % c;

    if (b % 2 == 0){
        return half;
    } else {
        return (half * a) % c;
    }
}

int main(void){
    int a, b, c;
    scanf("%d %d %d", &a, &b, &c);
    int result = solution(a, b, c);
    printf("%d\n", result);

    return 0;
}