#!/usr/bin/env python3

from weather_gov_api_client import Client

client = Client(base_url="https://api.weather.gov/", headers = {"User-Agent":"(wether.danthinne.com, wether.danthinne.com)"})
