"""Sqeuence I"""
m = int(input())
n = int(input())
NUM = 0

if m != 1 and n != 1:
    while NUM != m - 1:
        NUM += 1
        print(NUM, end=" ")

    NUM += 1
    print(NUM)

    while NUM != (n * m) - 1:
        NUM += 1
        print(NUM, end=" ")

    NUM += 1
    print(NUM)

elif m == 1 and n != 1:
    while NUM != (n - 1):
        NUM += 1
        print(NUM, end=" ")

    NUM += 1 
    print(NUM)

elif m != 1 and n == 1:
    while NUM != (m - 1):
        NUM += 1
        print(NUM)

elif m == 1 and n == 1:
    print("1")
