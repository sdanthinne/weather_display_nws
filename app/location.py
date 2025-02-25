#!/usr/bin/env python3

from dataclasses import dataclass
from functools import cached_property

import logging
import json

from weather_gov_api_client import Client

from http import HTTPStatus

from weather_gov_api_client.api.default import point
from weather_gov_api_client.models.point import Point
from weather_gov_api_client.models.point_geo_json import PointGeoJson

from weather_gov_api_client.api.default import gridpoint
from weather_gov_api_client.models.gridpoint_geo_json import GridpointGeoJson
from weather_gov_api_client.models.gridpoint import Gridpoint

from weather_gov_api_client.models.gridpoint_forecast_geo_json import GridpointForecastGeoJson
from weather_gov_api_client.models.gridpoint_forecast import GridpointForecast

from weather_gov_api_client.models.relative_location import RelativeLocation

from client import client

from booster import get_gridpoint_forecast_custom

logger = logging.getLogger("uvicorn.error")

@dataclass
class Location():
    longitude: int
    latitude: int

    def __post_init__(self):
        logger.info("Attempting to request relative location information")
        try:
            self._name = f"{self.relative_location.city}, {self.relative_location.state}"
        except Exception as e:
            logger.info(f"Location information for {self} not available")
            self._name = f"Unsearchable location"
    
    @cached_property
    def relative_location(self) -> RelativeLocation:
        return RelativeLocation.from_dict(self.point.relative_location.properties.to_dict())

    @cached_property
    def format(self):
        return  [format(x,".4f").rstrip('0') for x in (self.latitude, self.longitude)]
    
    def request_type(self, endpoint, *args):
        res = endpoint.sync_detailed(*args, client=client)
        if res.status_code != HTTPStatus.OK:
            raise Exception(f"Help! request failed: {res.status_code} : {res.headers}")
        return res.parsed

    @cached_property
    def point_geo_json(self) -> PointGeoJson:
        lat_format, long_format = self.format
        pt = self.request_type(point, f"{lat_format},{long_format}")
        return pt

    @cached_property
    def point(self) -> Point:
        return Point.from_dict(self.point_geo_json.properties.to_dict())

    @cached_property
    def name(self):
        return self._name
    
    @cached_property
    def gridpoint_geo_json(self) -> GridpointGeoJson:
        res = self.request_type(gridpoint, self.point.cwa, self.point.grid_x, self.point.grid_y)
        return res

    @cached_property
    def gridpoint_forecast_geo_json(self) -> GridpointForecastGeoJson:
        return get_gridpoint_forecast_custom(self.point.cwa, self.point.grid_x, self.point.grid_y, client=client).parsed
    
    @cached_property
    def gridpoint_forecast(self) -> GridpointForecast:
        return GridpointForecast.from_dict(self.gridpoint_forecast_geo_json.properties.to_dict())

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

