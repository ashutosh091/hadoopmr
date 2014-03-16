#!/usr/bin/python

import sys
import operator

oldKey = None
count = 0
keysMap = {}

# Loop around the data; we are actually doing left outer join here of node with users.

for line in sys.stdin:

    data = line.split("\t")

    if len(data) > 1:
        continue

    thisKey = data[0].strip()

    # Set oldKey and houra when first record is encountered
    if oldKey == None:
	oldKey = thisKey

    # whenever the key is changing
    if oldKey != thisKey: 
	keysMap[oldKey] = count
	# reset now
	oldKey = thisKey
	count = 1
    else:
        # when same key is being continued
	count += 1


# print top 10 records
sortedRecs = sorted(keysMap.iteritems(), key = operator.itemgetter(1), reverse = True)
maxIndex = 10

#print "len is ", len(sortedRecs)
#print sortedRecs

if len(sortedRecs) < 10:
	maxIndex = len(sortedRecs)

for i in range(0, maxIndex):
		print sortedRecs[i][0], "\t", sortedRecs[i][1]
