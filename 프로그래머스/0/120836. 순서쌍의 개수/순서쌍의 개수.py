def solution(n):
    answer = 0
    
    for i in range(1, n + 1):
        if n % i == 0:  # 중앙값까지만 반복하도록
           answer += 1 
    
    return answer

# 순서쌍: 두 개의 숫자를 순서를 정하여 짝지어 나타낸 쌍 => (a, b)
# n의 개수 return