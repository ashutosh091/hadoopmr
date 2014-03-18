#!/usr/bin/python

import sys

totalCount = 0
oldKey = None
index = []
snippets = []

# Loop around the data

for line in sys.stdin:
    data = line.strip().split("\t")

    if len(data) != 3:
        continue;

    thisKey = data[0]
    nodeId = data[1].strip()
    snippet = data[2]

    if oldKey == None:
	    oldKey = thisKey

    if oldKey != thisKey:
		print oldKey, "\t", totalCount,"\t", set(index), "\t", snippets
		totalCount = 1
		oldKey = thisKey
		index = []
		index.append(nodeId)
		snippets = []
		snippets.append(snippet)
    else:
		totalCount += 1
		index.append(nodeId)
		snippets.append(snippet)

if oldKey != None:
    print oldKey, "\t", totalCount, "\t", set(index), "\t", snippets

