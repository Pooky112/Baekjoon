#include <stdio.h>
#include <math.h>
#include <stdlib.h>
#include <limits.h>

typedef struct {
    int x;
    int y;
} Dot;

int compare_x(const void* a, const void* b){
    Dot* p1 = (Dot*)a;
    Dot* p2 = (Dot*)b;
    return p1->x - p2->x;
}
int compare_y(const void* a, const void* b){
    Dot* p1 = (Dot*)a;
    Dot* p2 = (Dot*)b;
    return p1->y - p2->y;
}

int distance(Dot a, Dot b){
    return pow(a.x - b.x, 2)+ pow(a.y - b.y, 2);
}

int closest_pair(Dot* dots, int left, int right){
    if (right - left <= 3) {
        int min_dist = INT_MAX;
        for (int i = left; i < right; i++){
            for (int j = i + 1; j < right; j++){
                min_dist = fmin(min_dist, distance(dots[i], dots[j]));
            }
        }
        return min_dist;
    }

    int mid = left + (right - left) / 2;
    int mid_x = dots[mid].x;

    int left_min = closest_pair(dots, left, mid);
    int right_min = closest_pair(dots, mid, right);
    int min_dist = fmin(left_min, right_min);

    Dot* strip = (Dot*)malloc((right-left) * sizeof(Dot));

    int strip_size = 0;
    for (int i = left; i < right; i++){
        if (pow(dots[i].x - mid_x,2) < min_dist) {
            strip[strip_size++] = dots[i];
        }
    }

    qsort(strip, strip_size, sizeof(Dot), compare_y);

    for (int i = 0; i < strip_size; i++){
        for (int j = i + 1; j < strip_size && pow(strip[j].y - strip[i].y,2) < min_dist; j++){
            min_dist = fmin(min_dist, distance(strip[i], strip[j]));
        }
    }
    free(strip);
    
    return min_dist;
}

int main(void){
    int n;
    scanf("%d", &n);

    Dot* dots = (Dot*)malloc(n * sizeof(Dot));
    for (int i = 0; i < n; i++) {
        scanf("%d %d", &dots[i].x, &dots[i].y);
    }

    qsort(dots, n, sizeof(Dot), compare_x);
    int result = closest_pair(dots, 0, n);

    printf("%d\n", result);

    free(dots);

    return 0;
}