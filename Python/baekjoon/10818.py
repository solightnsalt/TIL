# https://www.acmicpc.net/problem/10818
import sys
sys.stdin = open('10818.txt')

n = int(input())
n_list = list(map(int, input().split()))

print(min(n_list), max(n_list))
