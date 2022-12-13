

from flask_restful import Resource
from flask import request
from flask import Response
import json
from cryptography.fernet import Fernet
#key for password
key = b'f_eZN-pVBPS-0mZrhI5seaNmaRjVqRAxOXNw46m7aSU='

class GrandpaR(Resource):

    def __init__(self, **kwargs) -> None:
        print("Init get grandpa resoruce")
        self.grandpaModel = kwargs['model']
        self.db = kwargs['database'] # ref to db
    def post(self):
        # posts a grandpa so creats a new grandpa if it doenst exits
        print("Reqauested post")
        print("form recived: ")
        print(request.form)
        usrName = request.form['username']
        pw = request.form['password']
        print("username extracted: " + usrName)
        grandPaLookup = self.safeLookUpGrandpa(usrName)
       
        if grandPaLookup == False:
            
            tempGrandpa = self.grandpaModel() # creats empty grandpa
            tempGrandpa.username = usrName

            #tempGrandpa.password = encrypter(pw)
             #g
            # TODO add password to grandpa and ecrypt
            #tempGrandpa.password =''
            #tempGrandpa.password = request.form ['password']
            #tempGrandpa.usrPassword = input("\n Password? \n")
            #ask usrname
            #ask password
            #add to db
            ####


            ###
            print(tempGrandpa)
            self.db.session.add(tempGrandpa) # adds to db
            self.db.session.commit() # commits chagnes to db
            r = Response('Grandpa created successfully')
            r.status = 200
            #return {'status': 200, 'msg': 'Grandpa created successfully'}
            return r
        else:
            r = Response('Grandpa already exists')
            r.status = 500
            return r #{'status': 500, 'msg': 'Grandpa already exists'}
    def get(self):
        # sends back a grandpa
        gID = request.args['grandpaID'] # grandpa id = username
        gPW = request.args['password'] # grandpa pw 

        tempGrandpa = self.safeLookUpGrandpa(gID)
        # TODO logic to check if passowrd is correct 
        if tempGrandpa != False:
            # stuff to send to user
            dic = {'grandpaID':tempGrandpa.username,'history': self.constructHistoryJson(tempGrandpa.history)}
            #decrypt password of tempgtandpa
            decPW = self.decrypt(tempGrandpa.password)
            # if decPW = gPW
            if decPW == gPW:
              response = Response(json.dumps(dic)) # this is how you convert the dic to json response
              response.status = 200
              response.headers.add("Access-Control-Allow-Origin", "*") 
              return response
            else:
               response = Response("Unable to find grandpa in database")
               response.status = 500
               response.headers.add("Access-Control-Allow-Origin", "*") 
            #dic = {'status':500, 'msg': "Unable to find grandpa in database"}
            #response = Response("Unable to find grandpa in database")
            #response.status = 500
            #response.headers.add("Access-Control-Allow-Origin", "*") 
               return response

            #return re {'status': 200, 'grandpaID':tempGrandpa.username,'history': self.constructHistoryJson(tempGrandpa.history)}
        else:
            #dic = {'status':500, 'msg': "Unable to find grandpa in database"}
            response = Response("Unable to find grandpa in database")
            response.status = 500
            response.headers.add("Access-Control-Allow-Origin", "*") 
            return response
            #return {'status':500, 'msg': "Unable to find grandpa in database"} # error getting grandpa
        # point1 = {'time': 1234,'lat': 0, 'lon': 0,'bpm': 100}
        # point2 = {'time': 1234,'lat': 0, 'lon': 0,'bpm': 100}
        # point3 = {'time': 1234,'lat': 0, 'lon': 0,'bpm': 100}
        # historyPos = [point1,point2,point3]
        # return {'grandpaID':gID,'history': historyPos}

    
    
    def safeLookUpGrandpa(self,username:str):
        # safe looks up the grandpa by the id in the db
        # returns the grandpa object if found otherwise returns false
        try:
            temp_grandPa = self.grandpaModel.query.filter_by(username=username).first() # should only be one since it is uniques
            if temp_grandPa != None:
                return temp_grandPa
            else:
                return False
        except:
            return False
    

    def constructHistoryJson(self,history)->dict:
        # reds history array and constructs array of dic
        historyDicArr = []
        for i in range(0,len(history)):
            currentPoint = history[i]
            historyDicArr.append({'id':currentPoint.id, 'time':currentPoint.time,'lat':currentPoint.lat, 'log': currentPoint.log, 'bpm': currentPoint.bpm})
        return historyDicArr

    def encrypt(self,password:str)-> str:
        fernet = Fernet(key)
        encMessage = fernet.encrypt(password.encode())
        return encMessage
        

    def decrypt (self,password:str)->str:
        fernet = Fernet(key)
        decMessage = fernet.decrypt(password).decode()
        return decMessage


