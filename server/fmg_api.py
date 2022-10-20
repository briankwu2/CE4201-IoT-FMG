from operator import add
from flask import Flask
from flask_restful import Api
from sqlalchemy import true 
from resources.healthChecker import HealthChecker
from resources.getGrandpa import GetGrandpa
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

def addResources(api):
    # adds all the resources that we need for the app
    api.add_resource(HealthChecker,"/")
    api.add_resource(LogGrandpa,"/log_grandpa_data/")
    api.add_resource(GetGrandpa,"/get_grandpa_data/")


print("Starting Find my Grandpa api")
app,api = buildApp() 
print("Will run")
# app.run(host='0.0.0.0', port=80)
addResources(api)

# database setup
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + DATABASE_PATH
db = SQLAlchemy(app)



class Grandpa(db.Model):
    __tablename__ = 'grandpa'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, unique=False, nullable=False)
    history = db.relationship('PointLog', backref='history')
class PointLog(db.Model):
    __tablename__ = 'point'
    id = db.Column(db.Integer, primary_key=True)
    lat = db.Column(db.Float, nullable=False)
    log = db.Column(db.Integer, nullable=False)
    bpm = db.Column(db.Integer, nullable=False)
    grandpaID = db.Column(db.Integer,db.ForeignKey('grandpa.id'),nullable=False)

def testUserAdd(database):
    database.create_all()

    for i in range(0,10):
        tempGrandpa = Grandpa()
        tempGrandpa.username = "miguel" + str(i)
    
        database.session.add(tempGrandpa)
    for k in range(0,10):
        tempPoint = PointLog()
        tempPoint.lat = 123
        tempPoint.log = 1244
        tempPoint.bpm = 100
        tempPoint.grandpaID = 1

        database.session.add(tempPoint)
    database.session.commit()

def printAllInDB(database):
    #print(db.session.query.all())
    pass

#testUserAdd(db)
with app.app_context():
    testUserAdd(db)
    printAllInDB(db)
app.run(debug=True)
