from collections import Counter, defaultdict
import numpy as np
from numpy.lib.stride_tricks import sliding_window_view
from copy import deepcopy


def rec(cur, prev_path, all_path, m):
    prev_path = prev_path + (cur, )
    if cur == 'end':
        return prev_path
    choices = m[cur]
    res = None
    for position in choices:
        if position.isupper():
            res = rec(position, prev_path, all_path, m)
        if position.islower() and position not in prev_path:
            res = rec(position, prev_path, all_path, m)
        all_path.add(res)

def p1():
    data = open("inp.txt", "r").read().splitlines()
    dat = []
    places = set()
    connections = []
    paths = defaultdict(set)
    for d in data:
        a,b = d.split('-')
        places.add(a)
        places.add(b)
        connections.append((a,b))
        paths[a].add(b)
        paths[b].add(a)
    position = 'start'
    all_path = set()
    rec(position, (), all_path, paths)
    all_path = all_path - {None}
    print(len(all_path))


def rec2(cur, prev_path, all_path, m):
    prev_path = prev_path + (cur, )
    if cur == 'end':
        return prev_path
    choices = m[cur]
    res = None
    for position in choices:
        prevc = Counter(prev_path)
        alredc = [v for k,v in prevc.items() if k.islower()]
        alred = (max(alredc) == 2)
        if position in ['start', 'end']:
            if position not in prev_path:
                res = rec2(position, prev_path, all_path, m)
        elif position.islower() and alred and position not in prev_path:
            res = rec2(position, prev_path, all_path, m)
        elif position.islower() and prevc[position] <= 1 and not alred:
            res = rec2(position, prev_path, all_path, m)
        if position.isupper():
            res = rec2(position, prev_path, all_path, m)
        all_path.add(res)


def p2():
    data = open("inp.txt", "r").read().splitlines()
    dat = []
    places = set()
    connections = []
    paths = defaultdict(set)
    for d in data:
        a,b = d.split('-')
        places.add(a)
        places.add(b)
        connections.append((a,b))
        paths[a].add(b)
        paths[b].add(a)
    position = 'start'
    all_path = set()
    rec2(position, (), all_path, paths)
    all_path = all_path - {None}
    print(len(all_path))



if __name__ == "__main__":
    # p1()
    p2()
