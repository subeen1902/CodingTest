def solution(sides):
    sides.sort()
    
    if sides[2] < sides[0] + sides[1]:
        return 1
    else:
        return 2

# sides: 삼각형 세 변의 길이
# 가장 긴 변의 길이 < 다른 두 변의 길이의 합