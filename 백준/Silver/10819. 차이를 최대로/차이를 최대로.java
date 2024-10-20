import java.util.Scanner;

public class Main {
    static int maxDifference = 0;

    private static int returnValue(int[] arr){
        int sum = 0;
        for (int i = 0; i < arr.length - 1; i++){
            sum += Math.abs(arr[i] - arr[i + 1]);
        }
        return sum;
    }
    static void swap(int[] arr, int i, int j){
        int temp = arr[i];
        arr[i] = arr[j];
        arr[j] = temp;
    }
    static void permute(int[] arr, int start, int N){
        if (start == N){
            int sum = returnValue(arr);
            if (sum > maxDifference) {
                maxDifference = sum;
            }
        } else {
            for (int i = start; i < N; i++){
                swap(arr, start, i);
                permute(arr, start + 1, N);
                swap(arr, i, start);
            }
        }

    }

    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);

        int N = sc.nextInt();
        int[] arr = new int[N];
        for(int i = 0; i < N; i++){
            arr[i] = sc.nextInt();
        }
        permute(arr, 0, N);

        System.out.println(maxDifference);
    }
}
