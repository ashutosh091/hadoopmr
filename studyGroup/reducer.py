#!/usr/bin/python

import sys
import operator

oldKey = None
authors = []

# Loop around the data; we are actually doing left outer join here of node with users.

for line in sys.stdin:

    data = line.split("\t")

    if len(data) < 2:
        continue

    thisKey = data[0].strip()
    thisAuthor = data[1].strip()

    # Set oldKey and houra when first record is encountered
    if oldKey == None:
        oldKey = thisKey

    # whenever the key is changing
    if oldKey != thisKey:
        print oldKey, "\t", authors
        # reset now
        oldKey = thisKey
        authors = []
        authors.append(thisAuthor)
    else:
        # when same key is being continued
        authors.append(thisAuthor)

# print last record
print oldKey, "\t", authors

