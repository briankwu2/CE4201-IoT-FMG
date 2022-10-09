# Import all the required modules
import numpy as np
from matplotlib import pyplot as plt
from matplotlib import animation
from functions import *
import time

data_file = 'position.csv'
Longitude = []
Latitude = []
Time = []

fig, ax= plt.subplots()
parseData(data_file, Time, Longitude, Latitude) # Parses Data into three lists.
configPlot(Longitude,Latitude,ax) # Configures all the plot settings

line, = ax.plot(Longitude[0],Latitude[0]) # Creates a empty base plot
numDataPoints = len(Longitude)

def animate_func(num):
    line.set_xdata(Longitude[:num])
    line.set_ydata(Latitude[:num])
    return line,

anim = animation.FuncAnimation(fig, func=animate_func,frames=numDataPoints, interval=100)
writergif = animation.PillowWriter(fps=numDataPoints/5)
anim.save("timePlot.gif",writer=writergif)


plt.show()




    



    
    