# run tests to see if api works properly

import requests
from sqlalchemy import true
import time
# test parameters

url = 'http://ec2-3-20-227-73.us-east-2.compute.amazonaws.com'#'http://127.0.0.1:5000'
pasColor = '\33[92m'
failColor = '\33[91m'
normalColor = '\33[0m'
def printTestMsg(didPass:bool,msg:str):
    currentColor = pasColor if didPass else failColor
    currentLegend = "PASS " if didPass else "FAIL "
    print(currentColor + currentLegend,end='')
    print(msg)

# test 1

# health checker
try:
    #print("trying health checker")
    response1 = requests.get(url)
    #print(response1)
    #print(response1.json())
    if response1.status_code == 200:
        printTestMsg(True,"health check")
    else:
        printTestMsg(False,"health check")
except:
    printTestMsg(False,"health check")

# test 2 create grandpa
try:
    gp_data = {'username': 'miguel123', 'password': 'password'}
    response2 = requests.post(url+'/grandpa_data/',data=gp_data)
    #print(response2.json())
    if response2.status_code == 200:
        printTestMsg(True,"grandpa creation")
    else:
        if response2.status_code == 500:

            printTestMsg(False,"grandpa already exists")
        else:
            printTestMsg(False, "grandpa creation")
except:
    printTestMsg(False,"grandpa creation")


# test 3 gets incorrect grandpa
try:
    gp_data = {'grandpaID': '2', 'password': 'password'}
    response3 = requests.get(url+'/grandpa_data/',params=gp_data)
    #print(response3.json())
    if response3.status_code == 500:
        printTestMsg(True,"incorrect grandpa retrival")
    else:
        printTestMsg(False,"incorrect grandpa retrival")
except:
    printTestMsg(False,"incorrect grandpa retrival")



# test 4 gets correct grandpa
try:
    gp_data = {'grandpaID': 'miguel123', 'password': 'password'}
    response3 = requests.get(url+'/grandpa_data/',params=gp_data)
    print(response3.json())
    if response3.status_code == 200:
        printTestMsg(True,"correct grandpa retrival")
    else:
        printTestMsg(False,"correct grandpa retrival")
except:
    printTestMsg(False,"correct grandpa retrival")


# test 5 log position for grandpa
try:
    gp_data = {'grandpaID': 'miguel123','bpm': 70, 'lat': 32.98821483333334, 'log': -96.77045733333335, 'time': int(time.time())}
    response3 = requests.post(url+'/log_grandpa_data/',data=gp_data)
    #print(response3.json())
    if response3.status_code == 200:
        printTestMsg(True,"log grandpa pos")
    else:
        printTestMsg(False,"log grandpa pos")
except:
    printTestMsg(False,"due to exception")