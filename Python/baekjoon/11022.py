# 두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램을 작성하시오.
# 첫째 줄에 테스트 케이스의 개수 T가 주어진다.
# input: 각 테스트 케이스는 한 줄로 이루어져 있으며, 각 줄에 A와 B가 주어진다. (0 < A, B < 10)
# output: 각 테스트 케이스마다 "Case #x: A + B = C" 형식으로 출력한다. x는 테스트 케이스 번호이고 1부터 시작하며, C는 A+B이다.

import sys
sys.stdin = open('11022.txt', 'r')

T = int(input())
for test_case in range(1, T+1):
    a, b = input().split()
    c = int(a) + int(b)
    print(f'Case #{test_case}:', int(a), '+', int(b), '=', c)