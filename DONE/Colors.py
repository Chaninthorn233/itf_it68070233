"""docccccccccccccc"""
x = input()
y = input()
"""idkkkkkkkkkkkkkk"""
if (x == "Red" and y == "Yellow") or (x == "Yellow" and y == "Red"):
    print("Orange")
elif (x == "Red" and y == "Blue") or (x == "Blue" and y == "Red"):
    print("Violet")
elif (x == "Blue" and y == "Yellow") or (x == "Yellow" and y == "Blue"):
    print("Green")
elif (x == "Red" and y == "Red"):
    print("Red")
elif (x == "Blue" and y == "Blue"):
    print("Blue")
elif (x == "Yellow" and y == "Yellow"):
    print("Yellow")
else:
    print("Error")
