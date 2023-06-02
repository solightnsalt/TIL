# https://www.acmicpc.net/problem/10250
import sys
sys.stdin = open('10250.txt')

t = int(input())
for _ in (0:t+1):
    h, w, n = map(int, input().split())
    y = n % h 
    x = n // h + 1  
    if n % h == 0:
        y = h 
        x = n // h
    print(str(y*100 + x))