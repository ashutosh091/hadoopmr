#!/usr/bin/python
import sys
import csv
from datetime import datetime
from datetime import timedelta

previous_day = datetime.now() - timedelta(days=1)
#print previous_day
reader = csv.reader(sys.stdin, delimiter='\t', quoting = csv.QUOTE_MINIMAL)

for line in reader:

	# YOUR CODE HERE
	if len(line) < 5:
		continue

	# Nodes file
	nodeid = line[0].strip()
	author_id = line[3].strip()
	last_active_dt = line[13].strip()
	# ensure that the id is valid number
	if nodeid.isdigit() == False:
		continue
	last_active_dt = last_active_dt[:last_active_dt.rfind('+'):]
	lastActive = datetime.strptime(last_active_dt, "%Y-%m-%d %H:%M:%S.%f")
	# print only those which are active	
	if lastActive >= previous_day:
		print nodeid




