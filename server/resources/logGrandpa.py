
from flask_restful import Resource
from flask import request
from flask import Response

class LogGrandpa(Resource):

    def __init__(self, **kwargs):
        print("init log grandpa resource")
        self.pointLogModel = kwargs['pointModel']
        self.grandpaModel = kwargs['grandpaModel']
        self.db = kwargs['database']
    
    def post(self):
        grandpaID = request.form['grandpaID']
        print(request.form)
        grandpaRef = self.findGrandpaWithUsername(grandpaID)
        if grandpaRef != False:
            # found grandpa now add stuff and save
            tempLogPoint = self.pointLogModel() # creats empty log point
            tempLogPoint.bpm = int(request.form['bpm'])
            tempLogPoint.lat = float(request.form['lat'])
            tempLogPoint.log = float(request.form['log'])
            tempLogPoint.time = int(request.form['time']) # in unix time
            tempLogPoint.grandpaID = int(grandpaRef.id) # assignes the matching grandpa id 
            self.db.session.add(tempLogPoint)
            self.db.session.commit()
            response = Response("logged successfully")
            response.status = 200
            return response#{'status': 200}
        else:
            response = Response("Unable to find grandpa")
            response.status = 500
            return response#{'status': 500, 'msg': 'Unable to find grandpa'}
        
        

    def findGrandpaWithUsername(self,username:str):
        try:

            return self.grandpaModel.query.filter_by(username=username).first()
        except:
            print("ERROR getting grandpa")
            return False
        pass