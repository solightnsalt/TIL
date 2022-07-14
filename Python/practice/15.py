# 문자열 word가 주어질 때, 
# 해당 문자열에서 a 가 처음으로 등장하는 위치(index)를 출력해주세요.
# a 가 없는 경우에는 -1을 출력해주세요.
# find() index() 메서드 사용 금지

word = 'apple'
# i를 문자로 접근하는게 아니라 인덱스로 접근하자 
# 원하는 숫자 = 01234 
# len(word) = 6이고 이걸 range로 범위화 시키면 0~5
for i in range(len(word)): # i는 보통 index
    # print(i, word[idx])
    if word[i] == 'a':
         print(1)
         break
   # else:
        # i = -1 안해도 됨
        # for문을 다 돌았다는거는 a가 없다는 말
        #  걍 바로 프린트
else:
# 또는 if not is_a:    
    print(-1)        
# print(i) 여기 안쓰고 걍 if 밑에 바로 넣어버리면 됨

# banana 를 for 문으로 하나씩 돌건데 
# 첫번째 자리 falst
# 두번째 자리 true 
# 어 ? 트루 나왔네? 그럼 더 안해도 돼 중지 



