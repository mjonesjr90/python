#This code creates text files containing data
#Change numOfFiles to change number of files created



word="//x,y,z"
numOfFiles = 12
    
for z in range(1,numOfFiles):
	outFName = 'File'+str(z)+'.txt'
	outF=open(outFName,'w')
	
	for i in range(1,401):
		line="";
		if(i==1):
			line=word+" " +"\n"
			print(outFName)
		else:
			line="Line: "+str(i)+"\n"
		outF.write(line)
	outF.close()

raw_input()
raw_input()
