import java.util.Scanner;

public class Main {
    public static void main(String[] args){
        Scanner scanner = new Scanner(System.in);
        
        int N = scanner.nextInt();
        int K = scanner.nextInt();

        int[] A = new int[2*N];
        for (int i = 0; i < 2 * N; i++) {
            A[i] = scanner.nextInt();
        }
        
        System.out.println(conveyorBelt(N, K, A));

        scanner.close();
    }


    public static int conveyorBelt(int N, int K, int[] A){
        int step = 0;
        boolean[] robot = new boolean[N];

        while (true) {
            step++;

            int temp = A[A.length - 1];
            for (int i = A.length - 1; i> 0; i--) {
                A[i] = A[i-1];
            }
            A[0] = temp;

            for (int i = robot.length - 1; i > 0; i--) {
                robot[i] = robot[i-1];
            }
            robot[0] = false;

            if (robot[N-1]) {
                robot[N-1] = false;
            }

            for (int i = N - 2; i >= 0; i--) {
                if (robot[i] && !robot[i+1] && A[i+1] > 0) {
                    robot[i] = false;
                    robot[i+1] = true;
                    A[i+1]--;
                }
            }

            if (robot[N-1]) {
                robot[N-1] = false;
            }

            if (A[0]>0) {
                robot[0] = true;
                A[0]--;
            }

            int tcount = 0;
            for (int a : A) {
                if (a == 0) {
                    tcount++;
                }
            }
            if (tcount >= K) {
                return step;
            }
            

            
        }
    }
}