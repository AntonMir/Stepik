x = int(input())
h = int(input())
m = int(input())
print((((h * 60) + x) + m) // 60)
print(((x + (h * 60) + m) % 60))