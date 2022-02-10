# By: Brendan Luke
# Date: February 10, 2022
# Scope: plot DEM's from interpreted text files
from datetime import datetime
startTime = datetime.now()

# Libraries:
import os
dirname = os.path.dirname(__file__) # relative filepaths
import math
import numpy as np
import matplotlib.pyplot as plt
import binascii

# User Inputs:
txtFileName = 'testPy2.txt' # filename of .txt Output file
LINES = 720 # rows of data, take from PDS label
LINE_SAMPLES = 1440 # columns per row, take from PDS label
SAMPLE_BITS = 16 # number of bits per DN sample, take from PDS label
chunk_size = int(SAMPLE_BITS*LINE_SAMPLES/8) # blocksize (bytes) of data buffer (one line at a time)

# Functions:
def processLine(lineStr,LINE_SAMPLES,dataArray,row,SAMPLE_BITS):
    # function to process the line into the dataArray
    tempList = lineStr.split(LINE_SAMPLES-1)
    col = 0
    scaleFactor = int(SAMPLE_BITS/(2**SAMPLE_BYTES))
    for x in tempList:
        dataArray[row][col] = np.ubyte(int("0x"+x)/scaleFactor) # scale pixel data to 8 bits unsigned
        col += 1
    return dataArray


# Script:
dataArray = np.empty((LINES, LINE_SAMPLES),np.ubyte) # pre-allocate image array (8-bit unsigned)

with open(dirname + '/' + txtFileName) as file:
    while line := file.readline():
        print(line.rstrip())



# Stop Clock
print('Done! Execution took ' + str(datetime.now() - startTime))