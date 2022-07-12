# 문자열 word의 길이를 출력하는 코드를 각각 작성하시오.
# len() 함수를 바로 쓰기보다는 반복문을 활용하세요.
# input > word = 'happy!'

#len()
#word = input()
#print(len(word))

# cnt = 0
# while(word!=""):
#    cnt+=1
#    word = word[1:]
#print(cnt)

word = input()
length = 0
for i in word:
    length += 1
print(length)

# 풀이 
# 하나하나씩 카운트 
word = 'happy!'
count = 0
for char in word:
# 1씩 증가시킨다. 
    count = count + 1 
print(count)

