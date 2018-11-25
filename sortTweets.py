
import csv
import io
import re

formatted = []
nlist = []
plist = []
inputTuples=open('./out/part-00000', 'r')
outputFile=open('./FinalDictionary/negative.txt', 'a')
negative=open('negative.txt', 'r')
for line in negative:
        nlist.extend([line])
positive=open('positive.txt', 'r')
for line in positive:
        plist.extend([line])



for line in inputTuples:
        line = re.sub('[(\n)]', '', line)
        line = line[1:]
        formatted.extend([line])

formatted = sorted(formatted, key=lambda x: int(x.split(',')[1]))

for line in formatted[860:]:
        line = line.split(',')[0]
        line = re.sub('[\']', '', line)
        line = line.lower()
        if line+'\n' not in nlist:
                if line+'\n' not in plist:
                        outputFile.write(line + '\n')

outputFile.close()


