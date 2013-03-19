"""
Read Zebris txt data from target folder
and save into output.csv

@aaron, 2013-03-19
"""
import Helper, os

walkfiles = Helper.getFloderData("./zebris_walk")

if walkfiles != '':
	os.chdir("./zebris_walk")
	for walkfile in walkfiles:
		Helper.readZebrisWalk(walkfile)
	os.chdir("../")
else:
	print 'no walk data'	

standfiles = Helper.getFloderData("./zebris_stand")
if standfiles != '':
	os.chdir("./zebris_walk")
	for walkfile in walkfiles:
		Helper.readZebrisWalk(walkfile)
	os.chdir("../")
else:
	print 'no stand data'