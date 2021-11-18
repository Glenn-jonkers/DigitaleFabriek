from flask import Flask
from flask_restful import Resource, Api, reqparse
import pandas as pd
import requests

app = Flask(__name__)
api = Api(app)

# Data
users_path = 'C:/Users/odranJ/OneDrive - Office 365 Fontys/Desktop/API Test Python/data/users.csv'
locations_path = 'C:/Users/odranJ/OneDrive - Office 365 Fontys/Desktop/API Test Python/data/locations.csv'

# Classes as resources
class Users(Resource):
    def get(self):
        data = pd.read_csv(users_path)
        data = data.to_dict()
        return {'data': data}, 200

    def post(self):
        # How to read a body of the API call
        # Check how to read XML
        parser = reqparse.RequestParser() # Used to read parameters of the call
        parser.add_argument('userId', required=True, type=int) # Specifically looks for a parameter with the value 'userId'
        parser.add_argument('name', required=True, type=str)
        parser.add_argument('city', required=True, type=str)
        args = parser.parse_args()

        data = pd.read_csv(users_path)

        if args['userId'] in data['userId']:
            return {
                'message': f"{args['userId']} already exists"
            }, 409
        else:
            data = data.append({
                'userId': args['userId'],
                'name': args['name'],
                'city': args['city'],
                'locations': []
            }, ignore_index=True)
            data.to_csv(users_path, index=False)
            return {'data': data.to_dict()}, 200

    def delete(self):
        parser = reqparse.RequestParser()
        parser.add_argument('userId', required=True, type=int)
        args = parser.parse_args()

        data = pd.read_csv(users_path)

        if args['userId'] in data['userId']:
            data = data[data['userId'] != str(args['userId'])]
            data.to_csv(users_path, index=False)
            return {'data': data.to_dict()}, 200
        else:
            return {
                'message': f"{args['userId']} does not exists"
            }, 404

    
class Locations(Resource):
    def get(self):
        # api-endpoint
        URL = "http://127.0.0.1:5000/users"
        # change this URL to: http://192.168.43.119/api/v2.0.0/mission_scheduler/

        # Add this to the body: {"mission_id": "e20d961c-a360-11eb-b0ec-94c6911adace"}

        # sending get request and saving the response as response object
        request = requests.get(url = URL)

        # extracting data in json format
        data = request.json()

        return {'data': data}, 200

    
api.add_resource(Users, '/users')  # '/users' is our entry point for Users
api.add_resource(Locations, '/locations')  # and '/locations' is our entry point for Locations

# Used to run the API
if __name__ == '__main__':
    app.run(debug=True)  # run our Flask app