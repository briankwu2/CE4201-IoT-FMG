# run tests to see if api works properly

import requests
from sqlalchemy import true

# test parameters

url = 'http://127.0.0.1:5000'
pasColor = '\33[92m'
failColor = '\33[91m'

def printTestMsg(didPass:bool,msg:str):
    currentColor = pasColor if didPass else failColor
    currentLegend = "PASS " if didPass else "FAIL "
    print(currentColor + currentLegend,end='')
    print(msg)

# test 1

# health checker
try:
    response1 = requests.get(url)
    if response1.status_code == 200:
        printTestMsg(True,"health check")
    else:
        printTestMsg(False,"health check")
except:
    printTestMsg(False,"health check")

# test 2 create grandpa
try:
    gp_data = {'username': 'miguel123'}
    response2 = requests.post(url+'/grandpa_data/',data=gp_data)
    print(response2.json())
    if response2.status_code == 200:
        printTestMsg(True,"grandpa creation")
    else:
        printTestMsg(False,"grandpa creation")
except:
    printTestMsg(False,"grandpa creation")


# test 3 gets incorrect grandpa
try:
    gp_data = {'grandpaID': '2'}
    response3 = requests.get(url+'/grandpa_data/',params=gp_data)
    print(response3.json())
    if response3.status_code == 500:
        printTestMsg(True,"incorrect grandpa retrival")
    else:
        printTestMsg(False,"incorrect grandpa retrival")
except:
    printTestMsg(False,"incorrect grandpa retrival")