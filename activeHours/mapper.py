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
	author_id = line[3].strip()
	added_at = line[8].strip()
	# ensure that the id is valid number
	if nodeid.isdigit() == False:
		continue
	added_at = added_at[:added_at.rfind('+'):]
	hour = datetime.strptime(added_at, "%Y-%m-%d %H:%M:%S.%f").hour
	print author_id, "\t", hour




