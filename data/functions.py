import numpy as np
from matplotlib import pyplot as plt
from matplotlib import animation
from functions import *
import time

def find_xticks(xList):
    """Function that lists 10 tick marks that are of appropriate range of the x-axis list"""
    maxVal = np.amax(xList)
    minVal = np.amin(xList)
    range = maxVal - minVal
    return np.linspace(minVal, maxVal, num=10) # Returns a 10 tick marks according to the range

def find_yticks(yList):
    """Function that lists 10 tick marks that are of appropriate range of the x-axis list"""
    maxVal = np.amax(yList)
    minVal = np.amin(yList)
    range = maxVal - minVal
    return np.linspace(minVal, maxVal, num=10) # Returns a 10 tick marks according to the range

def parseData(data_file, Time, Longitude, Latitude):
    try:
        with open(data_file,'r') as df:
            lines = df.readlines()
            for line in lines[1:]: # Starts at index '1' to skip the title row
                splitString = line.split(',') # Splits the csv into each row at a time
                Time.append(splitString[0][:20].rstrip()) # Appends the time column into the Time list
                Latitude.append(float(splitString[1].rstrip())) # Appends the latitude column into Latitude list
                Longitude.append(float(splitString[2].rstrip())) # Appends the longitude column into the Longitude list
    except FileNotFoundError:
        print("File not found")

def conv_GPSTime_to_ctime(Time):
    """Parses a time of the format
    2022-09-09 11:39:16
    YYYY-MM-DD HH:mm:ss
    to seconds before the epoch
    """
    Time = Time[0:20] # Truncates the decimal point of seconds
    structTime = time.strptime("2022-09-09 11:39:16", "%Y-%m-%d %H:%M:%S") #Converts the time of this format into a struct_time structure.
    epochTime = time.mktime(structTime) # Converts time to seconds since the epoch.
    return epochTime

def configPlot(Longitude, Latitude,ax):
    x_ticks = find_xticks(Longitude) #Finds the correct tick mark guides for x variable
    y_ticks = find_yticks(Latitude) # Finds the correct tick mark guides for the y variable
    ax.set_xticks(x_ticks)
    ax.set_yticks(y_ticks)
    ax.set_xlim(np.amin(Longitude), np.amax(Longitude))
    ax.set_ylim(np.amin(Latitude),np.amax(Latitude))
    plt.title("Location Plot of Walking on UTD Campus")
    plt.ylabel("Latitude", fontsize=10)
    plt.xlabel("Longitude", fontsize=10)
    



