
from asyncio import exceptions


n = input()
try:
    print(100/int(n))

except ValueError:
    print('숫자 써')

except ZeroDivisionError:
    print('응 0으로 나누기 안돼')

except exceptions:
    print('오류')

else:

finally:
    print('완료')