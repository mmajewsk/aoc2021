from collections import Counter, defaultdict
import numpy as np
from numpy.lib.stride_tricks import sliding_window_view
from copy import deepcopy



def p1():
    data = open("p13.in", "r").read().splitlines()
    # data = open("inp0.txt", "r").read().splitlines()
    xs, ys= [], []
    first = True
    folds = []
    for d in data:
        if not d:
            first = False
            continue
        if first:
            x, y = d.split(',')
            xs.append(int(x))
            ys.append(int(y))
        else:

            print(d)
            fold = d.split()[-1]
            fw, fi = fold.split("=")
            fi = int(fi)
            folds.append((fw,fi))

    tab = np.zeros((max(xs)+1, max(ys)+1), dtype=bool).T
    tab2 = np.zeros((max(xs)+1, max(ys)+1), dtype=object).T
    for x,y in zip(xs,ys):
        tab[y,x] = True
        tab2[y,x] = "#"
    # print(tab2)

    for fw, fi in folds:
        print(fw,fi)
        if fw == 'y':
            a = tab[:fi]
            if tab.shape[0]%2 == 1:
                addp = 1
            else:
                addp = 0
            b = tab[fi+addp:]
            a = np.flip(a, axis=0)
            tab = a |  b

        if fw == 'x':
            a = tab[:, :fi]
            if tab.shape[1]%2 == 1:
                addp = 1
            else:
                addp = 0
            b = tab[:, fi+addp:]
            a = np.flip(a, axis=1)
            tab = a |  b

    for t in (tab*1):
        s ="".join([(" ." if c else " #") for c in t])
        print(s)
    print(tab*1)

def p2():
    # data = open("inp.txt", "r").read().splitlines()
    import numpy as np
    from parse import findall

    instr = open("p13.in").read()
    paper = np.zeros((9999,9999), bool)

    for x,y in findall('{:d},{:d}', instr):
        paper[y,x] = True

    for axis,p in findall('{:l}={:d}', instr):
        if axis == 'x':
            paper = paper[:,0:p] | paper[:, 2*p:p:-1]
        if axis == 'y':
            paper = paper[0:p,:] | paper[2*p:p:-1,:]
        print(paper.sum())

    print(np.array2string(paper, separator='',
        formatter = {'bool':lambda x: ' █'[x]}))

if __name__ == "__main__":
    p1()
    # p2()
