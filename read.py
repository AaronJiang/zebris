import csv, os

txtfiles = []
for files in os.listdir("./zebris_walk"):
    if files.endswith(".txt"):
        txtfiles.append(files)

os.chdir("./zebris_walk")
for textfile in txtfiles:
	f = open(textfile, 'r')
	lines = f.read().splitlines()
	params = []

	#Read parameters
	paramindex = lines.index('[Parameters]')
	params.extend(lines[paramindex+1:paramindex+1+21])
	butterindex = lines.index('[Butterfly Parameters]')
	params.extend(lines[butterindex+1:butterindex+1+12])
	toeleftindex = lines.index('left force = {')
	params.extend(lines[toeleftindex+106:toeleftindex+106+4])
	toerightindex = lines.index('right force = {')
	params.extend(lines[toerightindex+106:toerightindex+106+4])

	row = []
	for param in params:
		param = param[param.find('\t')+1:]
		row.append(param)

	#write result into csv
	row = [row]
	resultFile = open("output.csv",'a')
	wr = csv.writer(resultFile, dialect='excel')
	wr.writerows(row)
os.chdir("../")


txtfiles = []
for files in os.listdir("./zebris_stand"):
    if files.endswith(".txt"):
        txtfiles.append(files)

print txtfiles

os.chdir("./zebris_stand")
for textfile in txtfiles:
	f = open(textfile, 'r')
	lines = f.read().splitlines()
	params = []

	#Read parameters
	paramindex = lines.index('Parameters')
	params.extend(lines[paramindex+2:paramindex+2+4])
	copindex = lines.index('[COP averaged]')
	params.extend(lines[copindex+1:copindex+1+7])

	row = []
	for param in params:
		param = param[param.find('\t')+1:]
		row.append(param)

	#write result into csv
	row = [row]
	resultFile = open("output.csv",'a')
	wr = csv.writer(resultFile, dialect='excel')
	wr.writerows(row)
os.chdir("../")