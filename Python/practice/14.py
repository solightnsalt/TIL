# 문자열 word가 주어질 때, 해당 문자열에서 a 개수를 구하세요.
# count() 메서드 사용 금지

word = 'banana'
char = 0
for i in word: 
    # word의 요소를 하나씩 꺼낼건데 그걸 i라고 부르자!
    if i == 'a': # 그 요소가 a 일때마다 +1
        char = char + 1   
        # char += 1 
print(char)

# 09 문제랑 같은 개념 
# 어떤 것을 첨부터 끝까지 한번씩 다 본다 ~ = for 

