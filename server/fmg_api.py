from operator import add
from flask import Flask
from flask_restful import Api
from sqlalchemy import true 
from resources.healthChecker import HealthChecker
from resources.getGrandpa import GetGrandpa
from resources.logGrandpa import LogGrandpa
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
app.run(debug=True)
