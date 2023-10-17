from flask import *
from flask import Blueprint

import os
from dotenv import load_dotenv
load_dotenv()
API_key = os.getenv("Alice_API_key")

WeeklyData_api = Blueprint("weeklyData", __name__, static_folder="static", template_folder="templates")

data_key = API_key
data_url = "https://opendata.cwa.gov.tw/api/v1/rest/datastore/F-D0047-091?Authorization="

def get_data(location_name, data_type):
    response = requests.get(data_url+data_key+"&locationName="+location_name)
    data = response.json()

    detail = data["records"]["locations"][0]["location"][0]
    data_time = detail["weatherElement"][data_type]["time"]

    clearData = {
		"locationName" : detail["locationName"],
		"longitude" : detail["lon"],
		"latitude" : detail["lat"],
		"description" : detail["weatherElement"][data_type]["description"],
		"time" : []
	}

    for item in data_time:
        timeData = {
            "startTime" : item["startTime"],
            "endTime" : item["endTime"],
            "result" : item["elementValue"][0]["value"],
            "measures" : item["elementValue"][0]["measures"]
        }
        clearData["time"].append(timeData)

    return clearData

@WeeklyData_api.route("/")
def get_weekly_data():
    location_name = str(request.args.get("locationName", ""))
    data_type = int(request.args.get("data_type", ""))

    finalData = get_data(location_name, data_type)
    print(finalData)
    return jsonify(finalData)

@WeeklyData_api.route("/test")
def test():
    return {"data" : "testing_successful"}