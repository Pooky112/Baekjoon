class Solution {
    public int solution(int a, int b) {
        int plus = Integer.parseInt(""+ a + b);
        return (plus >= 2 * a * b) ? plus : 2 * a * b;
    }
}