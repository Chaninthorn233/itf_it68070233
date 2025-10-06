"""Blackjack"""
n = int(input())
H1 = str()
H2 = str()
H3 = str()
CASE1 = 0
CASE2 = 0
CASE3 = 0
DIFF1 = 0
DIFF2 = 0
DIFF3 = 0

if n == 2:
    H1 = input()
    H2 = input()

    if H1 != "A" and H2 != "A":
        if H1 == "K":
            H1 = 10
        if H1 == "Q":
            H1 = 10
        if H1 == "J":
            H1 = 10

        else:
            H1 = int(H1)

        if H2 == "K":
            H2 = 10
        if H2 == "Q":
            H2 = 10
        if H3 == "J":
            H2 = 10

        else:
            H2 = int(H2)

        print(H1+H2)

    elif H1 == "A" and H2 != "A":
        if H2 == "K":
            H2 = 10
        if H2 == "Q":
            H2 = 10
        if H2 == "J":
            H2 = 10

        else:
            H2 = int(H2)

        if (H2 + 11) > 21:
            print(H2 + 1)

        elif (H2 + 11) <= 21:
            print(H2 + 11)

    elif H1 != "A" and H2 == "A":
        if H1 == "K":
            H1 = 10
        if H1 == "Q":
            H1 = 10
        if H1 == "J":
            H1 = 10

        else:
            H1 = int(H1)

        if (H1 + 11) > 21:
            print(H1 + 1)

        elif (H1 + 11) <= 21:
            print(H1 + 11)

    elif H1 == "A" and H2 == "A":
        print("12")


