class Solution {
    public double solution(int[] numbers) {
        double answer = 0;
        double sum = 0;
        
        // numbers 배열 순회하며 sum 변수에 총합
        for(int i = 0; i < numbers.length; i++){
            sum += numbers[i];
        }
        
        // numbers 배열의 숫자가 합해진 answer 변수를 numbers 배열 길이로 나누기(평균값 구하기)
        answer = sum / numbers.length;
        return answer;
    }
}
