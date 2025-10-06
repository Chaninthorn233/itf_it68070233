"""align"""
size = int(input())
direc = input()
text = input()

LONG = len(text)

if direc == "left":
    while LONG < size:
        text = text + " "
        LONG = len(text)

if direc == "right":
    while LONG < size:
        text = " " + text
        LONG = len(text)

if direc == "center":
    while LONG < size:
        text = " " + text + " "
        LONG = len(text)
print(text)
