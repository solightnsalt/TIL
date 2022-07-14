# 문자열 word가 주어질 때, 해당 문자열에서 a 의 모든 위치(index)를 출력해주세요.
# find() index() 메서드 사용 금지

word = 'HappyHacking'
for i in range(len(word)):
    if word[i] == 'a':
        print(i, end=' ')

# result라는 빈 리스트를 만들어놓고 
# for 로 도는 동안 word 가 a 이면 
# 빈 리스트에 하나씩 집어넣는 방법

#또는 그때그때 출력하는 방법