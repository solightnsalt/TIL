w, h, b = map(int, input().split())
mb = (w * h * b)/8/1024/1024
print(f'{mb:.2f} MB')