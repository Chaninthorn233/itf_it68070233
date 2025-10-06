"""Squid game"""
A = 0
B = 0

for i in range(20):
    force = int(input())
    if i < 10:
        A += force
    else:
        B += force

if A > B:
    print("B")
elif B > A:
    print("A")
else:
    print("AB")
