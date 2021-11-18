from flask import Flask, jsonify, request
from flask_restful import Resource, Api, reqparse
import pandas as pd
import requests
import xmltodict

app = Flask(__name__)
api = Api(app)

# Classes as resources
@app.route('/api/v1/users', methods=['POST'])
def getUsers():

    # # To read the JSON-body of a POST-request
    # print(request.get_json())

    xml_data = request.data # Reads the body of the api call and puts the values in this XML object
    content_dict = xmltodict.parse(xml_data) # Converts the XML to a dictionary
    json_data = jsonify(content_dict) # Converts the dictonary to a JSON
    return json_data, 200 # Returns the JSON data in the body of the response


# Used to run the API
if __name__ == '__main__':
    app.run(debug=True)  # run our Flask app / API