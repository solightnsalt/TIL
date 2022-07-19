T = int(input())

import sys
sys.stdin = open("2071.txt", "r")

for test_case in range(0, T):
    nums = list(map(int, input().split()))
    print("#%d %d" % (test_case+1, round(sum(nums)/10)))