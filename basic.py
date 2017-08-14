#!/usr/bin/python
import csv
import sys
import numpy as np
import matplotlib.pyplot as plt
fname = sys.argv[1]

l = 0 #counter for file length

with open(fname, 'rb') as csvfile:
     spamreader = csv.reader(csvfile, delimiter=',')
     for row in spamreader:
          l+=1

prices = np.zeros(l)

with open(fname, 'rb') as csvfile:
     ind = 0
     spamreader = csv.reader(csvfile, delimiter=',')
     for row in spamreader:
          prices[ind] = row[-2]
          ind += 1

#make histogram
#print(prices.shape)
#hist = np.histogram(prices)
#print(hist)
print('max,million')
print(max(prices)/10.0**6)
print('average')
print(np.mean(prices))
print(find(max(prices))
index, value = max(prices)
print(index)
#plt.plot(hist)
#plt.show()









