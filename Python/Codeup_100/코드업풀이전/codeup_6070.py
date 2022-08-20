month = int(input())
season = {
    'spring' : [3, 4, 5],
    'summer' : [6, 7, 8],
    'fall' : [9, 10, 11],
    'winter' : [12, 1, 2]
}
for k, v in season.items():
    if month in v:
        print(k)
        break
    