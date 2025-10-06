"""OverlapCircle"""
x1 = int(input())
y1 = int(input())
r1 = int(input())
x2 = int(input())
y2 = int(input())
r2 = int(input())
lo = r1 + r2
x = (((x2 - x1) ** 2) + ((y2 - y1) ** 2)) ** 0.5
if float(lo) > float(x):
    print("overlapping")
else:
    print("no overlapping")
