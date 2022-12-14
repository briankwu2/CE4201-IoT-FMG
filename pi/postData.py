import requests



# sends to server the new data
# should run every minute

SERVER_URL =   "http://127.0.0.1:5000/"
OUTPUTFILE_POS = "/home/pi/CE4201-IoT-FMG/pi/output/position.csv"
OUTPUTFILE_BPM = "/home/pi/CE4201-IoT-FMG/pi/output/bpm_data.csv"
def getPosData():
    # returns array of lat and log
    try:
        f = open(OUTPUTFILE_POS,"r")
        lastLine:str = f.readlines()[-1] # gets the last line
        data = lastLine.split(",") # date, lat, log
        return data[1:] # returns from the first one to the last one
    except:
        print("Error opening file")
    pass

def getBpmData():
    # returns bpm and time 
    # should use mike's algorthim to figroue otu what bpm to pump out
    try:
        f = open(OUTPUTFILE_BPM, "r")
        # use algorthim he has
        # temp algorthim only gets the last one
        lastLine:str = f.readlines()[-1] # gets the last line
        data = lastLine.split(",") # unix time, bpm, SpO2
        return data[:1] # returns up to the bpm
    except:
        print("unable to find bpm file")
    pass


def sendData():
    # sends the data to the server
    
    posData = getPosData()
    bpmData = getBpmData()
    gp_data = {'grandpaID': 'miguel123','bpm': bpmData[1], 'lat': posData[0], 'log': posData[1], 'time': bpmData[0]}
    print(gp_data)
    pass


sendData()


