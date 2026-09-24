import math

def solution(n):
    return 1 if math.sqrt(n).is_integer() else 2

# math.sqrt(): 제곱근을 구할 경우 - import math 필요
# 제곱근 반환 값 - 정수인지 확인 필요