# coding: utf-8

"""
    Radarr

    Radarr API docs  # noqa: E501

    The version of the OpenAPI document: 3.0.0
    Generated by: https://openapi-generator.tech
"""


from __future__ import annotations
from inspect import getfullargspec
import pprint
import re  # noqa: F401
import json

from datetime import datetime
from typing import Any, ClassVar, Dict, List, Optional
from pydantic import BaseModel
from whisparr.models.custom_format_resource import CustomFormatResource
from whisparr.models.language import Language
from whisparr.models.movie_history_event_type import MovieHistoryEventType
from whisparr.models.movie_resource import MovieResource
from whisparr.models.quality_model import QualityModel

class HistoryResource(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    id: Optional[int]
    movie_id: Optional[int]
    source_title: Optional[str]
    languages: Optional[List]
    quality: Optional[QualityModel]
    custom_formats: Optional[List]
    custom_format_score: Optional[int]
    quality_cutoff_not_met: Optional[bool]
    var_date: Optional[datetime]
    download_id: Optional[str]
    event_type: Optional[MovieHistoryEventType]
    data: Optional[Dict]
    movie: Optional[MovieResource]
    __properties = ["id", "movieId", "sourceTitle", "languages", "quality", "customFormats", "customFormatScore", "qualityCutoffNotMet", "date", "downloadId", "eventType", "data", "movie"]

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
    def from_json(cls, json_str: str) -> HistoryResource:
        """Create an instance of HistoryResource from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in languages (list)
        _items = []
        if self.languages:
            for _item in self.languages:
                if _item:
                    _items.append(_item.to_dict())
            _dict['languages'] = _items
        # override the default output from pydantic by calling `to_dict()` of quality
        if self.quality:
            _dict['quality'] = self.quality.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in custom_formats (list)
        _items = []
        if self.custom_formats:
            for _item in self.custom_formats:
                if _item:
                    _items.append(_item.to_dict())
            _dict['customFormats'] = _items
        # override the default output from pydantic by calling `to_dict()` of movie
        if self.movie:
            _dict['movie'] = self.movie.to_dict()
        # set to None if source_title (nullable) is None
        if self.source_title is None:
            _dict['sourceTitle'] = None

        # set to None if languages (nullable) is None
        if self.languages is None:
            _dict['languages'] = None

        # set to None if custom_formats (nullable) is None
        if self.custom_formats is None:
            _dict['customFormats'] = None

        # set to None if download_id (nullable) is None
        if self.download_id is None:
            _dict['downloadId'] = None

        # set to None if data (nullable) is None
        if self.data is None:
            _dict['data'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> HistoryResource:
        """Create an instance of HistoryResource from a dict"""
        if obj is None:
            return None

        if type(obj) is not dict:
            return HistoryResource.parse_obj(obj)

        _obj = HistoryResource.parse_obj({
            "id": obj.get("id"),
            "movie_id": obj.get("movieId"),
            "source_title": obj.get("sourceTitle"),
            "languages": [Language.from_dict(_item) for _item in obj.get("languages")] if obj.get("languages") is not None else None,
            "quality": QualityModel.from_dict(obj.get("quality")) if obj.get("quality") is not None else None,
            "custom_formats": [CustomFormatResource.from_dict(_item) for _item in obj.get("customFormats")] if obj.get("customFormats") is not None else None,
            "custom_format_score": obj.get("customFormatScore"),
            "quality_cutoff_not_met": obj.get("qualityCutoffNotMet"),
            "var_date": obj.get("date"),
            "download_id": obj.get("downloadId"),
            "event_type": obj.get("eventType"),
            "data": obj.get("data"),
            "movie": MovieResource.from_dict(obj.get("movie")) if obj.get("movie") is not None else None
        })
        return _obj

