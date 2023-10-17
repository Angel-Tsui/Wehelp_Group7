from flask import *
from flask import Blueprint

import os
from dotenv import load_dotenv
load_dotenv()
API_key = os.getenv("Alice_API_key")

DailyData_api = Blueprint("dailyData", __name__, static_folder="static", template_folder="templates")

data_key = API_key
data_url = "https://opendata.cwa.gov.tw/api/v1/rest/datastore/F-D0047-091?Authorization="

@DailyData_api.route("/test")
def test():
    return {"data" : "dialy_testing_successful"}