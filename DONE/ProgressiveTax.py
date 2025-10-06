"""ProgressiveTax"""
n = int(input())
LEFT = int()
TAX = 0

if n > 4000000:
    LEFT = n - 4000000
    TAX += LEFT * 0.35
    TAX += 965000

if 2000000 < n <= 4000000:
    LEFT = n - 2000000
    TAX += LEFT * 0.30
    TAX += 365000

if 1000000 < n <= 2000000:
    LEFT = n - 1000000
    TAX += LEFT * 0.25
    TAX += 115000

if 750000 < n <= 1000000:
    LEFT = n - 750000
    TAX += LEFT * 0.2
    TAX += 65000

if 500000 < n <= 750000:
    LEFT = n - 500000
    TAX += LEFT * 0.15
    TAX += 27500

if 300000 < n <= 500000:
    LEFT = n - 300000
    TAX += LEFT * 0.1
    TAX += 7500

if 150000 < n <= 300000:
    LEFT = n - 150000
    TAX += LEFT * 0.05

print(int(TAX))
