class Solution {
    public int[] solution(int money) {
        int[] answer = new int[2];  // 배열 
        
        if(money < 5500){
            answer[0] = 0;
            answer[1] = money;
        } else {
            answer[0] = money / 5500;  // 개수
            answer[1] = money % 5500;  // 가격
        }
        
        return answer;
    }
}

// 배열 answer: answer[0] = 최대로 마실 수 있는 아메리카노의 잔 수, answer[1] = 남은 돈
// money: 돈
// 아이스 아메리카노 한 잔: 5,500원