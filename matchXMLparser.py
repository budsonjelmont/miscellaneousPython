#! /usr/bin/python

# Performs SAX parsing of an InterPRO XML describing all the motif/domain annotations
# assigned to a queried amino acid sequence and prints them out to a tab-delimited txt
# file.

import sys
try:
	import xml.etree.cElementTree as etree
except ImportError:
	import xml.etree.ElementTree as etree

xmL = sys.argv[1]
print(xmL)

f = open('InterPRO_matches_parsed.txt','w')

#for event, elem in etree.iterparse(xmL, events=('start', 'end', 'start-ns', 'end-ns')):
for event, elem in etree.iterparse(xmL, events=('start', 'end')):
	if event == 'start':
		if elem.tag == 'protein':
			protID = elem.get('id')
			protName = elem.get('name')
			length = elem.get('length')
			print(protID)
			elem.clear()
		elif elem.tag == 'match':
			matchName = elem.get('name')
			matchID = elem.get('id')
			db = elem.get('dbname')
			evd = elem.get('evd')
			elem.clear()
		elif elem.tag == 'lcn':
			start = elem.get('start')
			end = elem.get('end')
			score = elem.get('score')
			elem.clear()
		elif elem.tag == 'ipr':
			IPRid = elem.get('id')
			IPRname = elem.get('name')
			IPRtype = elem.get('type')
			elem.clear()
	if event == 'end':
		if elem.tag == 'match':
			f.write(IPRid + '\t' + IPRname + '\t' + IPRtype + '\t' + matchID + '\t' + matchName + '\t' + protID + '\t' + protName + '\t' + length + '\t' + start + '\t' + end + '\t' + score + '\t' + db + '\t' + evd + '\n')
			elem.clear()
		elif elem.tag == 'protein':
			elem.clear()
		elif elem.tag == 'lcn':
			elem.clear()
		elif elem.tag == 'ipr':
			elem.clear()
f.close()