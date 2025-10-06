"""Heron of Alexandria"""
import math

a = float(input())
b = float(input())
c = float(input())
s = (a+b+c)/2
AREA = 0

if (s-a) and (s-b) and (s-c):
    AREA = math.sqrt(s*(s-a) * (s-b) * (s-c))
print(f"{AREA:.3f}")
