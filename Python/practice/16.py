# 문자열 word가 주어질 때, 해당 문자열에서 모음의 갯수를 출력하시오.
# 모음 : a, e, i, o, u 
# count() 사용 금지

word = 'apple'
cnt = 0
vowels = ['a', 'e', 'i', 'o', 'u']
for i in word:
    if i in vowels:
        cnt = cnt + 1
print(cnt)

# 만약에 모음리스트 따로 안만들고 
# if문에 i == 'a' or 'e' 이런식으로 쓰면 
# i는 a와 같거나 e와 같은게 아니라 
# i는 a 와 같거나, 그냥 e 일때 
# 따로 안묶고 if i == 'aeiou'