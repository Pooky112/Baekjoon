import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        int[] currentGroup = new int[N];
        int[] correctGroup = new int[N];
        int[] diff = new int[N];

        String[] tempArr = br.readLine().split(" ");
        for (int i = 0; i < N; i++){
            currentGroup[i] = Integer.parseInt(tempArr[i]);
        }
        tempArr = br.readLine().split(" ");
        for (int i = 0; i < N; i++){
            correctGroup[i] = Integer.parseInt(tempArr[i]);
            diff[i] = correctGroup[i] - currentGroup[i];
        }

        int[] count = new int[N];
        count[0] = Math.abs(diff[0]);

        for (int i = 1; i < N; i++){
            if (diff[i] * diff[i - 1] > 0){
                count[i] = count[i - 1] + Math.max(0, Math.abs(diff[i]) - Math.abs(diff[i-1]));
            } else {
                count[i] = count[i - 1] + Math.abs(diff[i]);
            }
        }


        System.out.println(count[N-1]);
    }
}
