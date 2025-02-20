#!/usr/bin/env python3

from dataclasses import dataclass

from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
import logging

from weather_gov_api_client import Client

from weather_gov_api_client.api.default import point
from weather_gov_api_client.models.point import Point
from weather_gov_api_client.models.point_geo_json import PointGeoJson

logger = logging.getLogger()

app = FastAPI()
templates = Jinja2Templates(directory="templates")
client = Client(base_url="https://api.weather.gov/", headers = {"User-Agent":"(wether.danthinne.com, wether@danthinne.com)"})

@dataclass
class Location():
    longitude: int
    latitude: int
    
    @property
    def format(self):
        return  [format(x,".4f").rstrip('0') for x in (self.latitude, self.longitude)]
    
    def request(self):
        lat_format, long_format = self.format
        pt:PointGeoJson = point.sync(f"{lat_format},{long_format}", client=client)
        return pt
        
    def to_gridpoint(self):
        x = 0
        y = 0
        pt = self.request()
        pt = Point.from_dict(pt.to_dict()) #conversion from geoJson to regular Point
        print(pt)
        return pt.grid_x, pt.grid_y

    @property
    def forecast(self):
        pt_json = self.request()
        pt = Point.from_dict(pt_json.to_dict())
        return pt.forecast


class LocationLookback():
    """ Stores locations in order of new -> old"""
    def __init__(self, location_lookback_length: int = 10):
        # ordered list of locations
        self.location_history:list(Location) = [Location(0,0) for _ in range(location_lookback_length)]
        self.location_lookback_length = location_lookback_length

    def add_location(self, location: Location):
        ## maybe want conversion to city?
        if len(self.location_history) > self.location_lookback_length:
            # remove oldest location
            self.location_history.pop()
        self.location_history.insert(0, location)

    @property
    def history(self):
        return self.location_history


lookback_table = LocationLookback()


@app.get("/display/")
async def weather_page(request: Request, lat:float = 0, lng:float = 0):

    ## append to location list
    requested_location = Location(longitude = lng, latitude = lat)
    lookback_table.add_location(requested_location)

    ## do API request to translate into gridpoints
    ## /points/lat,long
    
    print(requested_location.to_gridpoint())
    print(requested_location.forecast)

    ## do API request to get forecast
    ## /gridpoints/TOP/x,y/forecast

    return templates.TemplateResponse("location_display.html", {"request":request})

@app.get("/", response_class=HTMLResponse)
async def base_page(request: Request):
    return templates.TemplateResponse("select_location.html",{"request":request, "location_history":lookback_table.history})

