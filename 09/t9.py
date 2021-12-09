from collections import Counter, defaultdict
import numpy as np
from numpy.lib.stride_tricks import sliding_window_view
from copy import deepcopy

def p1():
    data = open("inp0.txt", "r").read().splitlines()
    dat = []
    for d in data:
        dat.append([int(j) for j in d ])
    a = np.array(dat)
    b = np.pad(a,((1,1),(1,1)), 'constant', constant_values=10)
    top = sliding_window_view(a[:2,:], (2,3))
    bot = sliding_window_view(b[:,:], (3,3))
    lowest = []
    lnum = []
    for i in range(a.shape[0]):
        for j in range(a.shape[1]):
            startshape = bot[i,j]
            ami = np.argmin(startshape)
            res = np.unravel_index(startshape.argmin(), startshape.shape)
            nextwindow = (res[0]+i-1, res[1]+j-1)
            prevwindow = (i,j)
            while nextwindow != prevwindow:
                nextshape = bot[nextwindow[0], nextwindow[1]]
                ami = np.argmin(nextshape)
                res = np.unravel_index(nextshape.argmin(), nextshape.shape)
                prevwindow = deepcopy(nextwindow)
                nextwindow = (res[0]+prevwindow[0]-1, res[1]+prevwindow[1]+-1)
                # print()
                # print(ami, prevwindow, nextwindow)
                # print(nextshape)
                # print(nextshape[res[0], res[1]])
                # print(res)
                if nextwindow == (0,0):
                    break
            lowest.append(nextwindow)
            lnum.append(nextshape[res[0], res[1]])
        # print()
        # print()
    uni = list(Counter(lowest).keys())
    uninum = [bot[x,y][1,1] for x,y in uni]
    risked = [1+u for u in uninum]
    # print(sum(risked))
    return uni

def p2():
    data = open("inp0.txt", "r").read().splitlines()
    dat = []
    for d in data:
        dat.append([int(j) for j in d ])
    a = np.array(dat)
    b = np.pad(a,((1,1),(1,1)), 'constant', constant_values=10)
    top = sliding_window_view(a[:2,:], (2,3))
    bot = sliding_window_view(b[:,:], (3,3))
    lowest = []
    lnum = []
    basind = defaultdict(set)
    for i in range(a.shape[0]):
        for j in range(a.shape[1]):
            startshape = bot[i,j]
            ami = np.argmin(startshape)
            res = np.unravel_index(startshape.argmin(), startshape.shape)
            nextwindow = (res[0]+i-1, res[1]+j-1)
            prevwindow = (i,j)
            path = []
            path.append(prevwindow)
            while nextwindow != prevwindow:
                nextshape = bot[nextwindow[0], nextwindow[1]].copy()
                nextshape[0,0] = 10
                nextshape[2,0] = 10
                nextshape[0,2] = 10
                nextshape[2,2] = 10
                ami = np.argmin(nextshape)
                res = np.unravel_index(nextshape.argmin(), nextshape.shape)
                path.append(nextwindow)
                prevwindow = deepcopy(nextwindow)
                nextwindow = (res[0]+prevwindow[0]-1, res[1]+prevwindow[1]+-1)
                p = nextwindow
                prev = prevwindow
                if (p[0]-prev[0], p[1]-prev[1]) in ((1,1),(-1,-1),(-1,1),(1,-1)):
                    break
                print()
                print(ami, prevwindow, nextwindow)
                print(nextshape)
                print(nextshape[res[0], res[1]])
                print(res)
                if nextwindow == (0,0):
                    break
            if path:
                prev = path[-1]
            for p in reversed(path):
                # if (p[0]-prev[0], p[1]-prev[1]) in ((1,1),(-1,-1),(-1,1),(1,-1)):
                #     break

                prev = p
                if bot[p[0], p[1]][1,1]!=9:
                    basind[nextwindow].add(p)
                # print( p, bot[p[0], p[1]][1,1])
            lowest.append(nextwindow)
            lnum.append(nextshape[res[0], res[1]])
        # print()
        # print()
    uni = list(Counter(lowest).keys())
    # uninum = [bot[x,y][1,1] for x,y in uni]
    # risked = [1+u for u in uninum]
    print(basind)
    for k,v in basind.items():
        print(k, [bot[p[0], p[1]][1,1] for p in v])
        print(len(v))
    # print(sum(risked))
    # return uni

if __name__=="__main__":
    # print(p1())
    p2()
