# By: Brendan Luke
# Date: February 10, 2022
# Scope: plot DEM's from interpreted text files
from datetime import datetime

from matplotlib.colors import Colormap
startTime = datetime.now()

# Libraries:
import os
dirname = os.path.dirname(__file__) # relative filepaths
import numpy as np
import matplotlib.pyplot as plt
import textwrap

# User Inputs:
txtFileName = 'testPy2.txt' # filename of .txt Output file
LINES = 720 # rows of data, take from PDS label
LINE_SAMPLES = 1440 # columns per row, take from PDS label
SAMPLE_BITS = 16 # number of bits per DN sample, take from PDS label
SIGNED = True # is data signed of unsigned, interpret from PDS label
chunk_size = int(SAMPLE_BITS*LINE_SAMPLES/8) # blocksize (bytes) of data buffer (one line at a time)

# Functions:
def processLine(lineStr,dataArray,row,SAMPLE_BITS,twosCompFactor,scaleFactor):
    # function to process the line into the dataArray
    tempList = textwrap.wrap(lineStr,4)
    col = 0
    for x in tempList:
        tempStr = x[2]+x[3]+x[0]+x[1]  # reverse byte order because data is LSB(yte)_INTEGER
        if int('0x'+tempStr,base=16) >= twosCompFactor:
            datum = int('0x'+tempStr,base=16) - 2**SAMPLE_BITS
        else:
            datum = int('0x'+tempStr,base=16)
        dataArray[row][col] = datum/scaleFactor
        col += 1
    return dataArray

# Script:
scaleFactor = 2
dataArray = np.empty((LINES, LINE_SAMPLES),np.short) # pre-allocate image array (16-bit signed)

if SIGNED:
    twosCompFactor = 2**(SAMPLE_BITS-1)
else:
    twosCompFactor = 0

row = 0
with open(dirname + '/' + txtFileName) as file:
    while line := file.readline():
        dataArray = processLine(line,dataArray,row,SAMPLE_BITS,twosCompFactor,scaleFactor)
        row += 1
latitude = np.linspace(90,-90,LINES) # flips image vertically to north up view
longitude = np.linspace(0,360,LINE_SAMPLES)

# Plotting:
fig1, ax1 = plt.subplots(constrained_layout=True)
CS = plt.contourf(longitude,latitude,dataArray,levels=50,cmap=plt.cm.bone)
ax1.set_title('LDEM_4 LOLA DEM')
ax1.set_ylabel('Latitude (°)')
ax1.set_xlabel('Longitude (°)')
ax1.set_aspect('equal', 'box')
cbar = fig1.colorbar(CS)
cbar.ax.set_ylabel('Elevation (m)')

# Stop Clock
print('Done! Execution took ' + str(datetime.now() - startTime))

# Show Plots
plt.show()