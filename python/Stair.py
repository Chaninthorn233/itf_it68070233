"""doc"""
y = int(input())
n = int(input())
STEP = 0
COUNT = 0
HERE = 0
while HERE < n+2:
    STEP = int(input())
    if STEP <= y:
        COUNT += 1
        HERE += y
    elif STEP > y:
        COUNT += 1
        HERE += 1

if COUNT:
    print(COUNT)

else:
    print("NO")
