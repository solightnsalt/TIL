a, b = input().split()
aa = bool(int(a))
bb = bool(int(b))
print((aa and (not bb)) or ((not aa) and bb))