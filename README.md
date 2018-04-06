# nycsales: a small data science project to explore building sales data in new york city

# repo contents
 - basic_stats.ipynb: python notebook demonstrating some basic statistics on the data
 - clustering_examples.ipynb: some use of k-means to find ways to clump together pricing data, and use of kmeans to "create" new neighborhoods
 - CNNclassifiers.ipynb: use of convolutional neural networks in Tensorflow to classify buildings as ranging from cheap to expensive (currently ~96% accurate) 
 - database_joins.ipynb: python notebook performing pandas joins of the sales data with geospatial data from building shapefile
 - nycsales.py: set of functions to help with joins, datetime formatting, and eventuall geotiff file creation
 - dataformat.sh: script to format the sales data (with headers) from excel to a friendly .csv format
 - dataconvert.py: pandas conversion of .xls to .csv
 - nycsales_schema.sql: equivalent sql schema for the sales data

# data used
The analysis is primarily looking at rolling sales data collection by the NYC department of finance from 2003 onward. The raw data in .xls format can be found at http://www1.nyc.gov/site/finance/taxes/property-rolling-sales-data.page. I have included a few examples files from 2015 in this repo.

The other data set used in conjunction with this is the NYC building footprint dataset that provides geospatial data for every building structure in new york. It is a rather large data set, and is not included in this git repo. It can be round at https://data.cityofnewyork.us/Housing-Development/Building-Footprints/nqwf-w8eh/data
 
# packages used
This project is mean to showcase the use of a few modern python packages. Pandas is the main workhorse here, allowing very easy database-type operations. scikitlearn is also utilized for k-means clustering, as are several modules such as gdal to allow for geotiff formatting.

# where this work is headed
I'm aiming to unearth some low-dimensional structure behind how buildings are sold in new york. While I'm particularly interested in how clustering routines can help revel the spatial relationships among building sales, I also want to explore some machine learning classification methods to predict building sale prices. I believe that using some gaussian mixture models could also help model prices by neighborhood borough.