def solution(angle):
    answer = 0
    
    if angle == 180:
        return 4
    elif angle > 90:
        return 3
    elif angle == 90:
        return 2
    else:
        return 1
    
    return answer


# 0 < angle < 90: 1
# angle = 90: 2
# 90 < angle < 180: 3
# angle = 180: 4