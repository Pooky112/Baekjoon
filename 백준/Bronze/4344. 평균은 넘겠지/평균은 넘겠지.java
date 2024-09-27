import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int c = Integer.parseInt(br.readLine());

        for (int i = 0; i < c; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            int n = Integer.parseInt(st.nextToken());
            int[] testCase = new int[n];

            int sum = 0;
            for (int j = 0; j < n; j++){
                testCase[j] = Integer.parseInt(st.nextToken());
                sum += testCase[j];
            }

            double avg = (double) sum / n;
            int aboveAvgCount = 0;

            for (int score : testCase) {
                if (score > avg){
                    aboveAvgCount++;
                }
            }

            double percentage = ((double) aboveAvgCount / n) * 100;

            System.out.printf("%.3f%%%n", percentage);
        }
    }
}
