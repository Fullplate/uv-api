import logging

import requests
from flask import current_app


class UvDataService:
    """Container for UV data operations.
    
    Attributes:
        api_url: Arpansa API URL
    """

    def __init__(self, api_url: str) -> None:
        self.api_url = api_url

    def fetch_uv_data(self, lat: float, long: float, date: str) -> dict:
        """Given lat, long and date in format yyyy-mm-dd, return UV data"""
        params = {"latitude": lat, "longitude": long, "date": date}
        resp = requests.get(self.api_url, params=params)
        current_app.logger.info(f"UV data request: {resp.url}")
        if resp.status_code == 200:
            resp_dict = resp.json()
            return {
                "current": resp_dict["CurrentUVIndex"],
                "max": resp_dict["MaximumUVLevel"],
                "max_time_of_day": resp_dict["MaximumUVLevelDateTime"].split(" ")[1]
            }
        else:
            raise Exception(f"UV data request failed with status code {resp.status_code}")
