# 2단부터 9단까지 반복하여 구구단을 출력하세요.
# * 문자열 출력시 f-string을 활용하면 편하게 작성할 수 있습니다.
# f-string 
# n = 2
# w = f'{n}단 입니다'
# print(w)


for a in range(2, 10):
    b = f'{a}단'
    print(b)
    for c in range(1, 10):
        print(a, 'X', c, '=', a*c)


