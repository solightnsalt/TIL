# https://www.acmicpc.net/problem/2839
n = int(input())

bag = 0
while n >= 0 : # 0보다 작으면 n - n//5가 3으로 나눠지지 않으므로 -1을 출력해야함
    if n % 5 == 0: # 3을 계속 빼주면서 n//5가 0이면 바로 종료
        bag += (n // 5)
        print(bag)
        break
    n -= 3
    bag += 1
else :
    print(-1)

