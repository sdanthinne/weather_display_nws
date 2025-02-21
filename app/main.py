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

from weather_gov_api_client.api.default import gridpoint
from weather_gov_api_client.models.gridpoint_geo_json import GridpointGeoJson
from weather_gov_api_client.models.gridpoint import Gridpoint

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

    @property
    def point(self) -> Point:
        pt = self.request()
        return Point.from_dict(pt.properties.to_dict())

    @property
    def name(self):
        
        self._name = f"{self.point.relative_location.city}, {self.point.relative_location.state}"
        return self._name
        

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
        [x.name for x in self.location_history]
        return self.location_history


lookback_table = LocationLookback()


@app.get("/display/")
async def weather_page(request: Request, lat:float = 0, lng:float = 0):

    ## append to location list
    requested_location = Location(longitude = lng, latitude = lat)
    lookback_table.add_location(requested_location)

    ## do API request to translate into gridpoints
    ## /points/lat,long
    
    print(requested_location.point.forecast)
    print(requested_location.point.grid_x)

    ## do API request to get forecast
    ## /gridpoints/TOP/x,y/forecast
    print(requested_location.point.cwa)
    gp:GridpointGeoJson = gridpoint.sync(requested_location.point.cwa, requested_location.point.grid_x, requested_location.point.grid_y, client=client)
    #print(Gridpoint.from_dict(gp.properties.to_dict()))

    return templates.TemplateResponse("location_display.html", {"request":request})

@app.get("/", response_class=HTMLResponse)
async def base_page(request: Request):
    return templates.TemplateResponse("select_location.html",{"request":request, "location_history":lookback_table.history})

