from operator import add
from flask import Flask
from flask_restful import Api
from sqlalchemy import true 
from resources.healthChecker import HealthChecker
from resources.grandpaR import GrandpaR
from resources.logGrandpa import LogGrandpa
from flask_sqlalchemy import SQLAlchemy
from globals import *
# @app.route("/")
# def fmg_home():
#     return "find my grandpa"


def buildApp():
    #sets up the app
    # sets up database for future
    app = Flask(__name__)
    
    api = Api(app)
    return app,api




print("Starting Find my Grandpa api")
app,api = buildApp() 
print("Will run")
# database setup
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + DATABASE_PATH
db = SQLAlchemy(app)
# app.run(host='0.0.0.0', port=80)







# database models


class Grandpa(db.Model):
    __tablename__ = 'grandpa'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(12), unique=True, nullable=False)
    # TODO add password section encrypted string // V
    password = db.Column(db.String(200), unique=False, nullable=False)
    #encryptPassword = db.Column(db.string(200), unique=False, nullable=False)
    #encryptKey= db.Column(db.string(200),unique=False, nullable=False)
    history = db.relationship('PointLog', backref='grandpa')
class PointLog(db.Model):
    __tablename__ = 'point'
    id = db.Column(db.Integer, primary_key=True)
    time = db.Column(db.Float,nullable=False) # in unix time
    lat = db.Column(db.Float, nullable=False)
    log = db.Column(db.Float, nullable=False)
    bpm = db.Column(db.Integer, nullable=False)
    grandpaID = db.Column(db.Integer,db.ForeignKey('grandpa.id'),nullable=False)



def addResources(api, dataBaseL):
    # adds all the resources that we need for the app
    api.add_resource(HealthChecker,"/")
    api.add_resource(LogGrandpa,"/log_grandpa_data/",resource_class_kwargs={'database': dataBaseL, 'grandpaModel': Grandpa, 'pointModel': PointLog})
    api.add_resource(GrandpaR,"/grandpa_data/",resource_class_kwargs={'database': dataBaseL,'model': Grandpa})

##############################################
# adds the resources to the api
addResources(api,db)
###############################################
def testUserAdd(database):
    database.create_all()

    #for i in range(0,10):
    # tempGrandpa = Grandpa()
    # tempGrandpa.username = "miguel" + str(0)

    # database.session.add(tempGrandpa)
    # for k in range(0,10):
    #     tempPoint = PointLog()
    #     tempPoint.time = 9999
    #     tempPoint.lat = 123
    #     tempPoint.log = 1244
    #     tempPoint.bpm = 100
    #     tempPoint.grandpaID = 1

    #     database.session.add(tempPoint)
    database.session.commit()

def printAllInDB(database):
    #print(db.session.query.all())
    grandpaTest:Grandpa =  Grandpa.query.filter_by(username='miguel0').first()
    print("grandpa points len:" + str(len(grandpaTest.history)))
    print("Point 1: " + str(grandpaTest.history[0].lat))
    pass
 
#testUserAdd(db) # comment this line out when db is already created
with app.app_context():
    testUserAdd(db)
    #printAllInDB(db)
#app.run(debug=False)
