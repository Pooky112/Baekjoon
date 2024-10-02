import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    private static boolean isPrime(int num) {
        if (num < 2){
            return false;
        }
        for (int i = 2; i <= Math.sqrt(num); i++) {
            if (num % i == 0) {
                return false;
            }
        }
        return true;
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int N = Integer.parseInt(br.readLine());
        String[] numbers = br.readLine().split(" ");

        int primeCount = 0;

        for (int i = 0; i < N; i++){
            int num = Integer.parseInt(numbers[i]);

            if (isPrime(num)){
                primeCount++;
            }
        }
        System.out.println(primeCount);
    }


}
