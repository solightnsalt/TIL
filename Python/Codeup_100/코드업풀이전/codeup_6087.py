n = int(input())
num = 0
while True:
    num += 1
    if num > n:
        break
    elif num % 3 == 0:
            continue
    else:
        print(num)