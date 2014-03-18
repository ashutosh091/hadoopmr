#!/usr/bin/python

import sys
import operator

oldKey = None
maxCount = 0
hotCount = 10 # this can be set to 100 for checking if 100 replies/ comments are there, I am just using 10 for ease

# Loop around the data; we are actually doing left outer join here of node with users.

for line in sys.stdin:

    thisKey = line.strip()

    # Set oldKey and houra when first record is encountered
    if oldKey == None:
		oldKey = thisKey

    # whenever the key is changing
    if oldKey != thisKey: 
	# check hot count
	if maxCount >= hotCount:
		print oldKey
	# reset now
	oldKey = thisKey
        maxCount = 1

    else:
        # when same key is being continued
	maxCount += 1

# check hot count
if maxCount >= hotCount:
	print oldKey

