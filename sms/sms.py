#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
A helper module for Nexmo
"""

import getopt
import os
import sys
from typing import List

import nexmo


def send(to: str, from_: str, body: str) -> None:
    """
    Send an SMS message
    """
    # pylint: disable-msg=C0103
    key = os.environ["NEXMO_API_KEY"]
    secret = os.environ["NEXMO_API_SECRET"]
    client = nexmo.Client(key=key, secret=secret)
    responseData = client.send_message(
        {"to": to, "from": from_, "text": body, "type": "unicode"}
    )

    if responseData["messages"][0]["status"] == "0":
        print("Message sent successfully.")
    else:
        print(f"Message failed with error: {responseData['messages'][0]['error-text']}")


def main(argv: List[str]) -> None:
    """
    A main function to parse arguments and send sms
    """
    # pylint: disable-msg=C0103
    to = ""
    from_ = ""
    text = ""
    try:
        opts, _ = getopt.getopt(argv, "h", ["to=", "from=", "text="])
    except getopt.GetoptError:
        print("sms.py --to <phone number> --from <phone number> --text <text>")
        sys.exit(2)
    for opt, arg in opts:
        if opt == "-h":
            print(" sms.py --to <phone number> --from <phone number> --text <text>")
            sys.exit()
        elif opt == "--to":
            to = arg
        elif opt == "--from":
            from_ = arg
        elif opt == "--text":
            text = arg.strip()

    if to == "" or from_ == "" or text == "":
        print("sms.py --to <phone number> --from <phone number> --text <text>")
        sys.exit(2)

    send(to=to, from_=from_, body=text)


if __name__ == "__main__":
    main(sys.argv[1:])
