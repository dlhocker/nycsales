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


# testing area. eventually want to export geotiffs from images
import gdal
from gdalconst import *
from osgeo import osr

def GetGeoInfo(FileName):
    SourceDS = gdal.Open(FileName, GA_ReadOnly)
    GeoT = SourceDS.GetGeoTransform()
    Projection = osr.SpatialReference()
    Projection.ImportFromWkt(SourceDS.GetProjectionRef())    
    return GeoT, Projection

def CreateGeoTiff(Name, Array, driver, 
                  xsize, ysize, GeoT, Projection):
    DataType = gdal.GDT_Float32
    NewFileName = Name+'.tif'
    # Set up the dataset
    DataSet = driver.Create( NewFileName, xsize, ysize, 1, DataType )
            # the '1' is for band 1.
    DataSet.SetGeoTransform(GeoT)
    DataSet.SetProjection( Projection.ExportToWkt() )
    # Write the array
    DataSet.GetRasterBand(1).WriteArray( Array )
    return NewFileName

def ReprojectCoords(x, y,src_srs,tgt_srs):
    trans_coords=[]
    transform = osr.CoordinateTransformation( src_srs, tgt_srs)
    x,y,z = transform.TransformPoint(x, y)
    return x, y

def array_to_raster(array,fname):
    """Array > Raster
    Save a raster from a C order array.

    :param array: ndarray
    """
    dst_filename = fname


    # You need to get those values like you did.
    x_pixels = 16  # number of pixels in x
    y_pixels = 16  # number of pixels in y
    PIXEL_SIZE = 3  # size of the pixel...        
    x_min = 553648  
    y_max = 7784555  # x_min & y_max are like the "top left" corner.
    wkt_projection = 'a projection in wkt that you got from other file'

    driver = gdal.GetDriverByName('GTiff')

    dataset = driver.Create(
        dst_filename,
        x_pixels,
        y_pixels,
        1,
        gdal.GDT_Float32, )

    dataset.SetGeoTransform((
        x_min,    # 0
        PIXEL_SIZE,  # 1
        0,                      # 2
        y_max,    # 3
        0,                      # 4
        -PIXEL_SIZE))  

    dataset.SetProjection(wkt_projection)
    dataset.GetRasterBand(1).WriteArray(array)
    dataset.FlushCache()  # Write to disk.
    return dataset, dataset.GetRasterBand(1)  #If you need to return, remenber to return  also the dataset because the band don`t live without dataset.

