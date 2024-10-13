import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Collections;

public class Main {
    public static void main(String[] args) throws IOException {
//        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
//        StringBuilder sb = new StringBuilder();
//
//        int N = Integer.parseInt(br.readLine());
//
//        ArrayList<Integer> list = new ArrayList<>();
//
//        for (int i = 0; i < N; i++) {
//            list.add(Integer.parseInt(br.readLine()));
//        }
//
//        Collections.sort(list);
//
//        for(int num : list){
//            sb.append(num).append('\n');
//        }
//        System.out.println(sb);
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();

        int N = Integer.parseInt(br.readLine());
        int[] cnt = new int[10001];

        for(int i = 0; i < N; i++){
            cnt[Integer.parseInt(br.readLine())]++;
        }
        
        for(int i = 1; i < 10001; i++){
            while(cnt[i] > 0){
                sb.append(i).append('\n');
                cnt[i]--;
            }
        }
        System.out.println(sb);

    }
}
