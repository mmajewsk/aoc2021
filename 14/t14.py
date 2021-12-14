from collections import Counter, defaultdict
import numpy as np
from numpy.lib.stride_tricks import sliding_window_view
from copy import deepcopy



def p1():
    data = open("p14.in", "r").read().splitlines()
    seq = ""
    rul = dict()
    for i, d in enumerate(data):
        if i==0:
            seq = d.strip()

        elif i>1:
            a,b = d.split(" -> ")
            rul[a] = b
    size = 10
    pairs = defaultdict(int)
    for j in range(1,len(seq)):
        t = seq[j-1]+seq[j]
        pairs[t] = 1
    for n in range(size):
        seq2 = ""
        for j in range(1,len(seq)):
            t = seq[j-1]+seq[j]
            r = rul[t]
            seq2 = seq2 + seq[j-1] + r
        seq2 = seq2 + seq[j]
        seq = seq2
    c = Counter(seq2)
    s = sorted(c.items(), key=lambda x: x[1])
    mi, ma = s[0], s[-1]
    print(ma[1]-mi[1])

def p2():
    data = open("p14.in", "r").read().splitlines()
    seq = ""
    rul = dict()
    for i, d in enumerate(data):
        if i==0:
            seq = d.strip()
        elif i>1:
            a,b = d.split(" -> ")
            rul[a] = b
    general_counter = Counter()
    word_counter = Counter(seq)
    for j in range(1,len(seq)):
        a,b = seq[j-1], seq[j]
        t = seq[j-1]+seq[j]
        general_counter[(a,b)] += 1
    size = 40
    for n in range(size):
        oldgc = general_counter.copy()
        for p,v in oldgc.items():
            a,b = p
            r = rul[a+b]
            general_counter[(a,b)] -= v
            general_counter[(a,r)] += v
            general_counter[(r,b)] += v
            word_counter[r] += v
    s = sorted(word_counter.items(), key=lambda x: x[1])
    mi, ma = s[0], s[-1]
    print(ma[1]-mi[1])

if __name__ == "__main__":
    # p1()
    p2()
