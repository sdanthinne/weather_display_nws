from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.gridpoint_weather_values_item import GridpointWeatherValuesItem


T = TypeVar("T", bound="GridpointWeather")


@_attrs_define
class GridpointWeather:
    """
    Attributes:
        values (list['GridpointWeatherValuesItem']):
    """

    values: list["GridpointWeatherValuesItem"]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        values = []
        for values_item_data in self.values:
            values_item = values_item_data.to_dict()
            values.append(values_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "values": values,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.gridpoint_weather_values_item import GridpointWeatherValuesItem

        d = src_dict.copy()
        values = []
        _values = d.pop("values")
        for values_item_data in _values:
            values_item = GridpointWeatherValuesItem.from_dict(values_item_data)

            values.append(values_item)

        gridpoint_weather = cls(
            values=values,
        )

        gridpoint_weather.additional_properties = d
        return gridpoint_weather

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
