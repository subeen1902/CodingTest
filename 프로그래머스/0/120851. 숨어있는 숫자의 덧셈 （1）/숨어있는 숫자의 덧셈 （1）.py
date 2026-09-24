def solution(my_string):
    
    return sum(int(i) 
              for i in my_string
              if i.isdigit())

# 모든 자연수들의 합 return
# isdigit(): 문자열이 숫자로 구성 되어있는지 True/False로 반환