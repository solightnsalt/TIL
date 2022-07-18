# numbers = input().split()
# print(sum(numbers))

numbers = input().split()
print(sum(map(int,numbers)))

# numbers ['10', '20'] 리스트 안의 요소가 str이라 int로 바꿔줘야됨