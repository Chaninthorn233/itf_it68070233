"""docstring"""
def main(move):
    """doctsring"""
    point = 1
    for i in move:
        if i == "A":
            if point == 1:
                point = 2
            elif point == 2:
                point = 1
        if i == "B":
            if point == 2:
                point = 3
            elif point == 3:
                point = 2
        if i == "C":
            if point == 1:
                point = 3
            elif point == 3:
                point = 1

    print(point)
main(input())
