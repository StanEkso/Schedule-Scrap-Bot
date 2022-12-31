from flask import Flask
from flask_restful import Api, Resource, reqparse
from api.resources.schedule import Schedule
from shared.services.config import configService
app = Flask(__name__)
api = Api(app)
api.add_resource(Schedule, "/schedule")


def bootstrap_api():
    print("Starting api...")
    print(configService.get("WEBAPP_PORT"))
    app.run(host=configService.get("WEBAPP_HOST"),
            port=configService.get("WEBAPP_PORT"))
