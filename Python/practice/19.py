n = 123   
counts = 0
while n: # 종료조건까지 반복 => 몫이 0 왜 ? 
    n //= 10
    counts += 1
print(counts)

# print(len(str(number)))

# 123 == 100 + 20 + 3
# 123 == 1 * 100 + 2 * 10 + 3 * 1
# 123/10 
number = 123
import math
print(int(math.log(number,10))+1)