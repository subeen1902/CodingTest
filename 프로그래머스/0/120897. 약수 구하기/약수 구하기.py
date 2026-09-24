def solution(n):
    answer = []
    
    for i in range(1, n + 1):
        if n % i == 0:  # i가 n의 약수일 경우
            answer.append(i)
    
    return answer