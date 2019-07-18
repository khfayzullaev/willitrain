#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Main file to get weather forecast and send sms
"""


import getopt
import json
import sys
from typing import List

import darksky
import sms


def main(argv: List[str]) -> None:
    """
    A main function to parse arguments and send sms
    """
    # pylint: disable-msg=C0103
    lat = ""
    lon = ""
    to = ""
    try:
        opts, _ = getopt.getopt(argv, "h", ["lat=", "lon=", "to=", "text="])
    except getopt.GetoptError:
        print("forecast.py --lat <latitude> --lon <longitude> --to <phone>")
        sys.exit(2)
    for opt, arg in opts:
        # pylint: disable-msg=C0103
        if opt == "-h":
            # pylint: disable-msg=C0103
            print("forecast.py --lat <latitude> --lon <longitude> --to <phone>")
            sys.exit()
        elif opt == "--lat":
            lat = arg
        elif opt == "--lon":
            lon = arg
        elif opt == "--to":
            to = arg

    if lat == "" or lon == "" or to == "":
        print("forecast.py --lat <latitude> --lon <longitude> --to <phone>")
        sys.exit(2)

    forecast = json.loads(darksky.get_hourly_forecast(lat, lon))
    sms.send(to=to, body=forecast["timezone"] + " " + forecast["hourly"]["summary"])


if __name__ == "__main__":
    main(sys.argv[1:])
