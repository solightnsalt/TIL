h, m, s = map(int, input().split())
t = int(input())

sec = s + (t % 60)
secs = sec % 60

min = m + (t // 60) + (sec // 60)
mins = min % 60

hour = h + (min // 60)
hours = hour % 24
print(hours, mins, secs)

# h, m, s = map(int, input().split())
# t = int(input())
# s += t % 60
# m += t // 60

# sec = s % 60
# min = (m + ( s // 60))
# mins = min % 60
# hour = h + (min // 60)
# if hour > 23:
#     print(abs(hour - 24), mins, sec)
# else:
#     print(hour, mins, sec)

