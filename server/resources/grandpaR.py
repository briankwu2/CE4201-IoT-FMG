

from flask_restful import Resource
from flask import request


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
        print("username extracted: " + usrName)
        tempGrandpa = self.grandpaModel() # creats empty grandpa
        tempGrandpa.username = usrName
        print(tempGrandpa)
        self.db.session.add(tempGrandpa) # adds to db
        self.db.session.commit() # commits chagnes to db
        return 200
    def get(self):
        gID = request.args['grandpaID'] # grandpa id = username
        tempGrandpa = self.safeLookUpGrandpa(gID)
        if tempGrandpa != False:
            return {'status': 200, 'grandpaID':tempGrandpa.username,'history': tempGrandpa.history}
        else:
            return {'status':500, 'msg': "Unable to find grandpa in database"} # error getting grandpa
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
    

    def constructHistoryJson(history)->dict:
        # reds history array and constructs dict

        historyDic = {}
        for i in range(0,len(history)):
            historyDic[str(history[i].time)] = hist