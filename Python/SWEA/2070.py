T = int(input())

import sys
sys.stdin = open("2070.txt", "r")

for test_case in range(1, T+1):
    a, b = map(int, input().split())
    if a > b:
        print('#%d' % test_case, '>')
    elif a < b:
        print('#%d' % test_case, '<')
    else:
        print('#%d' % test_case, '=')
