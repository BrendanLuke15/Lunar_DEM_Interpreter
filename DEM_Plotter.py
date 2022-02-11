# By: Brendan Luke
# Date: February 10, 2022
# Scope: plot DEM's from interpreted text files
from datetime import datetime

from matplotlib.colors import Colormap
startTime = datetime.now()

# Libraries:
import os
dirname = os.path.dirname(__file__) # relative filepaths
import math
import numpy as np
import matplotlib.pyplot as plt
import textwrap

# User Inputs:
txtFileName = 'testPy2.txt' # filename of .txt Output file
LINES = 720 # rows of data, take from PDS label
LINE_SAMPLES = 1440 # columns per row, take from PDS label
SAMPLE_BITS = 16 # number of bits per DN sample, take from PDS label
chunk_size = int(SAMPLE_BITS*LINE_SAMPLES/8) # blocksize (bytes) of data buffer (one line at a time)

# Functions:
def processLine(lineStr,LINE_SAMPLES,dataArray,row,SAMPLE_BITS):
    # function to process the line into the dataArray
    tempList = textwrap.wrap(lineStr,4)
    col = 0
    scaleFactor = int((2**SAMPLE_BITS)/(2**(SAMPLE_BITS-8)))
    for x in tempList:
        tempStr = x [::-1]
        dataArray[row][col] = np.byte(int("0x"+str(tempStr),base=16)/scaleFactor) # scale pixel data to 8 bits unsigned
        #dataArray[row][col] = np.short(int("0x"+str(tempStr),base=16)) # scale pixel data to 16 bits unsigned
        col += 1
    return dataArray

# Script:
dataArray = np.empty((LINES, LINE_SAMPLES),np.byte) # pre-allocate image array (8-bit unsigned)
#dataArray = np.empty((LINES, LINE_SAMPLES),np.short) # pre-allocate image array (16-bit unsigned)
row = 0
with open(dirname + '/' + txtFileName) as file:
    while line := file.readline():
        dataArray = processLine(line,LINE_SAMPLES,dataArray,row,SAMPLE_BITS)
        row += 1

plt.contourf(dataArray,cmap=plt.cm.bone)
plt.xlim((0,LINE_SAMPLES))
plt.ylim((0,LINES))

print(np.amax(dataArray))
print(np.amin(dataArray))

# Stop Clock
print('Done! Execution took ' + str(datetime.now() - startTime))

# Show Plots
plt.show()