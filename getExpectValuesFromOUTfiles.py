import re
import sys
from os import listdir
from os.path import isfile, join

OUTfolder = sys.argv[1]

#make list of paths to each OUT file
outlist = [f for f in listdir(OUTfolder) if isfile(join(OUTfolder,f))]

#make output file
resultsfile = open('C:\\expectValuesFromOUTs.txt', 'w')

#construct RE for line describing top scoring MASCOT hit. Example below:
#  1.   1 / ##        N/A 1361.55552  0.0000   27.34   0.824   4/20  sp|P49840|GSK3A_HUMAN| +3  R.GEPNVSYICS*R.Y
p = re.compile('^\s{2}1\.\s+[0-9]\s*/\s*.*\s+[\-0-9.]+\s+[\-0-9.]+\s+[\-0-9.]+\s+([\-0-9.]+)\s')

for out in outlist:
	#Get identifying metadata from out file name EDIT: not needed, can just match OUT name to Peptide Depot field "filename import"
	# parsedfname = out.split("]")
	# fname = parsedfname[0]
	# scan = parsedfname[1]
	# charge = parsedfname[3][:1]
	
	#open and parse each out file to get the expect value
	outpath = join(OUTfolder,out)
	with open(outpath) as f:
		#scan each line until you find a match to the RE describing the first line 
		for line in f:
			m = p.match(line)
			#when a hit is found, the expect value is captured in m.group(1)
			if m:
				print(line)
				print('Match found: ' + m.group(1))
				expect = m.group(1)
				break
			else:
				continue
	resultsfile.write(out + '\t' + expect + '\n')

resultsfile.close()
