"""calculator"""
n = int(input())
COUNT = 0

for i in range(1, n + 1):
    COUNT += len(str(i))

if n == 1:
    print(COUNT)
else:
    print(COUNT + (n - 1) + 1)
