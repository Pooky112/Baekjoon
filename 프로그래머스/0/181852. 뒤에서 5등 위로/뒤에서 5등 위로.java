import java.util.Arrays;

class Solution {
    public int[] solution(int[] num_list) {
        Arrays.sort(num_list);
        int[] result = new int[num_list.length - 5];
        for (int i = 0; i < result.length; i++){
            result[i] = num_list[5 + i];
        }
        return result;
    }
}