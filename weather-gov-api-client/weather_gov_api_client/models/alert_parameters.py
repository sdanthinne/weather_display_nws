from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="AlertParameters")


@_attrs_define
class AlertParameters:
    """System-specific additional parameters associated with the alert message.
    The keys in this object correspond to parameter definitions in the NWS CAP specification.

    """

    additional_properties: dict[str, list[Any]] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        field_dict: dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():
            field_dict[prop_name] = prop

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        alert_parameters = cls()

        additional_properties = {}
        for prop_name, prop_dict in d.items():
            additional_property = cast(list[Any], prop_dict)

            additional_properties[prop_name] = additional_property

        alert_parameters.additional_properties = additional_properties
        return alert_parameters

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> list[Any]:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: list[Any]) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
