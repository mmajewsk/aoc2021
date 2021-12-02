
from collections import defaultdict

def p1():
    data = open("inp0.txt", "r").read().splitlines()
    hor, dep = 0, 0
    for d in data:
        c, v = d.split()
        v = int(v)
        if c == "forward":
            hor += v
        if c == "down":
            dep += v
        if c == "up":
            dep -= v
    print(hor*dep)


def p2():
    data = open("inp0.txt", "r").read().splitlines()
    hor, aim, dep = 0, 0, 0
    for d in data:
        c, v = d.split()
        v = int(v)
        if c == "forward":
            hor += v
            dep += v*aim
        if c == "down":
            aim += v
        if c == "up":
            aim -= v
    print(hor*dep)

if __name__=="__main__":
    p2()
