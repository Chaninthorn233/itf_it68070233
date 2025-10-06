"""grocery"""
a, b, c = map(int, input().split())
COST = 0
COST += a * 10
COST += b * 25
COST += c * 3

print(COST)
