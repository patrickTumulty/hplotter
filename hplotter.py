
import sys
import numpy as np
import matplotlib.pyplot as plt

args = sys.argv
args.pop(0)

for data in args:
    plt.plot(np.array(data.split(",")).astype(float), "-")

plt.show()