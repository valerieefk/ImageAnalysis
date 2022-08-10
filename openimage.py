# Created vefk 08/01/22
# Program to load in image files

from datetime import datetime
from tabnanny import filename_only
from pytz import timezone
import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import griddata
import os

# where is your data? 
path = "C:/data/TXC_NSLS2_JUL2022/diamond1_images/"
filename = "post_16mA_longtest_low_6fps.raw"
file = path + filename
print(file)

# TXC file type
dt = np.dtype('int32')
data = np.fromfile(file, dtype = dt)
dSize = np.size(data)
imageTotal = int(dSize / 1024)

# some information about the image stack 
print ('Total # images')
print(imageTotal)
print ("the total average of all data") 
totalframeAvg = np.average(data)   #this prints the average value of every unit in the array
print (totalframeAvg)
frameAvg = np.array(1)
print(range(imageTotal))

# which image do you want to display?
i = 1
imStart = (i-1)*1024
imEnd = i * 1024

# convert the data into a 2D array to display 
image = data[imStart:imEnd]
data2d = image.reshape(32,32)
flipped = np.flip(data2d, 0) # TXC data opens upside down without this step in this import method
currimage = flipped * 0.0000608  #60.8 nA/ADU in low gain

# dispaly that sweet sweet data 
plt.contourf(currimage)   # what type of plot? also applies the flip.
plt.colorbar(label="current in mA", orientation="vertical")   # intensity scale
plt.xlabel('horizontal pixel number')
plt.ylabel('vertical pixel number')
plt.title(filename)


plt.show()   # brings up the plot window 


