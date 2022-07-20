# 1부터 N까지의 숫자에서 홀수는 더하고 짝수는 뺐을 때 최종 누적된 값을 구해보자. ?

import sys
sys.stdin = open("1986.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    n = int(input())
    result = 0
    for i in range(1, n +1):
        if not i % 2: # i % 2 2로 나눠서 나머지 있으면 홀 / 아님 짝 
            result -= i
        else:
            result += i

    print(f'#{test_case} {result}')