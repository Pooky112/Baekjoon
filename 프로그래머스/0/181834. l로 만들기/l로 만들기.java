class Solution {
    public String solution(String myString) {
        return myString.replaceAll("[^l-z]", "l");
        // String answer = "";
        // for(char c : myString.toCharArray()){
        //     if (c < 'l'){
        //         answer += 'l';
        //     } else{
        //         answer += c;
        //     }
        // }
        // return answer;
    }
}