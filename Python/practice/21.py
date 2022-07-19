# 주어진 숫자를 뒤집은 결과를 출력하시오. 
# * 문자열이 아닌 숫자로 활용해서 풀어주세요. str() 사용 금지 str(number)[::-1]하면 깔끔
# 1234 4321

n = 123456789
rev_n = 0 # 
while n > 0:
    a = n % 10
    rev_n = (rev_n * 10) + a
    n = n // 10
print(format(rev_n))