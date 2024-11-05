#include <stdio.h>


int white = 0;
int blue = 0;

void count_papers(int papers[128][128], int x, int y, int n){
    int initial_color = papers[x][y];

    for (int i = x; i < x + n; i++){
        for(int j = y; j < y + n; j++){
            if(initial_color != papers[i][j]){
                int next_n = n / 2;
                count_papers(papers, x, y, next_n);
                count_papers(papers, x + next_n, y, next_n);
                count_papers(papers, x, y + next_n, next_n);
                count_papers(papers, x + next_n, y+ next_n, next_n);
                return;
            }
        }
    }
    if(initial_color == 1){
        blue++;
    } else{
        white++;
    }
}

int main(void){
    int n;
    scanf("%d", &n);
    int papers[128][128];
    for (int i = 0; i < n; i++){
        for(int j = 0; j < n; j++){
            scanf("%d", &papers[i][j]);
        }
    }

    count_papers(papers, 0, 0, n);

    printf("%d\n", white);
    printf("%d\n", blue);

    return 0;
}