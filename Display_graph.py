import sys
import pickle
import matplotlib.pyplot as plt
file_paths = sys.argv[1:]
for p in file_paths:
    print(p)
    figx = pickle.load(file(p,'rb'))
    plt.show()