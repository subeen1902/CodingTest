def solution(price):
    if price >= 500000:
        answer = price * 0.8
    elif price >= 300000:
        answer = price * 0.9
    elif price >= 100000:
        answer = price * 0.95
    else:
        answer = price
    return int(answer)

# 10만원 이상 5% / 30만원 이상 10% / 50만원 이상 20%