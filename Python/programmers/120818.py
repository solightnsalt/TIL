# https://school.programmers.co.kr/learn/courses/30/lessons/120818?language=python3

# def solution(price):
#     if price >= 500000:
#         price = price * 0.8
#     elif price >= 300000:
#         price = price * 0.9
#     elif price >= 100000:
#         price = price * 0.95
#     return int(price)

# for k, v in 튜플.items()
# for문이 도는 동안 튜플의 키와 값을 각각 얻을 수 있음

def solution(price):
    discount_rates = {500000: 0.8, 300000: 0.9, 100000: 0.95, 0: 1}
    for discount_price, discount_rate in discount_rates.items():
        if price >= discount_price:
            return int(price * discount_rate)
        
        