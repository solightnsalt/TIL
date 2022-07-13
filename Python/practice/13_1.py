word = 'apple'
result = ''
for alph in word:
    result = alph + result
print(result)

# 2. pythonic
# print(word[::-1]) 인덱스를 뒤집는 
# ::-1 처음부터 끝까지 뒤에서 읽는다 
# print(''.join(reserved(word)))

# 3. index
world = 'apple'
for i in range(len(word)):
    print(word[len(word)-i-1],end='')
    
