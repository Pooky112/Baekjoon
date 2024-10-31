#include <stdio.h>
#include <stdlib.h>

int compare(const void* a, const void* b) {
    return *(int*)a - *(int*)b;
}

int can_place(int* houses, int distance, int n, int c){
    int count = 1;
    int last_position = houses[0];

    for(int i = 0; i < n; i++){
        if (houses[i] - last_position >= distance){
            count += 1;
            last_position = houses[i];
            if(count == c){
                return 1;
            }
        }
    }
    return 0;
}

int find_max_distance(int* houses, int n, int c){
    qsort(houses, n, sizeof(int), compare);

    int low = 1;
    int high = houses[n - 1] - houses[0];
    int result = 0;

    while (low <= high){
        int mid = (low + high) / 2;
        if (can_place(houses, mid,n, c)){
            result = mid;
            low = mid + 1;
        } else {
            high = mid - 1;
        }
    }
    return result;
}

int main(void)
{
    int n, c;
    scanf("%d %d", &n, &c);

    int* houses = (int*)malloc(n * sizeof(int));
    for (int i = 0; i < n; i++){
        scanf("%d", &houses[i]);
    }

    int result = find_max_distance(houses, n, c);
    printf("%d\n", result);

    free(houses);
    return 0;
}
