from flask_restful import Resource
from flask import request
from flask import Response

class HealthChecker(Resource):

    def get(self):
        response = Response("FMG healthy :)")
        response.headers.add("Access-Control-Allow-Origin", "*") 
        response.status_code = 200
        return response