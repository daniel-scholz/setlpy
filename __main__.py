import setlx
from setlx.splayset import Set


def main():
    s1 = Set()
    s2 = Set()
    j = 10
    for i in range(1, 100):
        s1.insert(setlx.List([10 - i, j]))
    for i in range(1, 100):
        s1[10 - i]= j +1

    print(s1)


main()
