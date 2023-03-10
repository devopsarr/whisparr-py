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


from typing import Optional
from pydantic import BaseModel

class MediaInfoResource(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    id: Optional[int]
    audio_bitrate: Optional[int]
    audio_channels: Optional[float]
    audio_codec: Optional[str]
    audio_languages: Optional[str]
    audio_stream_count: Optional[int]
    video_bit_depth: Optional[int]
    video_bitrate: Optional[int]
    video_codec: Optional[str]
    video_dynamic_range_type: Optional[str]
    video_fps: Optional[float]
    resolution: Optional[str]
    run_time: Optional[str]
    scan_type: Optional[str]
    subtitles: Optional[str]
    __properties = ["id", "audioBitrate", "audioChannels", "audioCodec", "audioLanguages", "audioStreamCount", "videoBitDepth", "videoBitrate", "videoCodec", "videoDynamicRangeType", "videoFps", "resolution", "runTime", "scanType", "subtitles"]

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
    def from_json(cls, json_str: str) -> MediaInfoResource:
        """Create an instance of MediaInfoResource from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # set to None if audio_codec (nullable) is None
        if self.audio_codec is None:
            _dict['audioCodec'] = None

        # set to None if audio_languages (nullable) is None
        if self.audio_languages is None:
            _dict['audioLanguages'] = None

        # set to None if video_codec (nullable) is None
        if self.video_codec is None:
            _dict['videoCodec'] = None

        # set to None if video_dynamic_range_type (nullable) is None
        if self.video_dynamic_range_type is None:
            _dict['videoDynamicRangeType'] = None

        # set to None if resolution (nullable) is None
        if self.resolution is None:
            _dict['resolution'] = None

        # set to None if run_time (nullable) is None
        if self.run_time is None:
            _dict['runTime'] = None

        # set to None if scan_type (nullable) is None
        if self.scan_type is None:
            _dict['scanType'] = None

        # set to None if subtitles (nullable) is None
        if self.subtitles is None:
            _dict['subtitles'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> MediaInfoResource:
        """Create an instance of MediaInfoResource from a dict"""
        if obj is None:
            return None

        if type(obj) is not dict:
            return MediaInfoResource.parse_obj(obj)

        _obj = MediaInfoResource.parse_obj({
            "id": obj.get("id"),
            "audio_bitrate": obj.get("audioBitrate"),
            "audio_channels": obj.get("audioChannels"),
            "audio_codec": obj.get("audioCodec"),
            "audio_languages": obj.get("audioLanguages"),
            "audio_stream_count": obj.get("audioStreamCount"),
            "video_bit_depth": obj.get("videoBitDepth"),
            "video_bitrate": obj.get("videoBitrate"),
            "video_codec": obj.get("videoCodec"),
            "video_dynamic_range_type": obj.get("videoDynamicRangeType"),
            "video_fps": obj.get("videoFps"),
            "resolution": obj.get("resolution"),
            "run_time": obj.get("runTime"),
            "scan_type": obj.get("scanType"),
            "subtitles": obj.get("subtitles")
        })
        return _obj

