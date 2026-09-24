def solution(n, k):
    answer = 0
    
    if n >= 0:
        return 12000 * n + 2000 * k - 2000 * (n // 10)
    else:
        return 12000 * n + 2000 * k
    
    return answer


# 1인분 12,000원 / 음료수 2,000원 - 10인분 + 음료수 1개(서비스)
# 양꼬치 * n명 + 음료수 * k개 - 음료수 * (n // 10)