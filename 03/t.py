import numpy as np

def p1():
    data = open("inp.txt", "r").read().splitlines()
    dar = []
    for d in data:
        a = [int(i) for i in d]
        dar.append(a)
    ar = np.array(dar)
    bitnum1 = ar.sum(axis=0) >= ar.shape[0]/2
    bitnum1 = list(bitnum1.astype(int))
    st = [str(i) for i in bitnum1]
    st2 = [str((not i)*1) for i in bitnum1]
    b1 = int("".join(st),2)
    b2 = int("".join(st2),2)
    print(b1, b2, b1*b2)

def get_most_common(ar, i):
    val = 1 * (sum(ar[:,i])>= ar.shape[0]/2)
    return ar[ar[:,i] == val]


def get_least_common(ar, i):
    val = 1 * (sum(ar[:,i])>= ar.shape[0]/2)
    return ar[ar[:,i] != val]


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
        if len(tmpar) == 1:
            break
    st = [str(i) for i in tmpar[0]]
    b1 = int("".join(st),2)
    tmpar = ar.copy()
    for i in range(ar.shape[1]):
        tmpar =  get_least_common(tmpar, i)
        if len(tmpar) == 1:
            break
    st2 = [str(i) for i in tmpar[0]]
    b2 = int("".join(st2),2)
    print(b1, b2, b1*b2)

if __name__=="__main__":
    p1()
    p2()
