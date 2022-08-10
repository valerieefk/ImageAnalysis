# Clumsily opens a text file of data for the TXC and plots it. 

from datetime import datetime
from tabnanny import filename_only
from pytz import timezone
import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import griddata
import os


location = "C:/data/TXC_NSLS2_JUL2022/diamond2_areascan/" 
filename = "6_txconly.txt"
path = location + filename

print(path)

data = open(path)

image = np.fromfile(data, dtype=float, count=-1, sep=' ')


#print(image)
image2d = image.reshape(51,51) 

currimage = image2d * (1/33330000)   #convert from voltage to current in nA



plt.contourf(currimage)   # what type of plot?
plt.colorbar(label="current in A", orientation="vertical")   # intensity scale
plt.xlabel('horizontal pinhole position (0.1 micron steps)')
plt.ylabel('vertical pinhole position (0.1 micron steps)')
plt.title("detector 2: high gain, 1.678E-7 A total current")


plt.show()   # brings up the plot window 


print("you did it")