# 정수 number가 주어질 때, 각 자릿수의 합을 구해서 출력하세요. 
# 123, 6
n = int(input())
count = 0
for i in str(n):
    count += int(i)

print(count)

# 10으로 나눈 나머지를 더하면 된다 
n = 123 
# number가 0이면 STOP 
# 왜? Integer는 0이면 False니까 
result = 0
while number:
    # 몫은 다음 number
    # 나머지는 더하면 된다
    result += number%10
    number //= 10
print(result)


# divmod(X,Y)는 X를 Y로 나누고, 결과를 tuple로 반환.
#     number, remainder = divmod(number,10)
#     result += remainder
# print(result)