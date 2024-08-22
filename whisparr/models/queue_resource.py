# coding: utf-8

"""
    Radarr

    Radarr API docs

    The version of the OpenAPI document: b08981dee068e1ed23e4f45a0d8fe70ef7bf7703
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictFloat, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional, Union
from whisparr.models.custom_format_resource import CustomFormatResource
from whisparr.models.download_protocol import DownloadProtocol
from whisparr.models.language import Language
from whisparr.models.movie_resource import MovieResource
from whisparr.models.quality_model import QualityModel
from whisparr.models.tracked_download_state import TrackedDownloadState
from whisparr.models.tracked_download_status import TrackedDownloadStatus
from whisparr.models.tracked_download_status_message import TrackedDownloadStatusMessage
from typing import Optional, Set
from typing_extensions import Self

class QueueResource(BaseModel):
    """
    QueueResource
    """ # noqa: E501
    id: Optional[StrictInt] = None
    movie_id: Optional[StrictInt] = Field(default=None, alias="movieId")
    movie: Optional[MovieResource] = None
    languages: Optional[List[Language]] = None
    quality: Optional[QualityModel] = None
    custom_formats: Optional[List[CustomFormatResource]] = Field(default=None, alias="customFormats")
    custom_format_score: Optional[StrictInt] = Field(default=None, alias="customFormatScore")
    size: Optional[Union[StrictFloat, StrictInt]] = None
    title: Optional[StrictStr] = None
    sizeleft: Optional[Union[StrictFloat, StrictInt]] = None
    timeleft: Optional[StrictStr] = None
    estimated_completion_time: Optional[datetime] = Field(default=None, alias="estimatedCompletionTime")
    added: Optional[datetime] = None
    status: Optional[StrictStr] = None
    tracked_download_status: Optional[TrackedDownloadStatus] = Field(default=None, alias="trackedDownloadStatus")
    tracked_download_state: Optional[TrackedDownloadState] = Field(default=None, alias="trackedDownloadState")
    status_messages: Optional[List[TrackedDownloadStatusMessage]] = Field(default=None, alias="statusMessages")
    error_message: Optional[StrictStr] = Field(default=None, alias="errorMessage")
    download_id: Optional[StrictStr] = Field(default=None, alias="downloadId")
    protocol: Optional[DownloadProtocol] = None
    download_client: Optional[StrictStr] = Field(default=None, alias="downloadClient")
    download_client_has_post_import_category: Optional[StrictBool] = Field(default=None, alias="downloadClientHasPostImportCategory")
    indexer: Optional[StrictStr] = None
    output_path: Optional[StrictStr] = Field(default=None, alias="outputPath")
    __properties: ClassVar[List[str]] = ["id", "movieId", "movie", "languages", "quality", "customFormats", "customFormatScore", "size", "title", "sizeleft", "timeleft", "estimatedCompletionTime", "added", "status", "trackedDownloadStatus", "trackedDownloadState", "statusMessages", "errorMessage", "downloadId", "protocol", "downloadClient", "downloadClientHasPostImportCategory", "indexer", "outputPath"]

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of QueueResource from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of movie
        if self.movie:
            _dict['movie'] = self.movie.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in languages (list)
        _items = []
        if self.languages:
            for _item_languages in self.languages:
                if _item_languages:
                    _items.append(_item_languages.to_dict())
            _dict['languages'] = _items
        # override the default output from pydantic by calling `to_dict()` of quality
        if self.quality:
            _dict['quality'] = self.quality.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in custom_formats (list)
        _items = []
        if self.custom_formats:
            for _item_custom_formats in self.custom_formats:
                if _item_custom_formats:
                    _items.append(_item_custom_formats.to_dict())
            _dict['customFormats'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in status_messages (list)
        _items = []
        if self.status_messages:
            for _item_status_messages in self.status_messages:
                if _item_status_messages:
                    _items.append(_item_status_messages.to_dict())
            _dict['statusMessages'] = _items
        # set to None if movie_id (nullable) is None
        # and model_fields_set contains the field
        if self.movie_id is None and "movie_id" in self.model_fields_set:
            _dict['movieId'] = None

        # set to None if languages (nullable) is None
        # and model_fields_set contains the field
        if self.languages is None and "languages" in self.model_fields_set:
            _dict['languages'] = None

        # set to None if custom_formats (nullable) is None
        # and model_fields_set contains the field
        if self.custom_formats is None and "custom_formats" in self.model_fields_set:
            _dict['customFormats'] = None

        # set to None if title (nullable) is None
        # and model_fields_set contains the field
        if self.title is None and "title" in self.model_fields_set:
            _dict['title'] = None

        # set to None if estimated_completion_time (nullable) is None
        # and model_fields_set contains the field
        if self.estimated_completion_time is None and "estimated_completion_time" in self.model_fields_set:
            _dict['estimatedCompletionTime'] = None

        # set to None if added (nullable) is None
        # and model_fields_set contains the field
        if self.added is None and "added" in self.model_fields_set:
            _dict['added'] = None

        # set to None if status (nullable) is None
        # and model_fields_set contains the field
        if self.status is None and "status" in self.model_fields_set:
            _dict['status'] = None

        # set to None if status_messages (nullable) is None
        # and model_fields_set contains the field
        if self.status_messages is None and "status_messages" in self.model_fields_set:
            _dict['statusMessages'] = None

        # set to None if error_message (nullable) is None
        # and model_fields_set contains the field
        if self.error_message is None and "error_message" in self.model_fields_set:
            _dict['errorMessage'] = None

        # set to None if download_id (nullable) is None
        # and model_fields_set contains the field
        if self.download_id is None and "download_id" in self.model_fields_set:
            _dict['downloadId'] = None

        # set to None if download_client (nullable) is None
        # and model_fields_set contains the field
        if self.download_client is None and "download_client" in self.model_fields_set:
            _dict['downloadClient'] = None

        # set to None if indexer (nullable) is None
        # and model_fields_set contains the field
        if self.indexer is None and "indexer" in self.model_fields_set:
            _dict['indexer'] = None

        # set to None if output_path (nullable) is None
        # and model_fields_set contains the field
        if self.output_path is None and "output_path" in self.model_fields_set:
            _dict['outputPath'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of QueueResource from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "movieId": obj.get("movieId"),
            "movie": MovieResource.from_dict(obj["movie"]) if obj.get("movie") is not None else None,
            "languages": [Language.from_dict(_item) for _item in obj["languages"]] if obj.get("languages") is not None else None,
            "quality": QualityModel.from_dict(obj["quality"]) if obj.get("quality") is not None else None,
            "customFormats": [CustomFormatResource.from_dict(_item) for _item in obj["customFormats"]] if obj.get("customFormats") is not None else None,
            "customFormatScore": obj.get("customFormatScore"),
            "size": obj.get("size"),
            "title": obj.get("title"),
            "sizeleft": obj.get("sizeleft"),
            "timeleft": obj.get("timeleft"),
            "estimatedCompletionTime": obj.get("estimatedCompletionTime"),
            "added": obj.get("added"),
            "status": obj.get("status"),
            "trackedDownloadStatus": obj.get("trackedDownloadStatus"),
            "trackedDownloadState": obj.get("trackedDownloadState"),
            "statusMessages": [TrackedDownloadStatusMessage.from_dict(_item) for _item in obj["statusMessages"]] if obj.get("statusMessages") is not None else None,
            "errorMessage": obj.get("errorMessage"),
            "downloadId": obj.get("downloadId"),
            "protocol": obj.get("protocol"),
            "downloadClient": obj.get("downloadClient"),
            "downloadClientHasPostImportCategory": obj.get("downloadClientHasPostImportCategory"),
            "indexer": obj.get("indexer"),
            "outputPath": obj.get("outputPath")
        })
        return _obj


