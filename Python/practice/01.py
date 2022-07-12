# 주어진 수 n이 3의 배수이면서 
# 짝수인 경우 ‘참’을 거짓인 경우 ‘거짓'을 출력하시오.
num = int(input())
if num %3 == 0 and num &2 == 0:
    print('참')
else:
    print('거짓')