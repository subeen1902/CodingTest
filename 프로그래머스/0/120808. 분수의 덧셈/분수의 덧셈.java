class Solution {
    public int[] solution(int numer1, int denom1, int numer2, int denom2) {
        int denom = denom1 * denom2;  // 새 분모
        int num = numer1 * denom2 + numer2 * denom1;  // 새 분자
        int gcd = getGCD(num, denom);  // 최대공약수
        
        int[] answer = {num / gcd, denom / gcd};
        return answer;
    }
    private int getGCD(int a, int b) {
        while (b != 0) {
            int temp = a % b;
            a = b;
            b = temp;
        }
        return a;
    }
}