class Solution {
    public String[] solution(String[] picture, int k) {
        StringBuilder answer = new StringBuilder();
        
        for (String row : picture){
            StringBuilder sb = new StringBuilder();
            for(char c : row.toCharArray()){
                for(int i = 0; i < k; i++){
                    sb.append(c);
                }
            }
            String expandedRow = sb.toString();
            for(int i = 0; i < k; i++){
                answer.append(expandedRow).append("\n");
            }
        }
        
        return answer.toString().split("\n");
    }
}