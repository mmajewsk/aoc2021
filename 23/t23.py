

from collections import Counter, defaultdict
# import numpy as np
# from numpy.lib.stride_tricks import sliding_window_view
from copy import deepcopy
import os, argparse
from aocd import submit
from itertools import permutations
# from math import prod
# submit(res, part="b", day=16)
# submit(res, part="a", day=16)


debug = False

  #A#D#C#A#

def dbg(*args):
    if debug:
        print(*args)

roomtoplace = {0:2,1:4,2:6,3:8}

destination = {
    "A":2,
    "B":4,
    "C":6,
    "D":8
}

def calc(data, start, end):
    x, y = start
    enum, epos = end
    moves = 0
    # dbg(f"Starting calc {start} {end}")
    if data.get(end, False):
        return None
    while x != enum or y != epos:
        if y != 0 and x!= enum:
            y += 1
        elif x==enum and y!= epos:
            y -= 1
        else:
            diff = enum - x
            direction = int(diff/abs(diff))
            x += direction
        nextpoint = (x, y)
        # dbg(nextpoint)
        if data.get(nextpoint):
            return None
        else:
            moves += 1
    return moves

def check_end(state):
    for k,(v,loc) in state.items():
        if k[0] != destination[v]:
            return False
    return True

prices = {
    "A":1,
    "B":10,
    "C":100,
    "D":1000,
}


def calc(unmoved, corridor, homed, start, end):
    x, y = start
    enum, epos = end
    moves = 0
    if start == end:
        return 0
    total = unmoved + corridor + homed
    data = {a:b for a,b in total}
    if data.get(end, False):
        return None
    while x != enum or y != epos:
        if y != 0 and x!= enum:
            y += 1
        elif x==enum and y!= epos:
            y -= 1
        else:
            diff = enum - x
            direction = int(diff/abs(diff))
            x += direction
        nextpoint = (x, y)
        # dbg(nextpoint)
        if data.get(nextpoint):
            return None
        else:
            moves += 1
    return moves

possibilities = set([0,1,3,5,7,9,10])
template="""
#############
#{corr}#
###{rooms[(2, -1)]}#{rooms[(4, -1)]}#{rooms[(6, -1)]}#{rooms[(8, -1)]}###
  #{rooms[(2, -2)]}#{rooms[(4, -2)]}#{rooms[(6, -2)]}#{rooms[(8, -2)]}#
  #{rooms[(2, -3)]}#{rooms[(4, -3)]}#{rooms[(6, -3)]}#{rooms[(8, -3)]}#
  #{rooms[(2, -4)]}#{rooms[(4, -4)]}#{rooms[(6, -4)]}#{rooms[(8, -4)]}#
  #########
"""


def visualize(unmoved, corridor, homed):
    rooms = defaultdict(lambda : '.')
    corids = {a:b for a,b in corridor}
    corr = ""
    for cr in range(11):
        k = corids.get((cr,0))
        if k:
            corr += k[0]
        else:
            corr += "."
    for h, (v,l) in homed:
        rooms[str(h)] = "\033[1m"+v+'\033[0m'
    for un, (v,l) in unmoved:
        rooms[str(un)] = v
    print('__________________')
    print("un   ", unmoved)
    print("cor  ", corridor)
    print("homed", homed)
    print(template.format(corr=corr, rooms=rooms))
    print('__________________')



import functools

globbest = float('inf')

