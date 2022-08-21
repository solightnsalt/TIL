n = int(input())
for i in range(1, n + 1):
    if str(i)[-1] in ['3', '6', '9']:
        print('X', end=' ')
    else:
        print(i, end=' ')