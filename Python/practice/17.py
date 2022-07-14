# 소문자로 구성된 문자열 word가 주어질 때, 모두 대문자로 바꾸어 표현하시오.
# .upper(), .swapcase() 사용 금지

word = 'banana'
tf = ''
for i in word:
    if 96 < ord(i) <123:
        tf1 = ord(i)
        # print(tf1)
        tf1 -= 32
        # print(tf1)
        tf += chr(tf1) # 여기서 왜 += ? 리스트 값을 합쳐야된다~ 
print(tf)