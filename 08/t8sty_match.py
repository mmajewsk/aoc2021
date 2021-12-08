from collections import Counter
import numpy as np

def p1():
    data = open("inp.txt", "r").read().splitlines()
    allowed = [2,4,3,7]
    s = 0
    for d in data:
        a,b = d.split("|")
        lilens = [len(i) for i in b.split()]

        alen = list(filter(lambda x: x in allowed, lilens))
        s += len(alen)
    print(s)


def p2():
    data = open("inp.txt", "r").read().splitlines()
    allowed = [2,4,3,7]
    letters= {
        "abcefg": 0,
        "acdeg": 2,
        "acdfg": 3,
        "abdfg": 5,
        "abdefg": 6,
        "abcdfg": 9,
        "cf": 1, #
        "bcdf": 4, #
        "acf": 7,  #
        "abcdefg": 8, #

    }
    s = 0
    for d in data:
        a,b = d.split("|")
        digits = a.split()
        c = Counter()
        c2 = Counter()
        tr = {}
        for d in digits:
            if len(d) in allowed:
                if len(d) == 2:
                    one = d
                if len(d) == 4:
                    four = d
                if len(d) == 3:
                    seven = d
                if len(d) == 7:
                    eight = d
                c2.update(d)
            else:
                c.update(d)
        for l in 'abcdefg':

            match l:
                case l if c[l]==5 and c2[l] == 2:
                    tr[l] = 'd'
                case l if c[l] + c2[l] == 7 and l in eight and l not in one+four+seven :
                    tr[l] = 'g'
                case l if c[l] == 4 and l in one :
                    tr[l] = 'c'
                case l if c[l] == 4 :
                    tr[l] = 'b'
                case l if c[l] == 5 and c2[l] == 4 :
                    tr[l] = 'f'
                case l if l in seven and l not in one :
                    tr[l] = 'a'
                case l if c[l] == 3 and c2[l]==1 :
                    tr[l] = 'e'
        output = b.split()
        transl = ["".join(sorted([tr[g] for g in p])) for p in output]
        numb = "".join([str(letters[s]) for s in transl])
        s += int(numb)
    print(s)


if __name__=="__main__":
    # p1()
    p2()
