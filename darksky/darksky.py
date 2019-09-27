#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
A helper module for Dark Sky Forecast
"""

import getopt
import json
import os
import sys
from typing import Dict, List

import requests


def generate_darksky_api_url(latitude: str, longitude: str) -> str:
    """
    Return url for Dark Sky API
    """
    secret_key = os.environ["DARKSKY_SECRET_KEY"]
    location = ",".join([str(latitude), str(longitude)])
    return "/".join(["https://api.darksky.net/forecast", secret_key, location])


def get_hourly_forecast(latitude: str, longitude: str) -> str:
    """
    Returns an hour-by-hour forecast for the next 48 hours
    """
    payload = {
        "exclude": "currently,minutely,daily,flags",
        "lang": "en",
        "units": "si",
    }  # type: Dict[str, str]
    req = requests.get(generate_darksky_api_url(latitude, longitude), params=payload)
    data = req.json()
    return json.dumps(data)


def main(argv: List[str]) -> str:
    """
    A main function to parse arguments and request hourly forecast
    """
    latitude = ""
    longitude = ""
    try:
        opts, _ = getopt.getopt(argv, "h", ["lat=", "lon="])
    except getopt.GetoptError:
        print("darksky.py --lat <latitude> --lon <longitude>")
        sys.exit(2)
    for opt, arg in opts:
        if opt == "-h":
            print("darksky.py --lat <latitude> --lon <longitude>")
            sys.exit()
        elif opt == "--lat":
            latitude = arg
        elif opt == "--lon":
            longitude = arg

    if latitude == "" or longitude == "":
        print("darksky.py --lat <latitude> --lon <longitude>")
        sys.exit(2)

    return get_hourly_forecast(latitude, longitude)


if __name__ == "__main__":
    main(sys.argv[1:])
