#!/usr/bin/python

import sys
import operator

oldKey = None
hours = {}

# Loop around the data; we are actually doing left outer join here of node with users.

for line in sys.stdin:

    data = line.split("\t")

    if len(data) < 2:
        continue
    
    thisHour = data[1].strip()
    thisKey = data[0].strip()

    # Set oldKey and houra when first record is encountered
    if oldKey == None:
		oldKey = thisKey
		hours.clear()

    # whenever the key is changing
    if oldKey != thisKey: 
	# print student's most active hour(s)
	sortedHours = sorted(hours.iteritems(), key = operator.itemgetter(1), reverse = True)
	maxCount = -1
	for hr in sortedHours:
		if hr[1] >= maxCount:
			maxCount = hr[1]
			print oldKey, hr[0]
	# reset now
	oldKey = thisKey
        hours.clear()
 	hours[thisHour] = 1

    else:
        # when same key is being continued
	# if hour field changes
	if thisHour in hours:
		hours[thisHour] = hours[thisHour] + 1
	else:
		hours[thisHour] = 1


# print student's most active hour(s)
sortedHours = sorted(hours.iteritems(), key = operator.itemgetter(1), reverse = True)
maxCount = -1
for hr in sortedHours:
	if hr[1] >= maxCount:
		maxCount = hr[1]
		print oldKey, hr[0]
