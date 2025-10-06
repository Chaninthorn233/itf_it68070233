"""DIVIDE"""
n = int(input())
ALL = 0
for i in range (n + 1):
    if not i % 3 or not i % 5:
        ALL += i
print(ALL)
