from collections import Counter, defaultdict
import numpy as np
from numpy.lib.stride_tricks import sliding_window_view
from copy import deepcopy
import os, argparse
from aocd import submit
from math import prod
# submit(res, part="b", day=16)
# submit(res, part="a", day=16)


alg = ""
debug = False

def dbg(s=""):
    if debug:
        print(s)

def subar(ar, alg):
    lst = ar.ravel().tolist()
    lstr = [str(i) for i in lst]
    # dbg(lstr[0])
    bnum = "".join(lstr)
    val = int(bnum,2)
    rval = alg[val]
    # dbg(ar)
    # dbg(val)
    # dbg(rval)
    return 1 if rval=="#" else 0

def sol(args, iterations):
    _data = open(args.path).read().splitlines()
    img = []
    for i, d in enumerate(_data):
        if i ==0:
            alg = d
        else:
            if d:
                img.append([1 if x=='#' else 0 for x in d])
    img2 = np.array(img)
    border = 5
    b = np.pad(img2,((border,border),(border,border)), 'constant', constant_values=0)
    get = lambda x: subar(x, alg)
    flipper = 0
    for it in range(iterations):
        win = sliding_window_view(b,(3,3))
        tmp = np.zeros(win.shape[:2], dtype=int)
        for i in range(tmp.shape[0]):
            for j in range(tmp.shape[0]):
                tmp[i,j] = get(win[i,j])
        if alg[0] == '#' and alg[-1] == '.':
            if it%2==0:
                flipper = 1
            else:
                flipper = 0
        b = np.pad(tmp,((border,border),(border,border)), 'constant', constant_values=flipper)
    res = b.sum()
    return res

def p1(args):
    return sol(args, 2)
def p2(args):
    return sol(args,50)

def main():
    script_name = os.path.basename(__file__)
    day = script_name[1:3]
    parser = argparse.ArgumentParser()
    parser.add_argument('-d', '--debug', action='store_true',
            help='Enable debug')
    defname = f"p{day}.in"
    parser.add_argument(
        "path", nargs="?", default=defname, help="Path to the input file"
    )
    parser.add_argument('-p1', action='store_true',
            help='submit p1')
    parser.add_argument('-p2', action='store_true',
            help='submit p2')
    args = parser.parse_args()
    global debug
    debug = args.debug
    res = p1(args)
    if args.p1:
        submit(res, part="a", day=int(day))
    # res = p2(args)
    if args.p2:
        submit(res, part="b", day=int(day))
    # run(args)

if __name__ == "__main__":
    main()