@functools.lru_cache()
def recsol(unmoved, corridor, homed, cost):
    if len(homed) == 16:
        global globbest
        if cost<globbest:
            globbest = cost
        return cost
    if cost>globbest:
        return float('inf')

    newhomed = homed
    newcor = corridor
    newstate = unmoved
    # if debug: visualize(unmoved,corridor,homed)
    costs = [float('inf')]
    for i,p in enumerate(corridor):
        cor, (v,l) = p
        trgt = destination[v]
        if len(corridor) > 1:
            smaller = list(filter(lambda x:x<cor[0], cor))
            bigger = list(filter(lambda x:x>cor[0], cor))
            if len(smaller) !=0:
                if cor[0]-trgt>0 and trgt<max(smaller)<cor[0]:
                    continue
            if len(bigger) != 0:
                if cor[0]-trgt<0 and cor[0]<min(bigger)<trgt:
                    continue

        trgts = [
            (trgt, -1),
            (trgt, -2),
            (trgt, -3),
            (trgt, -4),
        ]
        ms = [calc(unmoved, corridor, homed, cor, t) for t in trgts]
        homedids = [a for (a,b) in homed]
        ayun = [dict(unmoved).get(t,False) for t in trgts]
        if any(ayun):
            continue
        for jay,(m,t) in enumerate(zip(ms,trgts)):
            if not m:
                break
            elif m:
                if jay<3 and ms[jay+1]:
                    continue
                else:
                    newcor = corridor[:i] + corridor[i+1:]
                    newcost = cost + prices[v]*m
                    newhomed = homed + ((t,(v,True)),)
                    res= recsol(unmoved, newcor, newhomed, newcost)
                    costs.append(res)
    takenposes = set([a for (a,b),(_, _) in corridor])
    freeposes = possibilities - takenposes
    nfreeposes = freeposes
    for i,un in enumerate(unmoved):
        unreclev = len(unmoved)
        ntest = 15
        if  unreclev >= ntest:
            print(("="*(ntest-unreclev)) +str(unreclev))
            if unreclev == ntest:
                print(i, globbest)
        pos, (v,l) = un
        a,b = pos
        prev = dict(unmoved).get((a,b+1))
        if prev:
            continue
        if a==destination[v]:
            below = list(range(b-1,-5,-1))
            belowtest = [dict(unmoved)[a,bel]==destination[v] for bel in below]
            cond = all(belowtest) if len(belowtest)!=0 else False
            if b==-4 or cond:
                newstate = unmoved[:i] + unmoved[i+1:]
                newhomed = homed + ((pos,(v,True)),)
                res= recsol(newstate, corridor, newhomed, cost)
                costs.append(res)
                continue
        if len(corridor) > 0:
            smaller = list(filter(lambda x:x<a, takenposes))+[-1]
            bigger = list(filter(lambda x:x>a, takenposes))+[11]
            lb = max(smaller)
            ub = min(bigger)
            nfreeposes = filter(lambda x: lb<x<ub, freeposes)
        for p in nfreeposes:
                # if b==-2 or dict(unmoved)[(a,-2)] == destination[v]:
                #     newstate = unmoved[:i] + unmoved[i+1:]
                #     newhomed = homed + ((pos,(v,True)),)
                #     res= recsol(newstate, corridor, newhomed, cost)
                #     costs.append(res)
                #     continue
            m = calc(unmoved, corridor, homed, pos, (p, 0))
            if m:
                newstate = unmoved[:i] + unmoved[i+1:]
                newcor = corridor + (((p,0),(v,l)),)
                newcost = cost+prices[v]*m
                res= recsol(newstate, newcor, homed, newcost)
            else:
                res= float('inf')
            costs.append(res)

    return min(costs)


from tqdm import tqdm

def p1(args):
    _data = open(args.path).read().splitlines()
    data = []
    for i,d in enumerate(_data):
        if 2<=i <=3:
            print(d)
            data.append(d.strip().replace("#",""))
    data = list([list(i) for i in zip(*data)])
    alldat = {}
    s = {}
    for room, v in enumerate(data):
        place = roomtoplace[room]
        for j, inrum in enumerate(v):
            alldat[(place, j*-1-1)] = (inrum, False)
    s = tuple([(k,v) for (k,v) in alldat.items()])
    res = recsol(s, tuple(), tuple(), 0)
    res = globbest
    return res


def p2(args):
    _data = open(args.path).read().splitlines()
    data = []
    for i,d in enumerate(_data):
        if 2<=i <=5:
            print(d)
            data.append(d.strip().replace("#",""))
    data = list([list(i) for i in zip(*data)])
    alldat = {}
    s = {}
    for room, v in enumerate(data):
        place = roomtoplace[room]
        for j, inrum in enumerate(v):
            alldat[(place, j*-1-1)] = (inrum, False)
    s = tuple([(k,v) for (k,v) in alldat.items()])
    res = recsol(s, tuple(), tuple(), 0)
    res = globbest
    print(res)
    return res

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
    # res = p1(args)
    # if args.p1:
        # submit(res, part="a", day=int(day))
    res = p2(args)
    if args.p2:
        submit(res, part="b", day=int(day))
    # run(args)

if __name__ == "__main__":
    main()
