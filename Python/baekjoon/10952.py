# https://www.acmicpc.net/problem/10952
import sys
sys.stdin = open('10952.txt')


while True:
    a, b = map(int, input().split())
    if a == 0 and b == 0:
        break
    else:
        print(a + b)