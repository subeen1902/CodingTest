class Solution {
    public int solution(int slice, int n) {
        int answer = 0;
        
        while(n >= 1){
            answer += 1;
            n = n - slice;
        }
        
        return answer;
    }
}

// slice: 피자 조각 수
// n: 피자 먹는 사람 수
// answer: 시켜야 하는 최소한 피자의 판(n명의 사람이 한 조각 이상 피자 먹음)