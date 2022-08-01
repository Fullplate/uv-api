import re

import requests
from flask import current_app


class GeocodeService:
    """Container for geocode operations.
    
    Attributes:
        api_url: LocationIQ API URL
        api_key: LocationIQ API key
    """

    def __init__(self, api_url: str, api_key: str) -> None:
        self.api_url = api_url
        self.api_key = api_key

    def forward_lookup(self, location: str) -> tuple:
        """Given location, return lat, long tuple"""
        params = {"key": self.api_key, "city": location, "country": "Australia", "format": "json"}
        resp = requests.get(self.api_url, params=params)
        current_app.logger.info(f"Geocode forward lookup request: {re.sub('key=[^&]*', 'key=REDACTED', resp.url)}")
        if resp.status_code == 200:
            resp_dict = resp.json()[0] # safe assumption, returns 404s if no results
            return (resp_dict["lat"], resp_dict["lon"])
        else:
            raise Exception(f"Geocode forward lookup request failed with status code {resp.status_code}")
