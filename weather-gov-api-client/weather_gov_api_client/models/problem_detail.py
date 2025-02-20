from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="ProblemDetail")


@_attrs_define
class ProblemDetail:
    """Detail about an error. This document conforms to RFC 7807 (Problem Details for HTTP APIs).

    Attributes:
        type_ (str): A URI reference (RFC 3986) that identifies the problem type. This is only an identifier and is not
            necessarily a resolvable URL.
             Default: 'about:blank'. Example: urn:noaa:nws:api:UnexpectedProblem.
        title (str): A short, human-readable summary of the problem type. Example: Unexpected Problem.
        status (float): The HTTP status code (RFC 7231, Section 6) generated by the origin server for this occurrence of
            the problem.
             Example: 500.
        detail (str): A human-readable explanation specific to this occurrence of the problem. Example: An unexpected
            problem has occurred..
        instance (str): A URI reference (RFC 3986) that identifies the specific occurrence of the problem. This is only
            an identifier and is not necessarily a resolvable URL.
             Example: urn:noaa:nws:api:request:493c3a1d-f87e-407f-ae2c-24483f5aab63.
        correlation_id (str): A unique identifier for the request, used for NWS debugging purposes. Please include this
            identifier with any correspondence to help us investigate your issue.
             Example: 493c3a1d-f87e-407f-ae2c-24483f5aab63.
    """

    title: str
    status: float
    detail: str
    instance: str
    correlation_id: str
    type_: str = "about:blank"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_

        title = self.title

        status = self.status

        detail = self.detail

        instance = self.instance

        correlation_id = self.correlation_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
                "title": title,
                "status": status,
                "detail": detail,
                "instance": instance,
                "correlationId": correlation_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        type_ = d.pop("type")

        title = d.pop("title")

        status = d.pop("status")

        detail = d.pop("detail")

        instance = d.pop("instance")

        correlation_id = d.pop("correlationId")

        problem_detail = cls(
            type_=type_,
            title=title,
            status=status,
            detail=detail,
            instance=instance,
            correlation_id=correlation_id,
        )

        problem_detail.additional_properties = d
        return problem_detail

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
