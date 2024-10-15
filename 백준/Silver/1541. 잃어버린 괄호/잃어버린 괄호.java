import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        String expression = br.readLine();
        String[] separated = expression.split("-");
        int[] answer = new int[separated.length];

        for (int i = 0; i < separated.length; i++){
            if (separated[i].contains("+")){
                String[] temp = separated[i].split("\\+");
                for (String str: temp){
                    answer[i] += Integer.parseInt(str);
                }
            } else{
                answer[i] = Integer.parseInt(separated[i]);
            }
        }
        for (int i = 1; i < answer.length; i++){
            answer[0] -= answer[i];
        }
        System.out.println(answer[0]);
    }
}
