import numpy as np

def p1():
    data = open("inp.txt", "r").read().splitlines()
    dar = []
    for d in data:
        a = [int(i) for i in d.split()[0]]
        dar.append(a)
    ar = np.array(dar)
    bitnum1 = []
    for i in range(ar.shape[1]):
        bitnum1.append(1 if sum(ar[:,i])> ar.shape[0]//2 else 0)
    st = [str(i) for i in bitnum1]
    st2 = [str((not i)*1) for i in bitnum1]
    b1 = int("".join(st),2)
    b2 = int("".join(st2),2)
    print(b1, b2, b1*b2)
    res = ...
    print(res)

def get_most_common(ar, i):
    val = 1 if sum(ar[:,i])>= ar.shape[0]/2 else 0
    return ar[ar[:,i] == val]


def get_least_common(ar, i):
    val = 1 if sum(ar[:,i])>= ar.shape[0]/2 else 0
    val = 0 if val == 1 else 1
    return ar[ar[:,i] == val]


def p2():
    data = open("inp.txt", "r").read().splitlines()
    dar = []
    for d in data:
        a = [int(i) for i in d.split()[0]]
        dar.append(a)
    ar = np.array(dar)
    bitnum1 = []
    tmpar = ar.copy()
    for i in range(ar.shape[1]):
        tmpar =  get_most_common(tmpar, i)
        if len(tmpar[0]) == 1:
            break
    st = [str(i) for i in tmpar[0]]
    b1 = int("".join(st),2)

    tmpar = ar.copy()
    for i in range(ar.shape[1]):
        tmpar =  get_least_common(tmpar, i)
        print(len(tmpar))
        if len(tmpar) == 1:
            break
    st2 = [str(i) for i in tmpar[0]]
    b2 = int("".join(st2),2)
    print(b1, b2, b1*b2)

if __name__=="__main__":
    # p1()
    p2()
