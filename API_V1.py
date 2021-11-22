from flask import Flask
from flask_restful import Api
import requests


app = Flask(__name__)
api = Api(app)


# Classes as resources
@app.route('/api/v1/users', methods=['POST'])
def postMissionToFleetmanager():
    # Tijdelijke URL, voor PoC dat er een POST gestuurd kan worden:
    URL = "https://reqbin.com/echo/post/json"
    
    # Uiteindelijke URL hieronder:
    # URL = "http://192.168.43.119/api/v2.0.0/mission_scheduler/"

    # JSON data:
    JSON = '"mission_id": "e20d961c-a360-11eb-b0ec-94c6911adace"'

    # Actual request
    request = requests.post(url=URL, json=JSON)

    # Return value to confirm it was succesfull with statuscode of choice
    return {'response': "Call succesfull, resultcode: " + str(request.status_code)}, 200
  

# Used to run the API
if __name__ == '__main__':
    app.run(debug=True)  # run our Flask app / API, debug=true makes it rerun every ctrl+s