# https://www.acmicpc.net/problem/1110

n = int(input())
cnt = 0
og_n = n 
# n이 계속 바껴야되기 때문에 새변수에 n 저장해놓고 와일문으로 엔 계속 바뀌게 하는거
# 첨에 new_n 이렇게 하다가 무한루프 오지게 남

while True:
    cnt += 1
    sum_ = n // 10 + n % 10
    # print(sum_)
    # break
    n = n % 10 * 10 + sum_ % 10
    # print(n, new_n)
    # break
    if og_n == n:
        break

print(cnt) 
       