import sys
sys.stdin = open('14425.txt')

N = int(input())
S = []
word_set = set(S)
for word in words:
    if word in set(S):
        cnt += 1
print(cnt)







for i in range(1, N+1):
    S.append(input())
    print(S)

# oneliner code . but 시간복잡도는 ?.. 
# print(len(set(words)) & set(S))

# set 안 쓸 때 
# cnt = 0 
# for word in words:
#     if word in S:
#         cnt += 1
# print(cnt)