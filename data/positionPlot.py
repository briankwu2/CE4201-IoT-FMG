from typing import List
from matplotlib import pyplot as plt
from matplotlib import animation

from functions import * # import all functions from this fil

"""
Parse the input from position.csv
Ordered as a comma separated value (csv) file
Time is ordered as yyyy-mm-dd hh:mm:ss.ssssss (24hr-format)
Latitude is ordered as ll.l--- (cut it to 6 decimal pts)
    Latitude ranges from -90 to 90
Longitude is ordered as LL.L--- (cut it down to 6 decimal pts)
    Longitude ranges from -180 to 180

"""


data_file = 'position.csv'
Longitude = []
Latitude = []
Time = []

parseData(data_file, Time, Longitude, Latitude) #Parses Data into three lists
x_ticks = find_xticks(Longitude) #Finds the correct tick mark guides for x variable
y_ticks = find_yticks(Latitude) # Finds the correct tick mark guides for the y variable

fig, ax = plt.subplots()
ax.scatter(Longitude,Latitude,s=20) 
ax.set(xticks=x_ticks, yticks=y_ticks)
ax.ticklabel_format(useOffset=False, style='plain') # To disable scientific notation on axes
configPlot(Longitude, Latitude, ax)
plt.show()


