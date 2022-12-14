from turtle import pos
import serial               #import serial pacakge
from time import sleep
import webbrowser           #import package for opening link in browser
import sys                  #import system package
import datetime
import os


OUTPUT_FILE_PATH = "/home/pi/output/position.csv"

def GPS_Info():
    global NMEA_buff
    global lat_in_degrees
    global long_in_degrees
    nmea_time = []
    nmea_latitude = []
    nmea_longitude = []
    nmea_time = NMEA_buff[0]                    #extract time from GPGGA string
    nmea_latitude = NMEA_buff[1]                #extract latitude from GPGGA string
    nmea_latDirection = NMEA_buff[2]            # direction of lat
    nmea_longitude = NMEA_buff[3]               #extract longitude from GPGGA string
    nmea_longDirection = NMEA_buff[4]           # directio nof lon
    
    print("NMEA Time: ", nmea_time,'\n')
    print ("NMEA Latitude:", nmea_latitude,"NMEA Longitude:", nmea_longitude,'\n')
    
    lat = float(nmea_latitude)                  #convert string into float for calculation
    longi = float(nmea_longitude)               #convertr string into float for calculation
    if(nmea_latDirection == "S"):
        lat_in_degrees = convert_to_degrees(lat,True)    #get latitude in degree decimal format
    else:
        lat_in_degrees = convert_to_degrees(lat,False)    #get latitude in degree decimal format
    print("long direction: " + nmea_longDirection)
    if(nmea_longDirection == "W"):
        print("negative")
        long_in_degrees = convert_to_degrees(longi,True) #get longitude in degree decimal format
    else:
        print("positive")
        long_in_degrees = convert_to_degrees(longi,False) #get longitude in degree decimal format
    
#convert raw NMEA string into degree decimal format   
def convert_to_degrees(raw_value,isWorS):
    decimal_value = raw_value/100.00
    degrees = int(decimal_value)
    # if(isWorS):
    
    #     mm_mmmm = -1*(decimal_value - int(decimal_value))/0.6
        
    # else:

    mm_mmmm = (decimal_value - int(decimal_value))/0.6
    if(isWorS==True):
        position = -1*(degrees + mm_mmmm)
    else:
        position = degrees + mm_mmmm
    #position = "%.4f" %(position)
    return position
    

def writeToFile(lat,lon):
    f.write(str(datetime.datetime.now())+ "," + str(lat) + "," + str(lon) + "\n")
    pass

f = open(OUTPUT_FILE_PATH,'a')

gpgga_info = "$GPGGA,"
ser = serial.Serial ("/dev/ttyAMA0")              #Open port with baud rate
GPGGA_buffer = 0
NMEA_buff = 0
lat_in_degrees = 0
long_in_degrees = 0

try:
    if (os.path.isfile(OUTPUT_FILE_PATH) == False):
        f.write("date,lat,lon\n")
    i = 0
    while True:
        i += 1
        if(i >= 400000):
            sys.exit(0)
        if(i % 10000 == 0):
            received_data = (str)(ser.readline())                   #read NMEA string received
            GPGGA_data_available = received_data.find(gpgga_info)   #check for NMEA GPGGA string                 
            if (GPGGA_data_available>0):
                GPGGA_buffer = received_data.split("$GPGGA,",1)[1]  #store data coming after "$GPGGA," string 
                NMEA_buff = (GPGGA_buffer.split(','))               #store comma separated data in buffer
                GPS_Info()                                          #get time, latitude, longitude
    
                print("lat in degrees:", lat_in_degrees," long in degree: ", long_in_degrees, '\n')
                writeToFile(lat_in_degrees,long_in_degrees)
                #map_link = 'http://maps.google.com/?q=' + lat_in_degrees + ',' + long_in_degrees    #create link to plot location on Google map
                #print("<<<<<<<<press ctrl+c to plot location on google maps>>>>>>\n")               #press ctrl+c to plot on map and exit 
                print("------------------------------------------------------------\n")
                        
except KeyboardInterrupt:
    #webbrowser.open(map_link)        #open current position information in google map
    f.close()
    sys.exit(0)