import sys
sys.stdin = open("1976.txt", "r")

T = int(input())
for tc in range(1, T + 1) :
    h1, m1, h2, m2 = map(int,input().split())
    f_hour = 0
    f_min = 0
    # print(h1, h2, m1, m2)
    hour = h1 + h2
    min = m1 + m2
    # print(hour, min, type(hour), type(min))
    if min >= 60 :
        f_min = min - 60
        f_hour = hour + 1
    else :
        f_min = min
        
        print(f_hour, f_min)
    #         f_hour = hour - 12
    #     else:
    #         f_hour = hour
            
    # print(f'#{tc} {f_hour} {f_min}')
        