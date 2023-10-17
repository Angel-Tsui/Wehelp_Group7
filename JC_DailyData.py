from flask import *
from flask import Blueprint
import requests
import os
from dotenv import load_dotenv
load_dotenv()
API_key = os.getenv("Alice_API_key")

DailyData_api = Blueprint("dailyData", __name__, static_folder="static", template_folder="templates")

data_key = API_key
data_url = "https://opendata.cwa.gov.tw/api/v1/rest/datastore/F-C0032-001?Authorization="

def getDailyData(location_name):
    response = requests.get(data_url+data_key+"&locationName="+location_name)
    data = response.json()
    return data['records']['location'][0]

@DailyData_api.route("/")
def get_daily_data():
    location_name = str(request.args.get("locationName", ""))
    result = getDailyData(location_name)
    return jsonify(result)

@DailyData_api.route("/test")
def test():
    return {"data" : "dialy_testing_successful"}