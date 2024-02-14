# coding: utf-8

"""
    Radarr

    Radarr API docs

    The version of the OpenAPI document: b08981dee068e1ed23e4f45a0d8fe70ef7bf7703
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import json
from enum import Enum
from typing_extensions import Self


class Modifier(str, Enum):
    """
    Modifier
    """

    """
    allowed enum values
    """
    NONE = 'none'
    REGIONAL = 'regional'
    SCREENER = 'screener'
    RAWHD = 'rawhd'
    BRDISK = 'brdisk'
    REMUX = 'remux'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of Modifier from a JSON string"""
        return cls(json.loads(json_str))


