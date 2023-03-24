# coding: utf-8

"""
    Whisparr

    Whisparr API docs  # noqa: E501

    The version of the OpenAPI document: 3.0.0
    Generated by: https://openapi-generator.tech
"""


from __future__ import annotations
from inspect import getfullargspec
import pprint
import re  # noqa: F401
import json


from typing import List, Optional
from pydantic import BaseModel
from whisparr.models.profile_format_item_resource import ProfileFormatItemResource
from whisparr.models.quality_profile_quality_item_resource import QualityProfileQualityItemResource

class QualityProfileResource(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    id: Optional[int]
    name: Optional[str]
    upgrade_allowed: Optional[bool]
    cutoff: Optional[int]
    items: Optional[List]
    min_format_score: Optional[int]
    cutoff_format_score: Optional[int]
    format_items: Optional[List]
    __properties = ["id", "name", "upgradeAllowed", "cutoff", "items", "minFormatScore", "cutoffFormatScore", "formatItems"]

    class Config:
        allow_population_by_field_name = True
        validate_assignment = True
        alias_generator = lambda x: x.split("_")[0] + "".join(word.capitalize() for word in x.split("_")[1:])

    def __getitem__(self, item):
        return getattr(self, item)

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> QualityProfileResource:
        """Create an instance of QualityProfileResource from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in items (list)
        _items = []
        if self.items:
            for _item in self.items:
                if _item:
                    _items.append(_item.to_dict())
            _dict['items'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in format_items (list)
        _items = []
        if self.format_items:
            for _item in self.format_items:
                if _item:
                    _items.append(_item.to_dict())
            _dict['formatItems'] = _items
        # set to None if name (nullable) is None
        if self.name is None:
            _dict['name'] = None

        # set to None if items (nullable) is None
        if self.items is None:
            _dict['items'] = None

        # set to None if format_items (nullable) is None
        if self.format_items is None:
            _dict['formatItems'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> QualityProfileResource:
        """Create an instance of QualityProfileResource from a dict"""
        if obj is None:
            return None

        if type(obj) is not dict:
            return QualityProfileResource.parse_obj(obj)

        _obj = QualityProfileResource.parse_obj({
            "id": obj.get("id"),
            "name": obj.get("name"),
            "upgrade_allowed": obj.get("upgradeAllowed"),
            "cutoff": obj.get("cutoff"),
            "items": [QualityProfileQualityItemResource.from_dict(_item) for _item in obj.get("items")] if obj.get("items") is not None else None,
            "min_format_score": obj.get("minFormatScore"),
            "cutoff_format_score": obj.get("cutoffFormatScore"),
            "format_items": [ProfileFormatItemResource.from_dict(_item) for _item in obj.get("formatItems")] if obj.get("formatItems") is not None else None
        })
        return _obj

