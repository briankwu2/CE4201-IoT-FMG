
from flask_restful import Resource
from flask import request

class LogGrandpa(Resource):

    def __init__(self):
        print("init log grandpa resource")
    
    def post(self):
        grandpaID = request.form["grandpaID"]
        bpm = request.form['bpm']
        lat = request.form['lat']
        log = request.form['log']
        return {'status': 200}