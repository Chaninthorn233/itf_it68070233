"""TopTestScore"""
students = int(input())
NEWSCORE = 0
COUNT = 0
for i in range(students):
    score = int(input())
    if score >= NEWSCORE:
        if score == NEWSCORE:
            NEWSCORE = score
            COUNT += 1
        if score > NEWSCORE:
            NEWSCORE = score
            COUNT = 1+i-i

print(NEWSCORE)
print(COUNT)
