#!/usr/bin/python
import sys
import csv
from datetime import datetime

reader = csv.reader(sys.stdin, delimiter='\t', quoting = csv.QUOTE_MINIMAL)

for line in reader:

	# YOUR CODE HERE
	if len(line) < 5:
		continue

	# Nodes file
	nodeid = line[0].strip()
	authorId = line[3].strip()
	node_type = line[5].strip()
	absParentId = line[7].strip()
	# ensure that the id is valid number
	if nodeid.isdigit() == False:
		continue
	if node_type == 'question':
		print nodeid, "\t", authorId
	else:
		print absParentId, "\t", authorId




