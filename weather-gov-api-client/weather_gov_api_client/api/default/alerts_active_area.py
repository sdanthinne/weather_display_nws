from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.marine_area_code import MarineAreaCode
from ...models.state_territory_code import StateTerritoryCode
from ...types import Response


def _get_kwargs(
    area: Union[MarineAreaCode, StateTerritoryCode],
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/alerts/active/area/{area}",
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
    area: Union[MarineAreaCode, StateTerritoryCode],
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[Any]:
    """Returns active alerts for the given area (state or marine area)

    Args:
        area (Union[MarineAreaCode, StateTerritoryCode]): State/territory codes and marine area
            codes

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        area=area,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    area: Union[MarineAreaCode, StateTerritoryCode],
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[Any]:
    """Returns active alerts for the given area (state or marine area)

    Args:
        area (Union[MarineAreaCode, StateTerritoryCode]): State/territory codes and marine area
            codes

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        area=area,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
