#!/usr/bin/env python

import xlrd
import csv
import sys

fnamein = sys.argv[1]
fnameout = fnamein.split('.')[0]+'.csv'

with xlrd.open_workbook(fnamein) as wb:
    sh = wb.sheet_by_index(0)  # or wb.sheet_by_name('name_of_the_sheet_here')
    with open(fnameout, 'wb') as f:
        c = csv.writer(f)
        for r in range(sh.nrows):
            c.writerow(sh.row_values(r))








