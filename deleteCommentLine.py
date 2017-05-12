#Given a path and word,

import os
import glob

path = './test/'
list1 = os.listdir(path)

wordToDelete=raw_input("Enter a word you want to delete: ")

sizeWord=len(wordToDelete)
for infile in list1:
	print("current file is: " +infile)
	inputfile =file(path + infile,'r')
	(PATH, FILENAME) = os.path.split(infile)
	(Name, Extension) = os.path.splitext(FILENAME)
	outFName = path+Name+'output'+'.txt'
	outputFile=open(outFName,'w')
	for line in inputfile:
		firstWord=line[0:sizeWord]
		if firstWord == wordToDelete:
			print("This was deleted: " + line)
			outputFile.write(line[2:len(line)])
		else:
			outputFile.write(line)
inputfile.close()
outputFile.close()
#raw_input()
