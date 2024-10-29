import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Collections;

public class Main {
    static Integer searchHeight(int N, int M, int maxTreeHeight, int[] trees){
        int low = 0;
        int high = maxTreeHeight;
        //ArrayList<Integer> result = new ArrayList<Integer>();
        int result = 0;
        while (low <= high){
            int mid = (low + high) / 2;
            long targetWood = 0;

            for(int height: trees){
                if (height > mid){
                    targetWood += (height - mid);
                }
            }
            if (targetWood < M){
                high = mid - 1;
            } else{
                result = mid;
                low = mid + 1;
            }
        }

        return result;
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] firstLine = br.readLine().split(" ");
        int N = Integer.parseInt(firstLine[0]);
        int M = Integer.parseInt(firstLine[1]);

        String[] secondLine = br.readLine().split(" ");
        int[] trees = new int[N];

        int maxTreeHeight = 0;
        for(int i = 0; i < N; i++) {
            trees[i] = Integer.parseInt(secondLine[i]);
            if (trees[i] > maxTreeHeight) {
                maxTreeHeight = trees[i];
            }
        }
        int result = searchHeight(N, M, maxTreeHeight, trees);
        System.out.println(result);
    }
}
