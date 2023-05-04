# https://school.programmers.co.kr/learn/courses/30/lessons/120909
# def solution(n):
#     answer = 2
#     square = 0
#     num = 1
#     while True:
#         square = num * num
#         if square == n:  
#             answer = 1
#             break 
#         else:
#             num += 1
#     return answer

# 정수일 경우 1로 나누면 나머지가 0 
# 따라서 (n ** 0.5) % 1 == 0 과 (n ** 0.5).is_integer() 는 같다

def solution(n):
    return 1 if (n ** 0.5) % 1 == 0 else 2