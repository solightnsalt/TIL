import sys
sys.stdin = open("1989.txt", "r")

T = int(input())
for tc in range(1, T + 1) :
    word = input() 
    # 일단 뒤집어보기 
    r_word = word[::-1]
    if word == r_word:
        print(f'#{tc} {1}')
    else:
        print(f'#{tc} {0}')    
    
    
