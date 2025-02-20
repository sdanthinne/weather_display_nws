from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.nws_forecast_office_id import NWSForecastOfficeId
from ...types import UNSET, Response, Unset


def _get_kwargs(
    wfo: NWSForecastOfficeId,
    x: int,
    y: int,
    *,
    limit: Union[Unset, int] = 500,
    cursor: Union[Unset, str] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["limit"] = limit

    params["cursor"] = cursor

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/gridpoints/{wfo}/{x},{y}/stations",
        "params": params,
    }

    return _kwargs


def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[Any]:
    if response.status_code == 200:
        return None
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[Any]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    wfo: NWSForecastOfficeId,
    x: int,
    y: int,
    *,
    client: Union[AuthenticatedClient, Client],
    limit: Union[Unset, int] = 500,
    cursor: Union[Unset, str] = UNSET,
) -> Response[Any]:
    """Returns a list of observation stations usable for a given 2.5km grid area

    Args:
        wfo (NWSForecastOfficeId): Three-letter identifier for a NWS office.
        x (int):
        y (int):
        limit (Union[Unset, int]):  Default: 500.
        cursor (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        wfo=wfo,
        x=x,
        y=y,
        limit=limit,
        cursor=cursor,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    wfo: NWSForecastOfficeId,
    x: int,
    y: int,
    *,
    client: Union[AuthenticatedClient, Client],
    limit: Union[Unset, int] = 500,
    cursor: Union[Unset, str] = UNSET,
) -> Response[Any]:
    """Returns a list of observation stations usable for a given 2.5km grid area

    Args:
        wfo (NWSForecastOfficeId): Three-letter identifier for a NWS office.
        x (int):
        y (int):
        limit (Union[Unset, int]):  Default: 500.
        cursor (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        wfo=wfo,
        x=x,
        y=y,
        limit=limit,
        cursor=cursor,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
