from flask_restful import Resource
from flask import request

class HealthChecker(Resource):

    def get(self):
        return "FMG healthy :)"