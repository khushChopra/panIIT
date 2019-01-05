import csv
import numpy as np

filename="solution.csv"
csv = np.genfromtxt(filename, dtype=int, delimiter=",",usecols=[1])
print(csv)

