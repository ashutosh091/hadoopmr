#!/usr/bin/python
import sys
import csv
import re

reader = csv.reader(sys.stdin, delimiter='\t', quoting = csv.QUOTE_MINIMAL)
for line in reader:

	# YOUR CODE HERE
	#print len(line)
	if len(line) < 5:
		continue
	data = line[4].strip()
	nodeId = line[0].strip()

	nodeId = nodeId.replace('"','')
	if nodeId.isdigit() == False:
		#print nodeId
		continue
	#print data
	#|.|!|\?|(|)|<|>|[|]|#|$|=|-|/
	tokens = re.compile('\s+|!|\.|\?|\(|\)|<|>|\[|\]|#|\$|=|-|/|:|;|"|,').split(data)
	#print tokens

	for token in tokens:
		if token.strip() != '':
			index = data.find(token)
			# start from 20 chars before token till 50 chars after token
			startIndex = index - 20
			endIndex = index + 50
			if startIndex < 0:
				startIndex = 0
			if endIndex > len(data):
				endIndex = len(data)
			print token.lower(),"\t",nodeId, "\t", data[startIndex:endIndex] 

#writer.writerow(line)



