import sys
sys.stdin = open("1288.txt", "r")

T = int(input())
for test_case in range(1, T + 1) :
#    1)
#     n = int(input())
#     # 0~9 들어갈 자리
#     # [0] * 10 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
#     numbers = [0] * 10
#     # 곱할 수 1~
#     i = 1
#     while 0 in numbers : 
#         num = str(n * 1)
#         for j in range(len(num)):
#             numbers[int(num[j])] += 1
#             i += 1
                        
#     print(f'#{tc} {num}')


# 2)    
#     N = int(input())
#     check = set()
#     M = 1 # 배수
    
#     while len(check) < 10:
#         num = M * N
        
#         while num:
#             check.add(num % 10)
#             num //= 10
#             M += 1
    
#     print(f'#{test_case} {(M - 1) * N}')
    
#     민석이 sheep색기

# n + n 
# n + n + n 
# 계속 했을 때 0~9 다 나오면 
# 마지막 출력값 
# 1) 반복 언제까지 ? 모든 수에 체크 될 때까지 
# 2) 특정 조건이 있기때문에 while문
# 3) 모든 수 체크를 어케 ? 
#   1) 리스트에 0이 없을때까지 
#      0~9 숫자지만 뭘로 보면 쉽다? 인덱스 i[0]에 +하는식으로
#   2) 중복제거 > set 길이가 10이 될 때까지 ?????
#       ( 파이써닉한 방법, 일반적으로는 1 방법)

#풀이 

#input 가져오기 
    n = int(input())
    n1 = n
    #set에 계속 추가
    numbers = set()
    #while 반복 > set 길이가 10이 될 때까지 
    while len(numbers) < 10:
        # for 반복 : 숫자를 문자로 
        for N in str(n):
            # numbers set에 추가 
            numbers.add(N)
        if len(numbers) == 10:
            break
            n =+ n1
        # 내가 확실하게 아는 결과랑 출력문 비교해보기
            print(f'#{test_case} {n}')
            