from typing import Any, Dict, Optional, Union, cast
from weather_gov_api_client import Client
from weather_gov_api_client.models.gridpoint_forecast_geo_json import GridpointForecastGeoJson
from weather_gov_api_client.types import Response


def get_gridpoint_forecast_custom(
    wfo: str,
    x: int,
    y: int,
    client: Client,
) -> Response[Union[GridpointForecastGeoJson, Any]]:
    """
    Custom implementation for the gridpoint forecast endpoint, since auto-generation does not create endpoint due to:
    https://github.com/openapi-generators/openapi-python-client/issues/881

    Args:
                wfo: Weather Forecast Office identifier (e.g., 'SEA')
        x: X coordinate in the grid
        y: Y coordinate in the grid
        client: The API client instance

    Returns:
                Response object containing the parsed GridpointForecastGeoJson or error
    """
    url = f"/gridpoints/{wfo}/{x},{y}/forecast"
    
    kwargs = {
        "method":"get",
        "url": url
    }

    response = client.get_httpx_client().request(
            **kwargs
    )

    # Try to parse the response as a GridpointForecast
    try:
        if response.status_code == 200:
            return Response(
                status_code=response.status_code,
                content=response.content,
                headers=response.headers,
                parsed=GridpointForecastGeoJson.from_dict(response.json()),
            )
    except Exception as e:
        print(f"Error parsing response: {e}")

    # If parsing fails or status code is not 200, return the raw response
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=response.json(),
    )
