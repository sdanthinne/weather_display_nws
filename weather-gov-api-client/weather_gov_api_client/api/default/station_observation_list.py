import datetime
from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...types import UNSET, Response, Unset


def _get_kwargs(
    station_id: str,
    *,
    start: Union[Unset, datetime.datetime] = UNSET,
    end: Union[Unset, datetime.datetime] = UNSET,
    limit: Union[Unset, int] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    json_start: Union[Unset, str] = UNSET
    if not isinstance(start, Unset):
        json_start = start.isoformat()
    params["start"] = json_start

    json_end: Union[Unset, str] = UNSET
    if not isinstance(end, Unset):
        json_end = end.isoformat()
    params["end"] = json_end

    params["limit"] = limit

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/stations/{station_id}/observations",
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
    station_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    start: Union[Unset, datetime.datetime] = UNSET,
    end: Union[Unset, datetime.datetime] = UNSET,
    limit: Union[Unset, int] = UNSET,
) -> Response[Any]:
    """Returns a list of observations for a given station

    Args:
        station_id (str):
        start (Union[Unset, datetime.datetime]):
        end (Union[Unset, datetime.datetime]):
        limit (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        station_id=station_id,
        start=start,
        end=end,
        limit=limit,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    station_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    start: Union[Unset, datetime.datetime] = UNSET,
    end: Union[Unset, datetime.datetime] = UNSET,
    limit: Union[Unset, int] = UNSET,
) -> Response[Any]:
    """Returns a list of observations for a given station

    Args:
        station_id (str):
        start (Union[Unset, datetime.datetime]):
        end (Union[Unset, datetime.datetime]):
        limit (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        station_id=station_id,
        start=start,
        end=end,
        limit=limit,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
