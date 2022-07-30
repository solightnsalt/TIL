# https://www.acmicpc.net/problem/10871
import sys
sys.stdin = open('10871.txt')

n, x = map(int, input().split())
a = list(map(int, input().split()))
smaller = []
for i in a:
    if i < x:
        smaller.append(i)
        
print(*smaller)