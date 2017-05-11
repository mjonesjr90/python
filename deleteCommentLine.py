import os
import glob

path = 'H:\\Python Code\\3D_Canal\\'
list1 = os.listdir(path)

wordToDelete=raw_input('Enter Word to What You Want to Delete:')

sizeWord=len(wordToDelete)
for infile in list1:
	print "current file is: " +infile
	inputfile =file(path + infile,'r')
	(PATH, FILENAME) = os.path.split(infile)
	(Name, Extension) = os.path.splitext(FILENAME)
	outFName = 'H:\\Python Code\\New\\'+Name+'output'+'.txt'
	outputFile=open(outFName,'w')
	for line in inputfile:
		firstWord=line[0:sizeWord]
		if firstWord == wordToDelete:
			print("This was deleted" + line)
			outputFile.write(line[2:len(line)])
		else:
			outputFile.write(line)
inputfile.close()
outputFile.close()
raw_input()

