def solution(dot):
    answer = 0
    x, y = dot[0], dot[1]
    
    if x > 0 and y > 0:
        return 1
    elif x < 0 and y > 0:
        return 2
    elif x < 0 and y < 0:
        return 3
    else:
        return 4
    
    return answer

# dot[0] = x / dot[1] = y
# 1: dot[양수, 양수] / 2: dot[음수, 양수] / 3: dot[음수, 음수] / 4: dot[양수, 음수]