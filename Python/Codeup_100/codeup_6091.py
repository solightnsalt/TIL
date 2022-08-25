# import math
a, b, c = map(int, input().split())
# print(math.lcm(a, b, c))
day = 1
while day % a != 0 or day % b != 0 or day % c != 0:
    day += 1
print(day)