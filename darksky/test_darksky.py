#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Unit tests
"""

import os
import unittest

import mock
import requests

from . import darksky


# will override the requests.Response returned from requests.get
class MockResponse:
    # mock json() method always returns a specific testing dictionary
    @staticmethod
    def json():
        return {
            "latitude": 34,
            "longitude": 32,
            "timezone": "Asia/Nicosia",
            "hourly": {"summary": "Humid throughout the day."},
        }


@mock.patch.dict(os.environ, {"DARKSKY_SECRET_KEY": "N2MXMO8BSO"})
def test_generate_darksky_api_url():
    assert (
        darksky.generate_darksky_api_url("40.730610", "-73.935242")
        == "https://api.darksky.net/forecast/N2MXMO8BSO/40.730610,-73.935242"
    )


@mock.patch.dict(os.environ, {"DARKSKY_SECRET_KEY": "N2MXMO8BSO"})
def test_get_hourly_forecast(monkeypatch):
    def mock_get(*args, **kwargs):
        return MockResponse()

    monkeypatch.setattr(requests, "get", mock_get)
    result = darksky.get_hourly_forecast("40.730610", "-73.935242")
    assert (
        result
        == '{"latitude": 34, "longitude": 32, "timezone": "Asia/Nicosia", "hourly": {"summary": "Humid throughout the day."}}'
    )


def test_main():
    pass


if __name__ == "__main__":
    unittest.main()
