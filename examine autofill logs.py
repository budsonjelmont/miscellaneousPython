from os import listdir
from os.path import isfile, join
import csv

logfolderpath = 'C:/Users/superuser/Documents/AutoFillLogs'

logfiles = [f for f in listdir(logfolderpath) if isfile(join(logfolderpath, f))]

for log in logfiles:
	with open(join(logfolderpath, log), 'r') as f:
		reader = csv.reader(f, delimiter = '\t')
		# reads entire file into a list of lists
		d = list(reader)
		# check only row 2 to see if first element is blank
		print(d[2][0])
		if d[2][0] == '0':
			print(log)
		# for row in reader:
			# if row[5]=='':
				# print(log)
				# print(row[20])
