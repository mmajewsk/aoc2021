from collections import Counter, defaultdict
import numpy as np
from numpy.lib.stride_tricks import sliding_window_view
from copy import deepcopy
import os, argparse
from aocd import submit
from math import prod
# submit(res, part="b", day=16)
# submit(res, part="a", day=16)

debug = False

data = open("table.in", "r").read().splitlines()
tr = {}
for d in data:
    a,b = d.split(" = ")
    tr[a]=b

def dbg(s=""):
    if debug:
        print(s)

def hex_to_bin(msg):
    return "".join([tr[x] for x in msg])

def cut(msg):
    dbg('cut')
    dbg(len(msg))
    if len(msg) < 8:
        return None
    version =msg[:3]
    pid =msg[3:6]
    rest = msg[6:]
    return version, pid, rest

def process_literal(res):
    msg = []
    i = 0
    while True:
        msg.append(res[i+1:i+5])
        if res[i] == '0':
            break
        i += 5
    con ="".join(msg)
    return int(con,2), res[i+5:]


def process(dec, data):
    c = cut(dec)
    if not c:
        return None
    v, pid, res = c
    data.append(v)
    if 4 == int(pid, 2):
        msg, res = process_literal(res)
        dbg('litereal')
        return msg, res
    else:
        dbg('subp')
        lid, res = res[0], res[1:]
        if lid == '0':
            tot, res = res[:15], res[15:]
            tot = int(tot, 2)
            subp, res = res[:tot], res[tot:]
            while True:
                msg, subp = process(subp, data)
                dbg(msg)
                dbg(subp)
                if len(subp) < 8:
                    break
            return msg,res
        else:
            num, res = res[:11], res[11:]
            num = int(num, 2)
            for i in range(num):
                msg, res = process(res, data)
                dbg(msg)
                dbg(res)
            return msg,res

def test_string(opex):
    dbg('=========')
    dec = hex_to_bin(opex)
    data = []
    msg, res = process(dec, data)
    dbg('fin')
    dbg(msg)
    dbg(res)
    dbg(data)
    dbg()
    dbg("answer:")
    s = sum([int(d,2) for d in data])
    print(s)

def p1_tests():

    packet = 'D2FE28'
    dec = hex_to_bin(packet)
    data = []
    msg, res = process(dec, data)
    dbg(msg)
    dbg(res)
    al = [
        '38006F45291200',
        'EE00D40C823060',
        '8A004A801A8002F478',
        '620080001611562C8802118E34',
        'C0015000016115A2E0802F182340',
        'A0016C880162017C3686B18A3D4780',
    ]
    for opex in al:
        test_string(opex)

def p1(args):
    data = open(args.path, "r").read().splitlines()
    opex = data[0]
    p1_tests()
    test_string(opex)

def work(res, foo):
    lid, res = res[0], res[1:]
    if lid == '0':
        tot, res = res[:15], res[15:]
        tot = int(tot, 2)
        subp, res = res[:tot], res[tot:]
        msgs = []
        while True:
            msg, subp = foo(subp)
            dbg(msg)
            dbg(subp)
            msgs.append(msg)
            if len(subp) < 8:
                break
        return msgs,res
    else:
        num, res = res[:11], res[11:]
        num = int(num, 2)
        msgs = []
        for i in range(num):
            msg, res = foo(res)
            msgs.append(msg)
            dbg(msg)
            dbg(res)
        return msgs,res

def process2(dec):
    c = cut(dec)
    if not c:
        return None
    v, pid, res = c
    ipid = int(pid, 2)
    if 4 == ipid:
        msg, res = process_literal(res)
        dbg('litereal')
        return msg, res
    else:

        msgs, res = work(res, process2)
        operations = {
            0: sum,
            1: prod,
            2: min,
            3: max,
            5: lambda x: int(x[0]>x[1]),
            6: lambda x: int(x[0]<x[1]),
            7: lambda x: int(x[0]==x[1]),
        }
        bar = operations[ipid]
        return bar(msgs), res

def test_string2(opex):
    dbg('=========')
    dec = hex_to_bin(opex)
    dbg(dec)
    msg, res = process2(dec)
    dbg('fin')
    dbg(msg)
    dbg(res)
    dbg(data)
    dbg()
    dbg("answer:")
    print(msg)

def p2_tests():
    al = [
        'C200B40A82',
        '04005AC33890',
        '880086C3E88112',
        '9C0141080250320F1802104A08'
    ]
    for opex in al:
        test_string2(opex)

def p2(args):
    data = open("table.in", "r").read().splitlines()
    tr = {}
    for d in data:
        a,b = d.split(" = ")
        tr[a]=b

    data = open(args.path, "r").read().splitlines()
    opex = data[0]
    p2_tests()
    test_string2(opex)

def main():
    script_name = os.path.basename(__file__)

    parser = argparse.ArgumentParser()
    parser.add_argument('-d', '--debug', action='store_true',
            help='Enable debug')
    parser.add_argument('path', nargs='?', default=f'input-{script_name}.txt',
            help='Path to the input file')

    args = parser.parse_args()
    global debug
    debug = args.debug
    p1(args)
    p2(args)

if __name__ == "__main__":
    main()
