from flask import Flask
from flask_restful import Api, Resource
import pandas as pd
import json

app = Flask(__name__)
api = Api(app)

database = "mini.json"
data = json.loads(open(database).read())

class Main(Resource):
    def get(self,name):
        return data[name]

api.add_resource(Main,"/helloworld/<string:name>")

if __name__ == "__main__":
    app.run(debug = True)
