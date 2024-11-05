#include <stdio.h>
#include <stdlib.h>

int compare(const void* a, const void* b){
    int* line1 = *(int**)a;
    int* line2 = *(int**)b;
    if (line1[0] == line2[0]){
        return line1[1] - line2[1];
    } 
    return line1[0] - line2[0];
}

int calculate_total_length(int** dots, int n){
    int total_length = 0;
    int base_x = dots[0][0];
    int base_y = dots[0][1];

    for(int i = 1; i < n; i++){
        int x = dots[i][0];
        int y = dots[i][1];

        if (base_y > x){
            if (base_y < y){
                base_y = y;
            }
        } else {
            total_length += base_y - base_x;
            base_x = x;
            base_y = y;
        }
    }
    total_length += base_y - base_x;
    return total_length;
}

int main(void){
    int n;
    scanf("%d", &n);
    
    int** dots = (int**)malloc(n * sizeof(int*));
    for (int i = 0; i < n; i++ ){
        dots[i] = (int*)malloc(2 * sizeof(int));
        scanf("%d %d", &dots[i][0], &dots[i][1]);
    }

    qsort(dots, n, sizeof(int*), compare);

    int result = calculate_total_length(dots, n);

    printf("%d\n", result);
    
    for (int i = 0; i < n; i++){
        free(dots[i]);
    }
    free(dots);
    return 0;
}