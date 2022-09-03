n = 1
dn = 0
dn_list = []
while dn <= 10000:
    sn = str(n)
    dn = n
    for i in sn:
        dn += int(i)
    dn_list.append(dn)
    n += 1
# print(dn_list)
dnlist = sorted(set(dn_list))
for i in range(1, 10001):
    if i not in dnlist:
        print(i)