elif n == 3:
    H1 = input()
    H2 = input()
    H3 = input()

    if H1 != "A" and H2 != "A" and H3 != "A":
        if H1 == "K":
            H1 = 10
        if H1 == "Q":
            H1 = 10
        if H1 == "J":
            H1 = 10

        else:
            H1 = int(H1)

        if H2 == "K":
            H2 = 10
        if H2 == "Q":
            H2 = 10
        if H2 == "J":
            H2 = 10

        else:
            H2 = int(H2)

        if H3 == "K":
            H3 = 10
        if H3 == "Q":
            H3 = 10
        if H3 == "J":
            H3 = 10

        else:
            H3 = int(H3)

        print(H1+H2+H3)

    elif H1 == "A" and H2 != "A" and H3 != "A":
        if H2 == "K":
            H2 = 10
        if H2 == "Q":
            H2 = 10
        if H2 == "J":
            H2 = 10

        else:
            H2 = int(H2)

        if H3 == "K":
            H3 = 10
        if H3 == "Q":
            H3 = 10
        if H3 == "J":
            H3 = 10

        else:
            H3 = int(H3)

        if (H2 + 11 + H3) > 21:
            print(H2 + 1 + H3)

        elif (H2 + 11 + H3) <= 21:
            print(H2 + 11 + H3)

    elif H1 != "A" and H2 == "A" and H3 != "A":
        if H1 == "K":
            H1 = 10
        if H1 == "Q":
            H1 = 10
        if H1 == "J":
            H1 = 10

        else:
            H1 = int(H1)

        if H3 == "K":
            H3 = 10
        if H3 == "Q":
            H3 = 10
        if H3 == "J":
            H3 = 10

        else:
            H3 = int(H3)

        if (H1 + 11 + H3) > 21:
            print(H1 + 1 + H3)

        elif (H1 + 11 + H3) <= 21:
            print(H1 + 11 + H3)

    elif H1 != "A" and H2 != "A" and H3 == "A":
        if H1 == "K":
            H1 = 10
        if H1 == "Q":
            H1 = 10
        if H1 == "J":
            H1 = 10

        else:
            H1 = int(H1)

        if H2 == "K":
            H2 = 10
        if H2 == "Q":
            H2 = 10
        if H2 == "J":
            H2 = 10

        else:
            H2 = int(H2)

        if (H1 + 11 + H2) > 21:
            print(H1 + 1 + H2)

        elif (H1 + 11 + H2) <= 21:
            print(H1 + 11 + H2)

    elif H1 == "A" and H2 == "A" and H3 != "A":
        if H3 == "K":
            H3 = 10
        if H3 == "Q":
            H3 = 10
        if H3 == "J":
            H3 = 10

        else:
            H3 = int(H3)

        CASE1 = H3 + 1 + 1
        CASE2 = H3 + 1 + 11
        CASE3 = H3 + 11 + 11
        DIFF1 = CASE1 - 21
        DIFF2 = CASE2 - 21
        DIFF3 = CASE3 - 21

        if H3 == 10:
            print(H3 + 1 + 1)
        elif 2 < H3 < 10:
            print(H3 + 11 + 1)
        elif CASE1 < 21 < CASE2:
            print(CASE1)
        elif CASE1 > 21 > CASE2:
            print(CASE2)
        elif CASE1 < 21 and CASE2 < 21:
            if DIFF1 < DIFF2:
                print(CASE1)
            elif DIFF2 < DIFF1:
                print(CASE2)
        elif CASE1 > 21 and CASE2 > 21 and CASE3 > 21:
            if DIFF1 < DIFF2:
                if DIFF1 < DIFF3:
                    print(CASE1)
                elif DIFF1 > DIFF3:
                    print(CASE3)
            elif DIFF2 < DIFF1:
                if DIFF2 < DIFF3:
                    print(CASE2)
                elif DIFF2 > DIFF3:
                    print(CASE3)

    elif H1 == "A" and H2 != "A" and H3 == "A":
        if H2 == "K":
            H2 = 10
        if H2 == "Q":
            H2 = 10
        if H2 == "J":
            H2 = 10

        else:
            H2 = int(H2)

        CASE1 = H2 + 1 + 1
        CASE2 = H2 + 1 + 11
        CASE3 = H2 + 11 + 11
        DIFF1 = CASE1 - 21
        DIFF2 = CASE2 - 21
        DIFF3 = CASE3 - 21

        if H2 == 10:
            print(H2 + 1 + 1)
        elif 2 < H2 < 10:
            print(H2 + 11 + 1)
        elif CASE1 < 21 < CASE2:
            print(CASE1)
        elif CASE1 > 21 > CASE2:
            print(CASE2)
        elif CASE1 < 21 and CASE2 < 21:
            if DIFF1 < DIFF2:
                print(CASE1)
            elif DIFF2 < DIFF1:
                print(CASE2)
        elif CASE1 > 21 and CASE2 > 21 and CASE3 > 21:
            if DIFF1 < DIFF2:
                if DIFF1 < DIFF3:
                    print(CASE1)
                elif DIFF1 > DIFF3:
                    print(CASE3)
            elif DIFF2 < DIFF1:
                if DIFF2 < DIFF3:
                    print(CASE2)
                elif DIFF2 > DIFF3:
                    print(CASE3)


    elif H1 != "A" and H2 == "A" and H3 == "A":
        if H1 == "K":
            H1 = 10
        if H1 == "Q":
            H1 = 10
        if H1 == "J":
            H1 = 10

        else:
            H1 = int(H1)

        CASE1 = H1 + 1 + 1
        CASE2 = H1 + 1 + 11
        CASE3 = H1 + 11 + 11
        DIFF1 = CASE1 - 21
        DIFF2 = CASE2 - 21
        DIFF3 = CASE3 - 21
        if H1 == 10:
            print(H1 + 1 + 1)
        elif 2 < H1 < 10:
            print(H1 + 11 + 1)
        elif CASE1 < 21 < CASE2:
            print(CASE1)
        elif CASE1 > 21 > CASE2:
            print(CASE2)
        elif CASE1 < 21 and CASE2 < 21:
            if DIFF1 < DIFF2:
                print(CASE1)
            elif DIFF2 < DIFF1:
                print(CASE2)
        elif CASE1 > 21 and CASE2 > 21 and CASE3 > 21:
            if DIFF1 < DIFF2:
                if DIFF1 < DIFF3:
                    print(CASE1)
                elif DIFF1 > DIFF3:
                    print(CASE3)
            elif DIFF2 < DIFF1:
                if DIFF2 < DIFF3:
                    print(CASE2)
                elif DIFF2 > DIFF3:
                    print(CASE3)

    elif H1 == "A" and H2 == "A" and H3 == "A":
        print("13")
