from collections import Counter, defaultdict
import numpy as np
from numpy.lib.stride_tricks import sliding_window_view
from copy import deepcopy

def stride(a,b, i, j):
    x = max(min(i,a-1), 0)
    y = max(min(j,b-1), 0)
    return x,y

def window_inds(ar, i, j):
    a,b = ar.shape
    return {
        stride(a,b, i-1, j),
        stride(a,b, i+1, j),
        stride(a,b, i, j+1),
        stride(a,b, i, j-1),
    }

def process(a):
    a += 1
    tmp = a.copy()
    a,b = a.shape
    neighbours = [
        (-1,-1),
        (0,-1),
        (0,1),
        (-1,0),
        (-1,1),
        (1,0),
        (1,1),
        (1,-1)
    ]
    c = 0
    flashed = set()

    # print('enter')
    # print(tmp)
    # print()
    while np.any(tmp > 9):
        newset = flashed.copy()
        for i in range(a):
            for j in range(b):
                if tmp[i,j] > 9 and  (i,j) not in flashed:
                    for x,y in neighbours:
                        if 0 <= i+x <= a-1 and 0 <= j+y <= b-1:
                            tmp[i+x,j+y] += 1
                    flashed.add((i,j))
        # print()
        # print('loop')
        # print(tmp)
        # print()
        # print()
        if newset == flashed:
            break
    for i,j in flashed:
        tmp[i,j] = 0
    return tmp, len(flashed)






def p1():
    data = open("inp0.txt", "r").read().splitlines()
    dat = []
    for d in data:
        dat.append([int(c) for c in d])
    a = np.array(dat)

    total = 0
    for step in range(1000):
        a, c = process(a)
        # print(a)
        total += c
        # if step == 1:
        #     break
        if np.all(a == 0):
            print("flash all ", step)
            break

    print(total)


def p2():
    data = open("inp.txt", "r").read().splitlines()
    pass


if __name__ == "__main__":
    print('dsafd')
    p1()
    # p2()
