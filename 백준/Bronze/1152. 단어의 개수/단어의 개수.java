import java.util.Scanner;

public class Main {
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);

        String inputString = sc.nextLine().trim();

        if (inputString.isEmpty()){
            System.out.println(0);
        } else {
            String[] words = inputString.split("\\s+");
            System.out.println(words.length);
        }

        sc.close();
    }
}
