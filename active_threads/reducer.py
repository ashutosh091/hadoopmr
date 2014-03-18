#!/usr/bin/python

import sys
import operator

oldKey = None

# Loop around the data; we are actually doing left outer join here of node with users.

for line in sys.stdin:

    thisKey = line.strip()

    # Set oldKey and houra when first record is encountered
    if oldKey == None:
		oldKey = thisKey

    # whenever the key is changing
    if oldKey != thisKey: 
	# print node id
	print oldKey

	# reset now
	oldKey = thisKey

print oldKey
