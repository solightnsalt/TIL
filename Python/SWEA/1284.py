# w = 종민이 쓴 물 
# a_rate = w * p 
# b_rate 
# if w > r:
#     q + (w-q)*s 
#  if a > b:
#      print(b)
#  else: 
#      print(a)   

import sys
sys.stdin = open("1284.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    P, Q, R, S, W = map(int, input().split())
    # print(P, Q, R, S, W)
    a = W * P
    b = Q if W <= R else ((W - R) * S) + Q
    # print(a, b)

    if a > b:
        print(f'#{test_case} {b}')
    else:
        print(f'#{test_case} {a}')