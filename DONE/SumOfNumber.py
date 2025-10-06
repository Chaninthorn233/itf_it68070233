"""Sum Of Number"""
want = int(input())
SUM = 0
while SUM != want:
    num = int(input())
    if num == -1:
        break
    SUM += num

print(SUM)
