import numpy as np
from collections import Counter

def p1():
    """
    p2 solution works better bu im leaving this as is
    """
    data = open("inp.txt", "r").read().splitlines()
    d = np.array([int(i) for i in data[0].split(",")])
    days = 80
    for i in range(days):
        c = Counter(d)
        d = d - 1
        d[d==-1] = 6
        dl = list(d)
        for x in range(c[0]):
            dl.append(8)
        d = np.array(dl)
    print(len(d))


def p2():
    data = open("inp.txt", "r").read().splitlines()
    d = [int(i) for i in data[0].split(",")]
    days =256
    c = Counter(d)
    for i in range(days):
        for i in range(9):
            c[i-1] = c[i]
        c[6] = c[6] + c[-1]
        c[8] = c[-1]
        c[-1] = 0
    print(sum([ v for k,v in c.items()]))


if __name__=="__main__":
    # p1()
    p2()
