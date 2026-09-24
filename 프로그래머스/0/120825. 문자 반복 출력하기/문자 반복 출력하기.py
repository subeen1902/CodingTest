def solution(my_string, n):
    answer = ''  # 문자열 선언
    
    for i in my_string:
        answer += i * n
        
    return answer