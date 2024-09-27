import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(br.readLine());
        String[] testCases = new String[n];

        for (int i = 0; i < n; i++){
            testCases[i] = br.readLine();
        }

        for (int i = 0; i < n; i++){
            String testCase = testCases[i];
            int score = 0;
            int consecutive = 0;

            for (int j = 0; j < testCase.length(); j++){
                if (testCase.charAt(j) == 'O') {
                    consecutive++;
                    score += consecutive;
                } else {
                    consecutive = 0;
                }
            }
            System.out.println(score);
        }

    }
}
