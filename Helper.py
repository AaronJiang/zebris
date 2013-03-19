import os,csv

def readZebrisWalk(textfile):
	try: 
		f = open(textfile, 'r')
		lines = f.read().splitlines()
	except IOError as e:
		print "I/O error({0}): {1}".format(e.errno, e.strerror)

    #Read parameters	
	params = []
	paramindex = lines.index('[Parameters]')
	params.extend(lines[paramindex+1:paramindex+1+21])

	butterindex = lines.index('[Butterfly Parameters]')
	params.extend(lines[butterindex+1:butterindex+1+12])

	toeleftindex = lines.index('left force = {')
	params.extend(lines[toeleftindex+107:toeleftindex+107+4])

	toerightindex = lines.index('right force = {')
	params.extend(lines[toerightindex+106:toerightindex+106+4])

	row = []
	for param in params:
		param = param.split('\t')[1:]
		row.append(';'.join(param))

	#write result into csv
	resultFile = open("output.csv",'a')
	wr = csv.writer(resultFile, dialect='excel')
	wr.writerows([row])

def readZebrisStand(textfile):
	try: 
		f = open(textfile, 'r')
		lines = f.read().splitlines()
	except IOError as e:
		print "I/O error({0}): {1}".format(e.errno, e.strerror)

    #Read parameters	
	params = []
	paramindex = lines.index('Parameters')
	params.extend(lines[paramindex+2:paramindex+2+4])
	copindex = lines.index('[COP averaged]')
	params.extend(lines[copindex+1:copindex+1+7])

	row = []
	for param in params:
		param = param.split('\t')[1:]
		row.append(';'.join(param))

	#write result into csv
	resultFile = open("output.csv",'a')
	wr = csv.writer(resultFile, dialect='excel')
	wr.writerows([row])	

def getFloderData(folder):
	txtfiles = []
	for files in os.listdir(folder):
	    if files.endswith(".txt"):
	        txtfiles.append(files)
	
	return txtfiles	           

	        	