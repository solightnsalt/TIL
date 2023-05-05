# https://school.programmers.co.kr/learn/courses/30/lessons/120849
# def solution(my_string):
#     vowels = ['a', 'e', 'i', 'o', 'u']
#     answer = []
#     for i in my_string:
#         if i not in vowels:
#             answer.append(i)
#     return ''.join(answer)

def solution(my_string):
    return ''.join([i for i in my_string if not(i in "aeiou")])