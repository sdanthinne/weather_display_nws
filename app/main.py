#!/usr/bin/env python3

from dataclasses import dataclass
from functools import cached_property

from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
import logging
import json

## internal
from location import LocationLookback, Location
from client import client

from datetime import datetime

from weather_gov_api_client.api.default import gridpoint
from weather_gov_api_client.models.gridpoint_geo_json import GridpointGeoJson
from weather_gov_api_client.models.gridpoint import Gridpoint

logger = logging.getLogger("uvicorn.error")

app = FastAPI()
templates = Jinja2Templates(directory="templates")

lookback_table = LocationLookback()

### Page handlers ###

@app.get("/display/")
async def weather_page(request: Request, lat:float = 0, lng:float = 0):
    logger.info(f"request for display at: longitude: {lng} latitude {lat}")
    ## append to location list
    requested_location = Location(longitude = lng, latitude = lat)
    lookback_table.add_location(requested_location)

    ## do API request to get forecast
    ## /gridpoints/TOP/x,y/forecast
    return templates.TemplateResponse("location_display.html", {"request":request, "location":requested_location, "datetime" : datetime})

@app.get("/", response_class=HTMLResponse)
async def base_page(request: Request):
    logger.info("/ root request rcvd")
    return templates.TemplateResponse("select_location.html",{"request":request, "location_history":lookback_table.history})

