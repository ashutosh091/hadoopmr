#!/usr/bin/python

import sys

oldKey = None
totalSize = 0
qSize = 0
totalCount = 0

# Loop around the datas.

for line in sys.stdin:

    data = line.split("\t")

    if len(data) < 3:
        continue
    
    recordType = data[1].strip()
    thisKey = data[0].strip()

    # Set oldKey when first record is encountered
    if oldKey == None:
	    oldKey = thisKey

    # whenever the key is changing
    if oldKey != thisKey:
        if totalCount > 0:
            print oldKey, qSize, "\t", (totalSize / totalCount)
        oldKey = thisKey
        totalSize = 0
        totalCount = 0
        if recordType == 'A':
            qSize = float(data[2].strip())
        if recordType == 'B':
            # if the first record after key has changed is B then ofcourse there is not corresponding user record for this key
            totalCount += 1
            totalSize += float(data[2].strip())


    else:
        # extract info of records based on type
        if recordType == 'A':
            qSize = float(data[2].strip())

        if recordType == 'B':
            totalCount += 1
            totalSize += float(data[2].strip())
if totalCount > 0:
    print oldKey, qSize, "\t", (totalSize / totalCount)
