"""christmas"""
light = input()
num = int(input())
COUNT = 0 #[Red, Green, Blue]
for i in range(num):
    if COUNT == num:
        break
    if light == "R":
        print("Red", end=" ")
        COUNT += 1
        if COUNT == num:
            break
        print("Green", end=" ")
        COUNT += 1
        if COUNT == num:
            break
        print("Blue", end = " ")
        COUNT += 1+i-i
        if COUNT == num:
            break


    if light == "G":
        print("Green", end=" ")
        COUNT += 1
        if COUNT == num:
            break
        print("Blue", end=" ")
        COUNT += 1
        if COUNT == num:
            break
        print("Red", end = " ")
        COUNT += 1+i-i
        if COUNT == num:
            break


    if light == "B":
        print("Blue", end=" ")
        COUNT += 1
        if COUNT == num:
            break
        print("Red", end=" ")
        COUNT += 1
        if COUNT == num:
            break
        print("Green", end = " ")
        COUNT += 1+i-i
        if COUNT == num:
            break
