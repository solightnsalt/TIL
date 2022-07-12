# 1부터 n까지의 곱을 구하여 출력하는 코드를 
# 1) while 문 2) for 문으로 각각 작성하시오.

# 1) while
# n = int(input())
# m = 1
# l = 1
# while l <= n:
#     m *= l:
#     l += 1
# print(m)

# 2) for
n = int(input())
m = 1
for l in range(1, n+1):
    m *= l
print(m)
