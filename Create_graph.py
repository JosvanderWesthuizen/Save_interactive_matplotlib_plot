import matplotlib.pyplot as plt
import pickle

#Create an example plot
fig = plt.plot([1,2,3,4],[4,3,2,1])
#save the plot with pickle
pickle.dump(fig, file("temp_name.fig.pickle","wb")) #Replace 'file' with 'open' for python 3
