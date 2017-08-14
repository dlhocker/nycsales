import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


#basic test to load a frame and check prices with a histogram
#testframe = pd.read_csv('2015_manhattan.csv',sep = ',')
#sales = testframe['SALE PRICE']
#hist = np.histogram(sales)
#n, bins, patches = plt.hist(sales, 20, normed=1)

#concat the brooklyn data frames
bk15 = pd.read_csv('2015_brooklyn.csv',sep = ',')
bk14 = pd.read_csv('2014_brooklyn.csv',sep = ',')
bk13 = pd.read_csv('2013_brooklyn.csv',sep = ',')
bk12 = pd.read_csv('2012_brooklyn.csv',sep = ',')
bk11 = pd.read_csv('2011_brooklyn.csv',sep = ',')
bk10 = pd.read_csv('2010_brooklyn.csv',sep = ',')
bk9 = pd.read_csv('2009_brooklyn.csv',sep = ',')
bk8 = pd.read_csv('sales_2008_brooklyn.csv',sep = ',')
bk7 = pd.read_csv('sales_2007_brooklyn.csv',sep = ',')
bk6 = pd.read_csv('sales_brooklyn_06.csv',sep = ',')
bk5 = pd.read_csv('sales_brooklyn_05.csv',sep = ',')
bk4 = pd.read_csv('sales_brooklyn_04.csv',sep = ',')
bk3 = pd.read_csv('sales_brooklyn_03.csv',sep = ',')


bkall = pd.concat([bk15,bk14,bk13,bk12,bk11,bk10,bk9,bk8,bk7,bk6,bk5,bk4,bk3])
bklist = [bk3,bk4,b5,bk6,bk7,bk8,bk9,bk10,bk11,bk12,bk13,bk14,bk15]
sales = bkall['SALE PRICE'][bkall['SALE PRICE']< 0]
sqft = bkall['GROSS SQUARE FEET'][bkall['GROSS SQUARE FEET'] > 0]

ppsf = sales/


#grab price per square foot


