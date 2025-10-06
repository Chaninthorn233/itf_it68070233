"""999"""
n = int(input())
code1 = input()
code2 = input()

COUNT = 0
i = 0

for i in range(n):
    if int(code1[i]) + int(code2[i]) != 9:
        COUNT += 1

if not COUNT:
    print("YES")
else:
    print("NO", COUNT)
