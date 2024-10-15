import java.util.Comparator;
import java.util.Scanner;
import java.util.Set;
import java.util.TreeSet;

public class Main {
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);

        int N = sc.nextInt();
        sc.nextLine();

        Set<String> words = new TreeSet<>(new Comparator<String>() {
            @Override
            public int compare(String word1, String word2) {
                if(word1.length() != word2.length()){
                    return word1.length() - word2.length();
                } else {
                    return word1.compareTo(word2);
                }
            }
        });
        for (int i = 0; i < N; i++){
            words.add(sc.nextLine().trim());
        }

        for (String word: words){
            System.out.println(word);
        }

    }
}
