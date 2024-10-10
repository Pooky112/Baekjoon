import java.util.Scanner;

public class Main {
    private static int N;
    private static int[] row;
    private static int count;

    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        N = sc.nextInt();
        row = new int[N];

        nQueen(0);
        System.out.println(count);
    }

    private static void nQueen(int n) {
        if (n == N){
            count++;
            return;
        }

        for (int i = 0; i < N; i++){
            row[n] = i;
            if (isSafe(n)) {
                nQueen(n + 1);
            }
        }
    }

    private static boolean isSafe(int n) {
        for (int i = 0; i < n; i++){
            if (row[n] == row[i] || Math.abs(row[n] - row[i]) == Math.abs(n - i)){
                return false;
            }
        }
        return true;
    }
}
