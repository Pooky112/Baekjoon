import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;
import java.util.Arrays;

public class Main {
    public static long maxSum(int n, int[] arr) {
        Arrays.sort(arr);
        int i = 0;
        int j = n - 1;
        long sum = 0;

        while (i < n - 1 && arr[i] < 0 && arr[i + 1] <= 0) {
            sum += (long) arr[i] * arr[i + 1];
            i += 2;
        }

        while (j > 0 && arr[j] > 1 && arr[j - 1] > 1) {
            sum += (long) arr[j] * arr[j - 1];
            j -= 2;
        }

        while (i <= j) {
            sum += arr[i];
            i++;
        }

        return sum;
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(br.readLine());
        int[] arr = new int[n];

        for (int i = 0; i < n; i++) {
            arr[i] = Integer.parseInt(br.readLine());
        }

        long sum = maxSum(n, arr);
        System.out.println(sum);
    }
}
