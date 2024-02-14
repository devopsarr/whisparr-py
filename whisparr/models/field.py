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

from pydantic import BaseModel, Field, StrictBool, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from whisparr.models.privacy_level import PrivacyLevel
from whisparr.models.select_option import SelectOption
from typing import Optional, Set
from typing_extensions import Self

class Field(BaseModel):
    """
    Field
    """ # noqa: E501
    order: Optional[StrictInt] = None
    name: Optional[StrictStr] = None
    label: Optional[StrictStr] = None
    unit: Optional[StrictStr] = None
    help_text: Optional[StrictStr] = Field(default=None, alias="helpText")
    help_text_warning: Optional[StrictStr] = Field(default=None, alias="helpTextWarning")
    help_link: Optional[StrictStr] = Field(default=None, alias="helpLink")
    value: Optional[Any] = None
    type: Optional[StrictStr] = None
    advanced: Optional[StrictBool] = None
    select_options: Optional[List[SelectOption]] = Field(default=None, alias="selectOptions")
    select_options_provider_action: Optional[StrictStr] = Field(default=None, alias="selectOptionsProviderAction")
    section: Optional[StrictStr] = None
    hidden: Optional[StrictStr] = None
    privacy: Optional[PrivacyLevel] = None
    placeholder: Optional[StrictStr] = None
    is_float: Optional[StrictBool] = Field(default=None, alias="isFloat")
    __properties: ClassVar[List[str]] = ["order", "name", "label", "unit", "helpText", "helpTextWarning", "helpLink", "value", "type", "advanced", "selectOptions", "selectOptionsProviderAction", "section", "hidden", "privacy", "placeholder", "isFloat"]

    model_config = {
        "populate_by_name": True,
        "validate_assignment": True,
        "protected_namespaces": (),
    }


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of Field from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in select_options (list)
        _items = []
        if self.select_options:
            for _item in self.select_options:
                if _item:
                    _items.append(_item.to_dict())
            _dict['selectOptions'] = _items
        # set to None if name (nullable) is None
        # and model_fields_set contains the field
        if self.name is None and "name" in self.model_fields_set:
            _dict['name'] = None

        # set to None if label (nullable) is None
        # and model_fields_set contains the field
        if self.label is None and "label" in self.model_fields_set:
            _dict['label'] = None

        # set to None if unit (nullable) is None
        # and model_fields_set contains the field
        if self.unit is None and "unit" in self.model_fields_set:
            _dict['unit'] = None

        # set to None if help_text (nullable) is None
        # and model_fields_set contains the field
        if self.help_text is None and "help_text" in self.model_fields_set:
            _dict['helpText'] = None

        # set to None if help_text_warning (nullable) is None
        # and model_fields_set contains the field
        if self.help_text_warning is None and "help_text_warning" in self.model_fields_set:
            _dict['helpTextWarning'] = None

        # set to None if help_link (nullable) is None
        # and model_fields_set contains the field
        if self.help_link is None and "help_link" in self.model_fields_set:
            _dict['helpLink'] = None

        # set to None if value (nullable) is None
        # and model_fields_set contains the field
        if self.value is None and "value" in self.model_fields_set:
            _dict['value'] = None

        # set to None if type (nullable) is None
        # and model_fields_set contains the field
        if self.type is None and "type" in self.model_fields_set:
            _dict['type'] = None

        # set to None if select_options (nullable) is None
        # and model_fields_set contains the field
        if self.select_options is None and "select_options" in self.model_fields_set:
            _dict['selectOptions'] = None

        # set to None if select_options_provider_action (nullable) is None
        # and model_fields_set contains the field
        if self.select_options_provider_action is None and "select_options_provider_action" in self.model_fields_set:
            _dict['selectOptionsProviderAction'] = None

        # set to None if section (nullable) is None
        # and model_fields_set contains the field
        if self.section is None and "section" in self.model_fields_set:
            _dict['section'] = None

        # set to None if hidden (nullable) is None
        # and model_fields_set contains the field
        if self.hidden is None and "hidden" in self.model_fields_set:
            _dict['hidden'] = None

        # set to None if placeholder (nullable) is None
        # and model_fields_set contains the field
        if self.placeholder is None and "placeholder" in self.model_fields_set:
            _dict['placeholder'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of Field from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "order": obj.get("order"),
            "name": obj.get("name"),
            "label": obj.get("label"),
            "unit": obj.get("unit"),
            "helpText": obj.get("helpText"),
            "helpTextWarning": obj.get("helpTextWarning"),
            "helpLink": obj.get("helpLink"),
            "value": obj.get("value"),
            "type": obj.get("type"),
            "advanced": obj.get("advanced"),
            "selectOptions": [SelectOption.from_dict(_item) for _item in obj["selectOptions"]] if obj.get("selectOptions") is not None else None,
            "selectOptionsProviderAction": obj.get("selectOptionsProviderAction"),
            "section": obj.get("section"),
            "hidden": obj.get("hidden"),
            "privacy": obj.get("privacy"),
            "placeholder": obj.get("placeholder"),
            "isFloat": obj.get("isFloat")
        })
        return _obj


