import os
from datetime import date

from flask import Flask

from geocode import GeocodeService
from uv_data import UvDataService

app = Flask(__name__)
app.config.from_object("config.Config")

geocode_service = GeocodeService(app.config["LOCATIONIQ_API_URL"], app.config["LOCATIONIQ_API_KEY"])
uv_data_service = UvDataService(app.config["ARPANSA_API_URL"])

@app.route("/api/uv/<location>")
def show_uv(location):
    (lat, long) = geocode_service.forward_lookup(location)
    date_today = f"{date.today():%Y-%m-%d}"
    uv_data = uv_data_service.fetch_uv_data(lat, long, date_today)
    return uv_data
