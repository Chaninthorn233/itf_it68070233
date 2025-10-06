"""One For All"""

def main(num):
    """function"""
    text = ""
    for i in range(num):
        ofa = input()
        if not i:
            text = ofa
        elif i % 2:
            text = text + ("*"*i) + ofa
        elif not i % 2:
            text = text + ("-"*i)+ ofa
    num = str(num)
    print(text + "_"+num)

main(int(input()))
