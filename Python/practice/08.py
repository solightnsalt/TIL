# 주어진 리스트 numbers에서 두번째로 큰 수를 구하여 출력하시오.
# max() 함수 사용 금지

numbers = [0, 20, 100, 50, -60, 50, 100]
m = numbers[0]
s = numbers[0]
for n in range(1, len(numbers)):
    if n > numbers[0]:
       s = numbers[0]
       m = n
    # elif s < n < m: 어떤 언어는 이거 지원 안해줌 
    elif s < n and n < m:
         s = n
print(s)



# 1. 전체 숫자 반복 
for n in numbers:
   # 만약에 n 이 최대보다 크면 
   if m < n:
      # 최대값이었던 것을 s 주기 
      s = m 
      m = n
print(s)
# 하면 안됨 ㅎ

