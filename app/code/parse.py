import sys
import csv

fp = sys.argv[1]

lineArr = list()

with open(fp, "r") as f:
	next(f)
	for line in f:
		lineArr.append(line.strip().split(","))
f.close()

for i in lineArr:
	del i[1]
	del i[1]
	del i[1]
	del i[1]

with open("dataout.csv", "w") as out:
	for i in lineArr:
		a = i[:3]
		#print int(round(float(a[2][1:len(a[2])-1])))
		out.write(str(a)[1:len(str(a))-1]+"\n")
out.close()
