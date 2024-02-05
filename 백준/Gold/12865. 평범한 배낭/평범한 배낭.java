import java.util.Scanner;

public class Main{
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        
        int N = scanner.nextInt();
        int K = scanner.nextInt();
        
        int[][] items = new int[N][2];
        for(int i = 0; i < N; i++) {
            items[i][0] = scanner.nextInt();
            items[i][1] = scanner.nextInt();
        }
        
        int maxValue= knapsack(N, K, items);
        System.out.println(maxValue);
    }
    
    public static int knapsack(int N, int K, int[][] items) {
        int[][] dp = new int[N+1][K+1];
        
        for(int i = 1; i <= N; i++) {
            for(int w = 1; w <= K; w++){
                if(items[i-1][0] <= w) {
                    dp[i][w] = Math.max(dp[i-1][w], dp[i-1][w-items[i-1][0]]+ items[i-1][1]);
                }
                else {
                    dp[i][w] = dp[i -1][w];
                }
            }
        }
        return dp[N][K];
    }
}