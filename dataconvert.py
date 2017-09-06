#!/usr/bin/env python

#a script to convert .xls files into csv files, catchign the datetime conversion in excel and making it a datetime python

import xlrd
import csv
import sys
import datetime

fnamein = sys.argv[1]
fnameout = fnamein.split('.')[0]+'.csv'
dateind = -1

#find the index to start by locating "Borough"
ignoreinds = -1 #indices to ignore in the writing, metadata header info


def findheader(sh):
    for i in range(5):
        for j in sh.row_values(i):            
            if str(j).lower().find('borough') >= 0:
                ignoreinds = i
                print('found it')
                print(ignoreinds)
                return ignoreinds

with xlrd.open_workbook(fnamein) as wb:
    sh = wb.sheet_by_index(0)  # or wb.sheet_by_name('name_of_the_sheet_here')
    #iterate over rows until you find 'Borough', keeping track of index, then quit
    ignoreinds = findheader(sh) 
    
    with open(fnameout, 'wb') as f:
        c = csv.writer(f)
        for r in range(sh.nrows):
            if r ==ignoreinds:
                #strip the stuff of any dumb characters
                newheader = sh.row_values(r)
                for k in range(len(sh.row_values(r))):
                    newheader[k] = newheader[k].strip().strip('\n').strip('"')
                c.writerow(newheader)
            
            if r > ignoreinds:
                #replace datetime row with correct form, if a float
                if type(sh.row_values(r)[-1])==type(1.0):
                    a = sh.row_values(r)[:-1]
                    seconds = (sh.row_values(r)[-1] - 25569) * 86400.0
                    dt = datetime.datetime.utcfromtimestamp(seconds).date()
                    a.append(dt)
                    c.writerow(a)
                else:
                    c.writerow(sh.row_values(r))

                            








