from flask_restful import Resource
class Schedule(Resource):
    def get(self):
        return "OK", 200 