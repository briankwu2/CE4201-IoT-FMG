

from flask_restful import Resource
from flask import request

class GetGrandpa(Resource):

    def __init__(self) -> None:
        print("Init get grandpa resoruce")

    def get(self):
        gID = request.args['grandpaID']
        point1 = {'time': 1234,'lat': 0, 'lon': 0,'bpm': 100}
        point2 = {'time': 1234,'lat': 0, 'lon': 0,'bpm': 100}
        point3 = {'time': 1234,'lat': 0, 'lon': 0,'bpm': 100}
        historyPos = [point1,point2,point3]
        return {'grandpaID':gID,'history': historyPos}