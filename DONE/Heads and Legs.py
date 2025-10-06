"""Heads and Legs"""
a = int(input())
b = int(input())

if (b - 2 * a) % 2:
    print("Impossible")
else:
    rabbit = (b - 2 * a) // 2
    bird = a - rabbit
    if bird < 0 or rabbit < 0:
        print("Impossible")
    else:
        print(rabbit, bird)
