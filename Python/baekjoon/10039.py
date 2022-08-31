# input_ = [10, 65, 100, 30, 95]
scores = []
for i in range(5):
    i = int(input())
    # i = input_[i]
    if i < 40:
        scores.append(40)
    else:
        scores.append(i)

print(sum(scores) // 5)
        
