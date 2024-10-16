import java.util.Arrays;
import java.util.Scanner;

public class Main {
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        int[] dwarfs = new int[9];
        int totalSum = 0;

        for (int i = 0; i < 9; i++){
            dwarfs[i] = sc.nextInt();
            totalSum += dwarfs[i];
        }

        outerLoop:
        for (int i = 0; i < 9; i++){
            for (int j = i + 1; j < 9; j++) {
                if (totalSum - dwarfs[i] - dwarfs[j] == 100){
                    dwarfs[i] = dwarfs[j] = -1;
                    break outerLoop;
                }
            }
        }

        Arrays.sort(dwarfs);
        for(int i = 2; i < 9; i++) {
            System.out.println(dwarfs[i]);
        }
    }
}
