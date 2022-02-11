# By: Brendan Luke
# Date: February 9, 2022
# Scope: interpret PDS DEM's from RDRs
from datetime import datetime
startTime = datetime.now()

# Libraries:
import os
dirname = os.path.dirname(__file__) # relative filepaths

# User Inputs:
imgFileName = 'ldem_4.img' # filename of .img PDS DEM file
txtOutFileName = 'testPy2.txt' # filename of .txt Output file
LINES = 720 # rows of data, take from PDS label
LINE_SAMPLES = 1440 # columns per row, take from PDS label
SAMPLE_BITS = 16 # number of bits per DN sample, take from PDS label
chunk_size = int(SAMPLE_BITS*LINE_SAMPLES/8) # blocksize (bytes) of data buffer (one line at a time)

# Functions:
def read_in_chunks(file_object, chunk_size):
    # read data from file in chunks
    while True:
        data = file_object.read(chunk_size)
        if not data:
            break
        yield data

def write_chunk(file_object,datachunk,endLine):
    # write chunk to text file, carraige return if last sample in line
    if endLine:
        file_object.write(datachunk + '\n')#,'a')
    else:
        file_object.write(datachunk)#),'a')

# Script:
f = open(dirname + '/' + imgFileName,'rb') # open file
f_out = open(dirname + '/' + txtOutFileName,'a') # open file
for datachunk in read_in_chunks(f,chunk_size):
    #write_chunk(f_out,str(binascii.hexlify(datachunk)),True)
    write_chunk(f_out,str(datachunk.hex()),True)
f.close()

# Stop Clock
print('Done! Execution took ' + str(datetime.now() - startTime))