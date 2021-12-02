
from collections import defaultdict

def p1():
    data = open("inp0.txt", "r").read().splitlines()
    hor, dep = 0, 0
    for d in data:
        c, v = d.split()
        v = int(v)
        match c:
            case "forward":
                hor += v
            case "down":
                dep += v
            case "up":
                dep -= v
    print(hor*dep)




def p2():
    data = open("inp0.txt", "r").read().splitlines()
    hor, aim, dep = 0, 0, 0
    for d in data:
        c, v = d.split()
        v = int(v)
        match c:
            case "forward":
                hor += v
                dep += v*aim
            case "down":
                aim += v
            case "up":
                aim -= v
    print(hor*dep)

if __name__=="__main__":
    p1()
    p2()
