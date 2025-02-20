from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.nws_forecast_office_id import NWSForecastOfficeId
from ...models.nws_national_hq_id import NWSNationalHQId
from ...models.nws_regional_hq_id import NWSRegionalHQId
from ...types import Response


def _get_kwargs(
    office_id: Union[NWSForecastOfficeId, NWSNationalHQId, NWSRegionalHQId],
    headline_id: str,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/offices/{office_id}/headlines/{headline_id}",
    }

    return _kwargs


def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[Any]:
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
    office_id: Union[NWSForecastOfficeId, NWSNationalHQId, NWSRegionalHQId],
    headline_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[Any]:
    """Returns a specific news headline for a given NWS office

    Args:
        office_id (Union[NWSForecastOfficeId, NWSNationalHQId, NWSRegionalHQId]):
        headline_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        office_id=office_id,
        headline_id=headline_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    office_id: Union[NWSForecastOfficeId, NWSNationalHQId, NWSRegionalHQId],
    headline_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[Any]:
    """Returns a specific news headline for a given NWS office

    Args:
        office_id (Union[NWSForecastOfficeId, NWSNationalHQId, NWSRegionalHQId]):
        headline_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        office_id=office_id,
        headline_id=headline_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
