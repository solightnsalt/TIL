# 문자열 word가 주어질 때, 
# Dictionary를 활용해서 해당 문자열에서 등장한 모든 알파벳 개수를 구해서 출력하세요.

word = 'banana'
dict = {}   # 빈 딕셔너리 하나 만들어준다
for i in word: # 딕셔너리에 키가 없으면 ?
    dict[i] = 0 
    # 딕셔너리에 키를 넣고 값을 0으로 초기화한다.
for i in word:
    dict[i] += 1
for k, v in dict.items():
    print(k, v)


# for key in result:
#     print(key, result[key])
    