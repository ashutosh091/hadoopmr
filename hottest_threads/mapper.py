#!/usr/bin/python
import sys
import csv

reader = csv.reader(sys.stdin, delimiter='\t', quoting = csv.QUOTE_MINIMAL)

for line in reader:

	# YOUR CODE HERE
	if len(line) < 7:
		continue

	# Nodes file
	nodeid = line[0].strip()
	node_type = line[5].strip()
	parent_id = line[7].strip()
	# ensure that the id is valid number
	if nodeid.isdigit() == False:
		continue
	if node_type != 'question':
		print parent_id





