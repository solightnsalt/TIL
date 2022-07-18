# word = "HappyHacking"

# count = 0

# for char in word:
#     if char == "a" or "e" or "i" or "o" or "u":
#         count += 1

# print(count)

word = "HappyHacking"

vowels = ['a', 'e', 'i', 'o', 'u']
count = 0

for char in word:
    if char in vowels:
        count += 1

print(count)

# if char == "a" or "e" or "i" or "o" or "u"
# 는 char이랑 a랑 같거나, e i o u 거나