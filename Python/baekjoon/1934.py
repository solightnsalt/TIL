import sys
sys.stdin = open('1934.txt')

t = int(input())
for tc in range(t):
    a, b = map(int, input().split())
    aa, bb = b, a
    while bb != 0:
        aa = aa % bb
        aa, bb = bb, aa
    
    print(a*b//aa)       


# t = int(input())
# for tc in range(t):
#     a, b = map(int, input().split())
#     n = 2
#     list_ = [1] 
#     while True:
#         if (a % n != 0) or (b % n != 0):
#             aa = a // (n-1)
#             bb = b // (n-1)
#             list_.append(aa)
#             list_.append(bb)
#             break
#         elif (a % n == 0) and (b % n == 0):
#             list_.append(n)
#             n += 1
#             continue
#     if a % b == 0 or b % a == 0:
#         print(max(a, b))
#     else: 
#         result = list_[0]
#         for i in list_:
#             result = result * i
#         print(result)        
# 반례 22 33