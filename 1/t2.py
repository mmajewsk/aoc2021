import numpy as np
import pandas as pd
data = open("inp.txt", "r").read().splitlines()
d = np.array([int(d ) for d in data])
rolled = pd.DataFrame(d).rolling(3).sum()[2:]
print((rolled.diff()[1:]>0).sum())
