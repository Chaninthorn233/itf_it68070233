"""Donut"""

def main():
    """main"""
    a = int(input())
    b = int(input())
    c = int(input())
    d = int(input())
    TOTAL = 0
    PRICE = 0
    
    while TOTAL != d:
        if TOTAL < b:
            TOTAL += (b+c)
            PRICE += (a*b)
        else:
            TOTAL += 1
            PRICE += a
    
    print(PRICE, TOTAL)


main()
