import numpy as np
data = open("inp.txt", "r").read().splitlines()
d = np.array([int(d ) for d in data])
print(sum(np.diff(d) > 0))
