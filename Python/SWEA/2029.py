T = int(input())

# import sys
# sys.stdin = open("2029.txt", "r")

for test_case in range(1, T + 1):
    a, b = map(int, input().split())
    # print(a, b)
    print('#%d' % test_case, a // b, a % b)