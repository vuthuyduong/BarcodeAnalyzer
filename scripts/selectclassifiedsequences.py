#!/usr/bin/env python
# FILE: selectclassifiedsequences.py
# AUTHOR: Duong Vu
# CREATE DATE: 07 June 2019
#select sequences that have a taxonname at a given classification position
import sys
import numpy as np
import os
from Bio import SeqIO
import json
import multiprocessing
nproc=multiprocessing.cpu_count()
#from keras.utils import np_utils


fastafilename=sys.argv[1]
classificationfilename = sys.argv[2]
classificationpos = int(sys.argv[3])
output=sys.argv[4]

def GetBase(filename):
	return filename[:-(len(filename)-filename.rindex("."))]

def SelectSeqIds(classificationfilename,classificationpos):
	classificationfile= list(open(classificationfilename, "r"))
	seqids=[]
	for line in classificationfile:
		elements=line.rstrip().split("\t")
		seqid = elements[0].replace(">","").rstrip()
		if classificationpos < len(elements):
			taxonname=elements[classificationpos]
			if taxonname !="":
				seqids.append(seqid)		
	return seqids

#####main###
seqids=SelectSeqIds(classificationfilename,classificationpos)
seqrecords=list(SeqIO.parse(fastafilename, "fasta"))
selectedrecords=[]
for seqrec in seqrecords:
	if seqrec.id in seqids:
		selectedrecords.append(seqrec)
#save to file:
SeqIO.write(selectedrecords,output,"fasta")

