#!/bin/bash

#function to format .xls files into suitable .csv files for pandas and sql

#remove header and format header

#now run xls to csv
python dataconvert.py ${1}.xls

#remove any dumb space from csv headers
cat $1.csv |sed 's/","/,/g'|sed 's/"BOR/BOR/g' |sed '/,,,,*/d' > $1.tmp
mv $1.tmp $1.csv

#example command to execute all of one borough
#for i in $(ls data/*brooklyn.xls|awk 'BEGIN {FS = "."}; {print $1}'); do ./dataformat.sh $i; done; 