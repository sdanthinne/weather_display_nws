from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="AlertsActiveCountResponse200Areas")


@_attrs_define
class AlertsActiveCountResponse200Areas:
    """Active alerts by area (state/territory)"""

    additional_properties: dict[str, int] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        alerts_active_count_response_200_areas = cls()

        alerts_active_count_response_200_areas.additional_properties = d
        return alerts_active_count_response_200_areas

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> int:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: int) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
