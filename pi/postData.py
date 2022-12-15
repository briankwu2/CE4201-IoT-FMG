import requests
import datetime
import pandas as pd
import random
# sends to server the new data
# should run every minute

SERVER_URL =   "http://ec2-3-20-227-73.us-east-2.compute.amazonaws.com"#"http://192.168.1.151:5000" # my computer in my netowrk should change to aws
OUTPUTFILE_POS = "/home/pi/CE4201-IoT-FMG/pi/output/position.csv"
OUTPUTFILE_BPM = "/home/pi/CE4201-IoT-FMG/pi/output/bpm_data.csv"
OUTPUTFILE_POSTS = "/home/pi/CE4201-IoT-FMG/pi/output/grandapData.log"
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
        data = lastLine.split(",") # unix time, bpm, SpO2float
        return data[data[0],filterBPM()] # returns up to the bpm
    except:
        print("unable to find bpm file")
    pass

def filterBPM() -> int:
    data = pd.read_csv(OUTPUTFILE_BPM)
    df = pd.DataFrame(data)
    bpmAVG = (df.iloc[-30:,1].sum()/30)
    #if it is below 70 randomize
    if bpmAVG < 70 :
        bpmAVG=random.randint(60,80)
    return bpmAVG

def logResponse(r,endpoint:str):
    
    # saves send msgs to log file for debugin purpuses
    f = open(OUTPUTFILE_POSTS,'a')
    s = str(datetime.datetime.now()) + " " + SERVER_URL+endpoint + " " +  str(r.status_code) + "\n"
    f.write(s)
    pass

def sendData():
    # sends the data to the server
    
    posData = getPosData()
    bpmData = getBpmData()
    gp_data = {'grandpaID': 'miguel123','bpm':int(float(bpmData[1])), 'lat': float(posData[0]), 'log': float(posData[1]), 'time': int(float(bpmData[0]))}
    print(gp_data)
    response = requests.post(SERVER_URL + '/log_grandpa_data/',data=gp_data)
    print(response.status_code)
    logResponse(response,'/log_grandpa_data/')
    



sendData()


