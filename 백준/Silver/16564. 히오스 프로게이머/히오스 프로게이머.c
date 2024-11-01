#include <stdio.h>
#include <stdlib.h>

int compare(const void* a, const void* b){
    return *(int*)a - *(int*)b;
}

int can_up(int* levels, int mid, int n, int k){
    int sum = 0;
    for (int i = 0; i < n; i++){
        if (levels[i] < mid) {
            sum += mid - levels[i];
            if (sum > k) {
                return 0;
            }
        }
    }
    return 1;
}

int main(void){
    int n, k;
    scanf("%d %d", &n, &k);

    int* levels = (int*)malloc(n * sizeof(int));
    for (int i = 0; i < n; i++){
        scanf("%d", &levels[i]);
    }

    qsort(levels, n, sizeof(int), compare);

    int low = levels[0];
    int high = levels[0] + k;
    int result = 0;
    while (low <= high){
        int mid = (low + high) / 2;
        if (can_up(levels, mid, n, k)){
            result = mid;
            low = mid + 1;
        } else {
            high = mid - 1;
        }
    }
    printf("%d\n", result);

    free(levels);

    return 0;
}