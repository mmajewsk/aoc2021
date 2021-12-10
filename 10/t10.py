from collections import Counter, defaultdict
import numpy as np
from numpy.lib.stride_tricks import sliding_window_view
from copy import deepcopy


def p1():
    data = open("inp.txt", "r").read().splitlines()
    dat = []
    clo = ")]}>"
    ope = "([{<"
    tr = dict(zip(clo, ope))
    vals = {')':3, ']':57, '}':1197, '>':25137}
    errors = []
    for d in data:
        co = defaultdict(int)
        stack = []

        for c in d:
            if c in ope:
                co[c] += 1
                stack.append(c)
            if c in ")]}>":
                o = tr[c]
                if stack[-1] == o:
                    stack.pop(-1)
                else:
                    errors.append(c)
                    break
                co[o] -= 1

    res = sum([vals[k] for k in errors])
    print(res)
    # print(errors)
    #

def p2():
    data = open("inp.txt", "r").read().splitlines()
    dat = []
    clo = ")]}>"
    ope = "([{<"
    tr = dict(zip(clo, ope))
    un = dict(zip(ope, clo))
    vals = {')':3, ']':57, '}':1197, '>':25137}
    ends = {')':1, ']':2, '}':3, '>':4}
    errors = []
    for j, d in enumerate(data):
        co = defaultdict(int)
        stack = []

        for c in d:
            if c in ope:
                stack.append(c)
            if c in ")]}>":
                o = tr[c]
                if stack[-1] == o:
                    stack.pop(-1)
                else:
                    errors.append(j)
                    break
    ans = []
    results = []
    for j, d in enumerate(data):
        co = defaultdict(int)
        stack = []
        for c in d:
            if j in errors:
                continue
            if c in ope:
                co[c] += 1
                stack.append(c)
            if c in ")]}>":
                o = tr[c]
                if stack[-1] == o:
                    stack.pop(-1)
                else:
                    errors.append(c)
                    break
                co[o] -= 1
        closers = list(reversed([un[k] for k in stack]))
        su = 0
        for cl in closers:
            su = 5*su+ends[cl]


        if su:
            results.append(su)
        ans.append(closers)


    # print(ans)
    so = list(sorted(results))
    middleIndex = (len(so) - 1)//2

    print(so[middleIndex])

    # print(errors)
if __name__=="__main__":
    # p1()
    p2()
