import sys
sys.stdin = open('2480.txt')

a, b, c = map(int, input().split())

if a == b == c: 
    print(10000 + a * 1000)
    