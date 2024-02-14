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
from typing import Any, ClassVar, Dict, Optional
from whisparr.models.authentication_required_type import AuthenticationRequiredType
from whisparr.models.authentication_type import AuthenticationType
from whisparr.models.certificate_validation_type import CertificateValidationType
from whisparr.models.proxy_type import ProxyType
from whisparr.models.update_mechanism import UpdateMechanism
from typing import Optional, Set
from typing_extensions import Self

class HostConfigResource(BaseModel):
    """
    HostConfigResource
    """ # noqa: E501
    id: Optional[StrictInt] = None
    bind_address: Optional[StrictStr] = Field(default=None, alias="bindAddress")
    port: Optional[StrictInt] = None
    ssl_port: Optional[StrictInt] = Field(default=None, alias="sslPort")
    enable_ssl: Optional[StrictBool] = Field(default=None, alias="enableSsl")
    launch_browser: Optional[StrictBool] = Field(default=None, alias="launchBrowser")
    authentication_method: Optional[AuthenticationType] = Field(default=None, alias="authenticationMethod")
    authentication_required: Optional[AuthenticationRequiredType] = Field(default=None, alias="authenticationRequired")
    analytics_enabled: Optional[StrictBool] = Field(default=None, alias="analyticsEnabled")
    username: Optional[StrictStr] = None
    password: Optional[StrictStr] = None
    password_confirmation: Optional[StrictStr] = Field(default=None, alias="passwordConfirmation")
    log_level: Optional[StrictStr] = Field(default=None, alias="logLevel")
    console_log_level: Optional[StrictStr] = Field(default=None, alias="consoleLogLevel")
    branch: Optional[StrictStr] = None
    api_key: Optional[StrictStr] = Field(default=None, alias="apiKey")
    ssl_cert_path: Optional[StrictStr] = Field(default=None, alias="sslCertPath")
    ssl_cert_password: Optional[StrictStr] = Field(default=None, alias="sslCertPassword")
    url_base: Optional[StrictStr] = Field(default=None, alias="urlBase")
    instance_name: Optional[StrictStr] = Field(default=None, alias="instanceName")
    application_url: Optional[StrictStr] = Field(default=None, alias="applicationUrl")
    update_automatically: Optional[StrictBool] = Field(default=None, alias="updateAutomatically")
    update_mechanism: Optional[UpdateMechanism] = Field(default=None, alias="updateMechanism")
    update_script_path: Optional[StrictStr] = Field(default=None, alias="updateScriptPath")
    proxy_enabled: Optional[StrictBool] = Field(default=None, alias="proxyEnabled")
    proxy_type: Optional[ProxyType] = Field(default=None, alias="proxyType")
    proxy_hostname: Optional[StrictStr] = Field(default=None, alias="proxyHostname")
    proxy_port: Optional[StrictInt] = Field(default=None, alias="proxyPort")
    proxy_username: Optional[StrictStr] = Field(default=None, alias="proxyUsername")
    proxy_password: Optional[StrictStr] = Field(default=None, alias="proxyPassword")
    proxy_bypass_filter: Optional[StrictStr] = Field(default=None, alias="proxyBypassFilter")
    proxy_bypass_local_addresses: Optional[StrictBool] = Field(default=None, alias="proxyBypassLocalAddresses")
    certificate_validation: Optional[CertificateValidationType] = Field(default=None, alias="certificateValidation")
    backup_folder: Optional[StrictStr] = Field(default=None, alias="backupFolder")
    backup_interval: Optional[StrictInt] = Field(default=None, alias="backupInterval")
    backup_retention: Optional[StrictInt] = Field(default=None, alias="backupRetention")
    __properties: ClassVar[List[str]] = ["id", "bindAddress", "port", "sslPort", "enableSsl", "launchBrowser", "authenticationMethod", "authenticationRequired", "analyticsEnabled", "username", "password", "passwordConfirmation", "logLevel", "consoleLogLevel", "branch", "apiKey", "sslCertPath", "sslCertPassword", "urlBase", "instanceName", "applicationUrl", "updateAutomatically", "updateMechanism", "updateScriptPath", "proxyEnabled", "proxyType", "proxyHostname", "proxyPort", "proxyUsername", "proxyPassword", "proxyBypassFilter", "proxyBypassLocalAddresses", "certificateValidation", "backupFolder", "backupInterval", "backupRetention"]

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
        """Create an instance of HostConfigResource from a JSON string"""
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
        # set to None if bind_address (nullable) is None
        # and model_fields_set contains the field
        if self.bind_address is None and "bind_address" in self.model_fields_set:
            _dict['bindAddress'] = None

        # set to None if username (nullable) is None
        # and model_fields_set contains the field
        if self.username is None and "username" in self.model_fields_set:
            _dict['username'] = None

        # set to None if password (nullable) is None
        # and model_fields_set contains the field
        if self.password is None and "password" in self.model_fields_set:
            _dict['password'] = None

        # set to None if password_confirmation (nullable) is None
        # and model_fields_set contains the field
        if self.password_confirmation is None and "password_confirmation" in self.model_fields_set:
            _dict['passwordConfirmation'] = None

        # set to None if log_level (nullable) is None
        # and model_fields_set contains the field
        if self.log_level is None and "log_level" in self.model_fields_set:
            _dict['logLevel'] = None

        # set to None if console_log_level (nullable) is None
        # and model_fields_set contains the field
        if self.console_log_level is None and "console_log_level" in self.model_fields_set:
            _dict['consoleLogLevel'] = None

        # set to None if branch (nullable) is None
        # and model_fields_set contains the field
        if self.branch is None and "branch" in self.model_fields_set:
            _dict['branch'] = None

        # set to None if api_key (nullable) is None
        # and model_fields_set contains the field
        if self.api_key is None and "api_key" in self.model_fields_set:
            _dict['apiKey'] = None

        # set to None if ssl_cert_path (nullable) is None
        # and model_fields_set contains the field
        if self.ssl_cert_path is None and "ssl_cert_path" in self.model_fields_set:
            _dict['sslCertPath'] = None

        # set to None if ssl_cert_password (nullable) is None
        # and model_fields_set contains the field
        if self.ssl_cert_password is None and "ssl_cert_password" in self.model_fields_set:
            _dict['sslCertPassword'] = None

        # set to None if url_base (nullable) is None
        # and model_fields_set contains the field
        if self.url_base is None and "url_base" in self.model_fields_set:
            _dict['urlBase'] = None

        # set to None if instance_name (nullable) is None
        # and model_fields_set contains the field
        if self.instance_name is None and "instance_name" in self.model_fields_set:
            _dict['instanceName'] = None

        # set to None if application_url (nullable) is None
        # and model_fields_set contains the field
        if self.application_url is None and "application_url" in self.model_fields_set:
            _dict['applicationUrl'] = None

        # set to None if update_script_path (nullable) is None
        # and model_fields_set contains the field
        if self.update_script_path is None and "update_script_path" in self.model_fields_set:
            _dict['updateScriptPath'] = None

        # set to None if proxy_hostname (nullable) is None
        # and model_fields_set contains the field
        if self.proxy_hostname is None and "proxy_hostname" in self.model_fields_set:
            _dict['proxyHostname'] = None

        # set to None if proxy_username (nullable) is None
        # and model_fields_set contains the field
        if self.proxy_username is None and "proxy_username" in self.model_fields_set:
            _dict['proxyUsername'] = None

        # set to None if proxy_password (nullable) is None
        # and model_fields_set contains the field
        if self.proxy_password is None and "proxy_password" in self.model_fields_set:
            _dict['proxyPassword'] = None

        # set to None if proxy_bypass_filter (nullable) is None
        # and model_fields_set contains the field
        if self.proxy_bypass_filter is None and "proxy_bypass_filter" in self.model_fields_set:
            _dict['proxyBypassFilter'] = None

        # set to None if backup_folder (nullable) is None
        # and model_fields_set contains the field
        if self.backup_folder is None and "backup_folder" in self.model_fields_set:
            _dict['backupFolder'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of HostConfigResource from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "bindAddress": obj.get("bindAddress"),
            "port": obj.get("port"),
            "sslPort": obj.get("sslPort"),
            "enableSsl": obj.get("enableSsl"),
            "launchBrowser": obj.get("launchBrowser"),
            "authenticationMethod": obj.get("authenticationMethod"),
            "authenticationRequired": obj.get("authenticationRequired"),
            "analyticsEnabled": obj.get("analyticsEnabled"),
            "username": obj.get("username"),
            "password": obj.get("password"),
            "passwordConfirmation": obj.get("passwordConfirmation"),
            "logLevel": obj.get("logLevel"),
            "consoleLogLevel": obj.get("consoleLogLevel"),
            "branch": obj.get("branch"),
            "apiKey": obj.get("apiKey"),
            "sslCertPath": obj.get("sslCertPath"),
            "sslCertPassword": obj.get("sslCertPassword"),
            "urlBase": obj.get("urlBase"),
            "instanceName": obj.get("instanceName"),
            "applicationUrl": obj.get("applicationUrl"),
            "updateAutomatically": obj.get("updateAutomatically"),
            "updateMechanism": obj.get("updateMechanism"),
            "updateScriptPath": obj.get("updateScriptPath"),
            "proxyEnabled": obj.get("proxyEnabled"),
            "proxyType": obj.get("proxyType"),
            "proxyHostname": obj.get("proxyHostname"),
            "proxyPort": obj.get("proxyPort"),
            "proxyUsername": obj.get("proxyUsername"),
            "proxyPassword": obj.get("proxyPassword"),
            "proxyBypassFilter": obj.get("proxyBypassFilter"),
            "proxyBypassLocalAddresses": obj.get("proxyBypassLocalAddresses"),
            "certificateValidation": obj.get("certificateValidation"),
            "backupFolder": obj.get("backupFolder"),
            "backupInterval": obj.get("backupInterval"),
            "backupRetention": obj.get("backupRetention")
        })
        return _obj


