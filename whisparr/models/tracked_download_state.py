# coding: utf-8

"""
    Radarr

    Radarr API docs  # noqa: E501

    The version of the OpenAPI document: 3.0.0
    Generated by: https://openapi-generator.tech
"""


from inspect import getfullargspec
import pprint
import re  # noqa: F401
from aenum import Enum, no_arg





class TrackedDownloadState(str, Enum):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    allowed enum values
    """

    DOWNLOADING = 'downloading'
    IMPORTPENDING = 'importPending'
    IMPORTING = 'importing'
    IMPORTED = 'imported'
    FAILEDPENDING = 'failedPending'
    FAILED = 'failed'
    IGNORED = 'ignored'

