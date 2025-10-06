"""BrickBridge"""
a = int(input())
b = int(input())
goal = int(input())
COUNT = 0

while b:
    goal = goal - 5
    b -= 1

while a:
    goal = goal - 1
    a -= 1
    COUNT += 1

if not goal:
    print(COUNT)

else:
    print("-1")
