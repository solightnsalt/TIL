import random
n = int(input('얼마치 살 거야: '))
for i in range(n):

# 1~45까지의 숫자, 그 중 6개
    numbers = random.sample(range(1,46), 6)
# 순서대로 보고싶다 ? 
    numbers.sort()
    print(numbers)


# import random

# def generate_lotto(n):
#         result = []
#         for i in range(n):
#         numbers = range(1, 46)
#         pick = random.sample(numbers, 6)
#         result.sort()
#         return result
# print(generate_lotto(5), sep = '/n')