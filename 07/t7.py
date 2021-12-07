from collections import Counter

# def p1():
#     data = open("inp.txt", "r").read().splitlines()
#     d = np.array([int(i) for i in data[0].split(',')])
#     res = d.mean()
#     mi = min(d)
#     ma = max(d)
#     costs = []
#     for i in range(mi,ma+1):
#         c = np.sum(np.abs(d-i))
#         costs.append((i,c))
#     print(sorted(costs, key=lambda x: x[1])[0])



def p2():
    data = open("inp.txt", "r").read().splitlines()
    d = [int(i) for i in data[0].split(',')]
    mi = min(d)
    ma = max(d)
    costs = []
    for i in range(mi,ma+1):
        s = []
        for j in d:
            diff = abs(i-j)
            r = range(1,diff+1)
            ran = list(r)
            pr = sum(ran)
            s.append(pr)
        costs.append((i,sum(s)))
    print(sorted(costs, key=lambda x: x[1])[0])



if __name__=="__main__":
    # p1()
    p2()
