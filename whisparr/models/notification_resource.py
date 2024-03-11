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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from whisparr.models.contract_field import ContractField
from whisparr.models.provider_message import ProviderMessage
from typing import Optional, Set
from typing_extensions import Self

class NotificationResource(BaseModel):
    """
    NotificationResource
    """ # noqa: E501
    id: Optional[StrictInt] = None
    name: Optional[StrictStr] = None
    fields: Optional[List[ContractField]] = None
    implementation_name: Optional[StrictStr] = Field(default=None, alias="implementationName")
    implementation: Optional[StrictStr] = None
    config_contract: Optional[StrictStr] = Field(default=None, alias="configContract")
    info_link: Optional[StrictStr] = Field(default=None, alias="infoLink")
    message: Optional[ProviderMessage] = None
    tags: Optional[List[StrictInt]] = None
    presets: Optional[List[NotificationResource]] = None
    link: Optional[StrictStr] = None
    on_grab: Optional[StrictBool] = Field(default=None, alias="onGrab")
    on_download: Optional[StrictBool] = Field(default=None, alias="onDownload")
    on_upgrade: Optional[StrictBool] = Field(default=None, alias="onUpgrade")
    on_rename: Optional[StrictBool] = Field(default=None, alias="onRename")
    on_movie_added: Optional[StrictBool] = Field(default=None, alias="onMovieAdded")
    on_movie_delete: Optional[StrictBool] = Field(default=None, alias="onMovieDelete")
    on_movie_file_delete: Optional[StrictBool] = Field(default=None, alias="onMovieFileDelete")
    on_movie_file_delete_for_upgrade: Optional[StrictBool] = Field(default=None, alias="onMovieFileDeleteForUpgrade")
    on_health_issue: Optional[StrictBool] = Field(default=None, alias="onHealthIssue")
    on_health_restored: Optional[StrictBool] = Field(default=None, alias="onHealthRestored")
    on_application_update: Optional[StrictBool] = Field(default=None, alias="onApplicationUpdate")
    on_manual_interaction_required: Optional[StrictBool] = Field(default=None, alias="onManualInteractionRequired")
    supports_on_grab: Optional[StrictBool] = Field(default=None, alias="supportsOnGrab")
    supports_on_download: Optional[StrictBool] = Field(default=None, alias="supportsOnDownload")
    supports_on_upgrade: Optional[StrictBool] = Field(default=None, alias="supportsOnUpgrade")
    supports_on_rename: Optional[StrictBool] = Field(default=None, alias="supportsOnRename")
    supports_on_movie_added: Optional[StrictBool] = Field(default=None, alias="supportsOnMovieAdded")
    supports_on_movie_delete: Optional[StrictBool] = Field(default=None, alias="supportsOnMovieDelete")
    supports_on_movie_file_delete: Optional[StrictBool] = Field(default=None, alias="supportsOnMovieFileDelete")
    supports_on_movie_file_delete_for_upgrade: Optional[StrictBool] = Field(default=None, alias="supportsOnMovieFileDeleteForUpgrade")
    supports_on_health_issue: Optional[StrictBool] = Field(default=None, alias="supportsOnHealthIssue")
    supports_on_health_restored: Optional[StrictBool] = Field(default=None, alias="supportsOnHealthRestored")
    supports_on_application_update: Optional[StrictBool] = Field(default=None, alias="supportsOnApplicationUpdate")
    supports_on_manual_interaction_required: Optional[StrictBool] = Field(default=None, alias="supportsOnManualInteractionRequired")
    include_health_warnings: Optional[StrictBool] = Field(default=None, alias="includeHealthWarnings")
    test_command: Optional[StrictStr] = Field(default=None, alias="testCommand")
    __properties: ClassVar[List[str]] = ["id", "name", "fields", "implementationName", "implementation", "configContract", "infoLink", "message", "tags", "presets", "link", "onGrab", "onDownload", "onUpgrade", "onRename", "onMovieAdded", "onMovieDelete", "onMovieFileDelete", "onMovieFileDeleteForUpgrade", "onHealthIssue", "onHealthRestored", "onApplicationUpdate", "onManualInteractionRequired", "supportsOnGrab", "supportsOnDownload", "supportsOnUpgrade", "supportsOnRename", "supportsOnMovieAdded", "supportsOnMovieDelete", "supportsOnMovieFileDelete", "supportsOnMovieFileDeleteForUpgrade", "supportsOnHealthIssue", "supportsOnHealthRestored", "supportsOnApplicationUpdate", "supportsOnManualInteractionRequired", "includeHealthWarnings", "testCommand"]

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
        """Create an instance of NotificationResource from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in fields (list)
        _items = []
        if self.fields:
            for _item in self.fields:
                if _item:
                    _items.append(_item.to_dict())
            _dict['fields'] = _items
        # override the default output from pydantic by calling `to_dict()` of message
        if self.message:
            _dict['message'] = self.message.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in presets (list)
        _items = []
        if self.presets:
            for _item in self.presets:
                if _item:
                    _items.append(_item.to_dict())
            _dict['presets'] = _items
        # set to None if name (nullable) is None
        # and model_fields_set contains the field
        if self.name is None and "name" in self.model_fields_set:
            _dict['name'] = None

        # set to None if fields (nullable) is None
        # and model_fields_set contains the field
        if self.fields is None and "fields" in self.model_fields_set:
            _dict['fields'] = None

        # set to None if implementation_name (nullable) is None
        # and model_fields_set contains the field
        if self.implementation_name is None and "implementation_name" in self.model_fields_set:
            _dict['implementationName'] = None

        # set to None if implementation (nullable) is None
        # and model_fields_set contains the field
        if self.implementation is None and "implementation" in self.model_fields_set:
            _dict['implementation'] = None

        # set to None if config_contract (nullable) is None
        # and model_fields_set contains the field
        if self.config_contract is None and "config_contract" in self.model_fields_set:
            _dict['configContract'] = None

        # set to None if info_link (nullable) is None
        # and model_fields_set contains the field
        if self.info_link is None and "info_link" in self.model_fields_set:
            _dict['infoLink'] = None

        # set to None if tags (nullable) is None
        # and model_fields_set contains the field
        if self.tags is None and "tags" in self.model_fields_set:
            _dict['tags'] = None

        # set to None if presets (nullable) is None
        # and model_fields_set contains the field
        if self.presets is None and "presets" in self.model_fields_set:
            _dict['presets'] = None

        # set to None if link (nullable) is None
        # and model_fields_set contains the field
        if self.link is None and "link" in self.model_fields_set:
            _dict['link'] = None

        # set to None if test_command (nullable) is None
        # and model_fields_set contains the field
        if self.test_command is None and "test_command" in self.model_fields_set:
            _dict['testCommand'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of NotificationResource from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "name": obj.get("name"),
            "fields": [ContractField.from_dict(_item) for _item in obj["fields"]] if obj.get("fields") is not None else None,
            "implementationName": obj.get("implementationName"),
            "implementation": obj.get("implementation"),
            "configContract": obj.get("configContract"),
            "infoLink": obj.get("infoLink"),
            "message": ProviderMessage.from_dict(obj["message"]) if obj.get("message") is not None else None,
            "tags": obj.get("tags"),
            "presets": [NotificationResource.from_dict(_item) for _item in obj["presets"]] if obj.get("presets") is not None else None,
            "link": obj.get("link"),
            "onGrab": obj.get("onGrab"),
            "onDownload": obj.get("onDownload"),
            "onUpgrade": obj.get("onUpgrade"),
            "onRename": obj.get("onRename"),
            "onMovieAdded": obj.get("onMovieAdded"),
            "onMovieDelete": obj.get("onMovieDelete"),
            "onMovieFileDelete": obj.get("onMovieFileDelete"),
            "onMovieFileDeleteForUpgrade": obj.get("onMovieFileDeleteForUpgrade"),
            "onHealthIssue": obj.get("onHealthIssue"),
            "onHealthRestored": obj.get("onHealthRestored"),
            "onApplicationUpdate": obj.get("onApplicationUpdate"),
            "onManualInteractionRequired": obj.get("onManualInteractionRequired"),
            "supportsOnGrab": obj.get("supportsOnGrab"),
            "supportsOnDownload": obj.get("supportsOnDownload"),
            "supportsOnUpgrade": obj.get("supportsOnUpgrade"),
            "supportsOnRename": obj.get("supportsOnRename"),
            "supportsOnMovieAdded": obj.get("supportsOnMovieAdded"),
            "supportsOnMovieDelete": obj.get("supportsOnMovieDelete"),
            "supportsOnMovieFileDelete": obj.get("supportsOnMovieFileDelete"),
            "supportsOnMovieFileDeleteForUpgrade": obj.get("supportsOnMovieFileDeleteForUpgrade"),
            "supportsOnHealthIssue": obj.get("supportsOnHealthIssue"),
            "supportsOnHealthRestored": obj.get("supportsOnHealthRestored"),
            "supportsOnApplicationUpdate": obj.get("supportsOnApplicationUpdate"),
            "supportsOnManualInteractionRequired": obj.get("supportsOnManualInteractionRequired"),
            "includeHealthWarnings": obj.get("includeHealthWarnings"),
            "testCommand": obj.get("testCommand")
        })
        return _obj

# TODO: Rewrite to not use raise_errors
NotificationResource.model_rebuild(raise_errors=False)

