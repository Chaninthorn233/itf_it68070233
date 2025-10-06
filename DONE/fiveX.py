"""five"""
num = int(input())
COUNT = 1
for i in range(num):
    if not COUNT % 5:
        print("X", end="")
    else:
        print("*", end="")
    COUNT += 1+i-i
