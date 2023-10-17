from flask import *
import requests
app = Flask(__name__)

from flask import Blueprint

from Alice_WeeklyData import WeeklyData_api

app.register_blueprint(WeeklyData_api, url_prefix="/api/weekly_data")

# 頁面
@app.route("/")
def index():
    return render_template("index.html")

app.run(host="0.0.0.0", port=3000, debug=True)