# 주어진 리스트 numbers에서 최대값을 구하여 출력하시오.
# max() 함수 사용 금지

numbers = [0, 20, 100]
m = numbers[0] # 우선 초기값을 임의로 넘버스 첫번째껄로 해놓자!!! for 로 훑고 바꾸면 되니까 
for i in range(1, len(numbers)): # ? 굳이 이렇게 할 필요 없나 ?,,,,
    if m < numbers[i]:
        m = numbers[i]
print(m)

# 3살짜리 컴터한테 알려준다고 생각하기 

# 문제 딱 보면 for문으로 전체 다 돌거야 (반복)
# 최대값 뭐라고 하지? 맥스의 m 
# 비교 > m이 n보다 작을때 
# 어케 ? m이랑 n이랑 바꿔 

# 오 출력해보고 뭔가 틀렸다 ?
# 그럼 중간에 프린트 넣어서 아랫값 나오는지 확인하기 


numbers = [-10, -100, -30]
# max_num = float("-inf") ??????
m = numbers[0]
# 1. 반복
for n in numbers:
    # 만약 m이 n보다 작으면 바꾼다. 
    if m < n:
        m = n
print(m)
