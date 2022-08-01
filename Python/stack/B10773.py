# https://www.acmicpc.net/problem/10773

import sys
sys.stdin = open('B10773.txt')

T = int(input())
list = []
for tc in range(1, T+1):
    a = int(input())
    if a != 0:
        list.append(a)
    else:
        list.pop()
    
print(sum(list))