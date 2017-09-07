#set of functions that might be useful for later calculations

#this is a notebook for running a few scripts to get the 
#original sales data from a csv format into pandas,
#as well as the relevant GIS building footprint into a csv file.
#This is more of a grab-bag of commands to get ready for some 
#pandas joins and a sql join (which I may execute from python)

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import tensorflow as tf
from geopy.geocoders import Nominatim
import datetime

def join_latlong(db,shapecsvname):
    #function to join a pandas database with borough, blot, and lot info
    #with a shapefile-based csv made from database_joins.ipynb
    
    #load a csv file of interest
    shapecsv = pd.read_csv(shapecsvname,sep = ',')
    #calculate the bbl and format it as string
    borough = [str(item) for item in np.array(db.loc[:,'BOROUGH']).astype(int)]
    block= [str(item).zfill(5) for item in np.array(db.loc[:,'BLOCK']).astype(int)]
    lot = [str(item).zfill(4) for item in np.array(db.loc[:,'LOT']).astype(int)]
    bbl = []
    for k in range(len(borough)):
        bbl.append(int(borough[k]+block[k]+lot[k]))

    db['bbl'] = pd.Series(bbl,index=db.index)
    #join the databases
    joinedpd = pd.merge(db,shapecsv,on='bbl')
    
    return joinedpd

def toDateTime(S):
    #will return list of datetime objects
    #input: S, a pandas dataframe or series
    import pandas as pd
    import numpy as np
    from datetime import datetime
    
    Slist = S.tolist()
    n = len(Slist)
    dates = []
    for j in range(n):
        dates.append(datetime.strptime(Slist[j],'%Y-%m-%d'))
    
    return dates