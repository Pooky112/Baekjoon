#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

// 파라미터로 주어지는 문자열은 const로 주어집니다. 변경하려면 문자열을 복사해서 사용하세요.
char* solution(const char* code) {
    // return 값은 malloc 등 동적 할당을 사용해주세요. 할당 길이는 상황에 맞게 변경해주세요.
    char* answer = (char*)malloc(strlen(code) + 1);
    int idx = 0;
    int mode = 0;
    for (int i = 0; i < strlen(code); i++){
        if (code[i] == '1'){
            mode = 1 - mode;
        } else{
            if( (mode == 0 && i % 2 == 0) || (mode == 1 && i % 2 == 1)) {
                answer[idx++] = code[i];
            }
        }
    }
    answer[idx] = '\0';
    if (idx == 0){
        strcpy(answer,"EMPTY");
    }
    return answer;
}