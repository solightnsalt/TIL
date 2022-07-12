# 주어진 숫자의 평균을 구하는 코드를 작성하시오.
# sum(), len()  함수 사용 금지

# 1. 문제제공 
numbers = [3, 10, 20]

# 2. 값 초기화
i = 0
total = 0

# 반복
for num in numbers: # 넘버스에서 하나씩 꺼낼거야 
    total += num 
    i += 1
print(int(total/i))

# 풀이
# 임의변수0 정해놓고 거기서부터 리스트 첫번째 기록하고 더하고, 두번째 기록하고 더하고 이런 너낌

# 쉬운버전
print(sum(numbers)/len(numbers))
