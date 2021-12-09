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
        (i,j),
        stride(a,b, i-1, j),
        stride(a,b, i+1, j),
        stride(a,b, i, j+1),
        stride(a,b, i, j-1),
    }



def as_windows(ar):
    a,b = ar.shape
    basin = defaultdict(set)
    minima = set()
    for i in range(a):
        for j in range(b):
            step = (-10,-10)
            next_step = (i,j)
            path = []
            while step != next_step:
                path.append(next_step)
                window = window_inds(ar, next_step[0], next_step[1])
                slist = [((x,y), ar[x,y]) for x,y in window]
                sor = sorted(slist, key=lambda x: x[1])
                step = next_step
                next_step = sor[0][0]
                if next_step == step:
                    minima.add(next_step)
            for p in path:
                basin[next_step].add(p)
    print()
    print(minima)
    print()
    sums= []
    for k,v in basin.items():
        # print()
        # print('==============================================')
        # print("lowest px: ", k, "  val", ar[k[0], k[1]])
        tab = np.zeros((a,b))
        s = 0
        for x,y in v:
            if ar[x,y] != 9:
                tab[x,y] = ar[x,y]
                s += 1
        sums.append(s)
    t1, t2, t3 = list(sorted(sums))[-3:]
    res = t1*t2*t3
    print(res)





def p1():
    data = open("inp.txt", "r").read().splitlines()
    dat = []
    for d in data:
        dat.append([int(j) for j in d ])
    a = np.array(dat)
    as_windows(a)



if __name__=="__main__":
    print(p1())
    # p2()
