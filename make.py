import csv
import numpy as np

filename="solution.csv"
csv = np.genfromtxt(filename, dtype=int, delimiter=",",usecols=[1])
csv = np.delete(csv, (0), axis=0)
import pickle
with open("Y.obj","wb") as fp:
	pickle.dump(csv,fp)
print(csv)

