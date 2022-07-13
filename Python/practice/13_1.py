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

# 3번으로 풀수록 알고리즘에 강해진다.
# end는 print 기본값에 있음 \n 개행 
# 아~~~~  
