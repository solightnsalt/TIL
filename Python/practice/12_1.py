# while? for? 하나를 끝까지 
# 만약에 글자가 a라면 안해 

word = 'apple'
# 반복 for
for alph in word:
    # 만약 a 일 때 
    if alph != 'a': # != 같지 않다 연산자
        # 여기서 print로 작동하는지 확인해줘봐도 ㅇㅋ
        # 반복문에서 아무것도 안하고 넘어가는거는? 
        # continue 써도되고 
        result = result + alph
print(result)

# 이렇게 쉬운거였다고?......

