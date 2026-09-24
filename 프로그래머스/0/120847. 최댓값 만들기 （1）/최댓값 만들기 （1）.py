def solution(numbers):
    answer = 0
    
    numbers.sort()  # 오름차순 정렬
    answer = numbers[-1] * numbers[-2]
    
    return answer

# numbers 원소 중 두 개를 곱해 만들 수 있는 최댓값 return