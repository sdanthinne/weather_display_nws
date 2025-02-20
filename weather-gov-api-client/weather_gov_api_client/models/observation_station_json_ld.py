from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.observation_station_type import ObservationStationType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.json_ld_context_type_1 import JsonLdContextType1
    from ..models.quantitative_value import QuantitativeValue


T = TypeVar("T", bound="ObservationStationJsonLd")


@_attrs_define
class ObservationStationJsonLd:
    """
    Attributes:
        context (Union['JsonLdContextType1', list[Any]]):
        geometry (Union[None, str]): A geometry represented in Well-Known Text (WKT) format.
        id (Union[Unset, str]):
        type_ (Union[Unset, ObservationStationType]):
        elevation (Union[Unset, QuantitativeValue]): A structured value representing a measurement and its unit of
            measure. This object is a slighly modified version of the schema.org definition at
            https://schema.org/QuantitativeValue
        station_identifier (Union[Unset, str]):
        name (Union[Unset, str]):
        time_zone (Union[Unset, str]):
        forecast (Union[Unset, str]): A link to the NWS public forecast zone containing this station.
        county (Union[Unset, str]): A link to the NWS county zone containing this station.
        fire_weather_zone (Union[Unset, str]): A link to the NWS fire weather forecast zone containing this station.
    """

    context: Union["JsonLdContextType1", list[Any]]
    geometry: Union[None, str]
    id: Union[Unset, str] = UNSET
    type_: Union[Unset, ObservationStationType] = UNSET
    elevation: Union[Unset, "QuantitativeValue"] = UNSET
    station_identifier: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    time_zone: Union[Unset, str] = UNSET
    forecast: Union[Unset, str] = UNSET
    county: Union[Unset, str] = UNSET
    fire_weather_zone: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        context: Union[dict[str, Any], list[Any]]
        if isinstance(self.context, list):
            context = self.context

        else:
            context = self.context.to_dict()

        geometry: Union[None, str]
        geometry = self.geometry

        id = self.id

        type_: Union[Unset, str] = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        elevation: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.elevation, Unset):
            elevation = self.elevation.to_dict()

        station_identifier = self.station_identifier

        name = self.name

        time_zone = self.time_zone

        forecast = self.forecast

        county = self.county

        fire_weather_zone = self.fire_weather_zone

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "@context": context,
                "geometry": geometry,
            }
        )
        if id is not UNSET:
            field_dict["@id"] = id
        if type_ is not UNSET:
            field_dict["@type"] = type_
        if elevation is not UNSET:
            field_dict["elevation"] = elevation
        if station_identifier is not UNSET:
            field_dict["stationIdentifier"] = station_identifier
        if name is not UNSET:
            field_dict["name"] = name
        if time_zone is not UNSET:
            field_dict["timeZone"] = time_zone
        if forecast is not UNSET:
            field_dict["forecast"] = forecast
        if county is not UNSET:
            field_dict["county"] = county
        if fire_weather_zone is not UNSET:
            field_dict["fireWeatherZone"] = fire_weather_zone

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.json_ld_context_type_1 import JsonLdContextType1
        from ..models.quantitative_value import QuantitativeValue

        d = src_dict.copy()

        def _parse_context(data: object) -> Union["JsonLdContextType1", list[Any]]:
            try:
                if not isinstance(data, list):
                    raise TypeError()
                componentsschemas_json_ld_context_type_0 = cast(list[Any], data)

                return componentsschemas_json_ld_context_type_0
            except:  # noqa: E722
                pass
            if not isinstance(data, dict):
                raise TypeError()
            componentsschemas_json_ld_context_type_1 = JsonLdContextType1.from_dict(data)

            return componentsschemas_json_ld_context_type_1

        context = _parse_context(d.pop("@context"))

        def _parse_geometry(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        geometry = _parse_geometry(d.pop("geometry"))

        id = d.pop("@id", UNSET)

        _type_ = d.pop("@type", UNSET)
        type_: Union[Unset, ObservationStationType]
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = ObservationStationType(_type_)

        _elevation = d.pop("elevation", UNSET)
        elevation: Union[Unset, QuantitativeValue]
        if isinstance(_elevation, Unset):
            elevation = UNSET
        else:
            elevation = QuantitativeValue.from_dict(_elevation)

        station_identifier = d.pop("stationIdentifier", UNSET)

        name = d.pop("name", UNSET)

        time_zone = d.pop("timeZone", UNSET)

        forecast = d.pop("forecast", UNSET)

        county = d.pop("county", UNSET)

        fire_weather_zone = d.pop("fireWeatherZone", UNSET)

        observation_station_json_ld = cls(
            context=context,
            geometry=geometry,
            id=id,
            type_=type_,
            elevation=elevation,
            station_identifier=station_identifier,
            name=name,
            time_zone=time_zone,
            forecast=forecast,
            county=county,
            fire_weather_zone=fire_weather_zone,
        )

        observation_station_json_ld.additional_properties = d
        return observation_station_json_ld

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
