"""countvo"""
n = int(input())
COUNT = 0
VOWEL = "AEIOU"

for i in range(n):
    char = input().strip()
    if char in VOWEL:
        COUNT += 1 +i-i

print(COUNT)
