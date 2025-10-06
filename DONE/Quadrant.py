"""Quadrant"""
x = int(input())
y = int(input())

if not x and not y:
    print("O")
elif not x:
    print("Y")
elif not y:
    print("X")
elif x > 0 < y:
    print("Q1")
elif x < 0 < y:
    print("Q2")
elif x < 0 > y:
    print("Q3")
elif x > 0 > y:
    print("Q4")
