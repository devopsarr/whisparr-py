# coding: utf-8

# flake8: noqa
"""
    Radarr

    Radarr API docs

    The version of the OpenAPI document: b08981dee068e1ed23e4f45a0d8fe70ef7bf7703
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


# import models into model package
from whisparr.models.add_movie_method import AddMovieMethod
from whisparr.models.add_movie_options import AddMovieOptions
from whisparr.models.alternative_title_resource import AlternativeTitleResource
from whisparr.models.api_info_resource import ApiInfoResource
from whisparr.models.apply_tags import ApplyTags
from whisparr.models.authentication_required_type import AuthenticationRequiredType
from whisparr.models.authentication_type import AuthenticationType
from whisparr.models.auto_tagging_resource import AutoTaggingResource
from whisparr.models.auto_tagging_specification_schema import AutoTaggingSpecificationSchema
from whisparr.models.backup_resource import BackupResource
from whisparr.models.backup_type import BackupType
from whisparr.models.blocklist_bulk_resource import BlocklistBulkResource
from whisparr.models.blocklist_resource import BlocklistResource
from whisparr.models.blocklist_resource_paging_resource import BlocklistResourcePagingResource
from whisparr.models.certificate_validation_type import CertificateValidationType
from whisparr.models.collection_movie_resource import CollectionMovieResource
from whisparr.models.collection_resource import CollectionResource
from whisparr.models.collection_update_resource import CollectionUpdateResource
from whisparr.models.colon_replacement_format import ColonReplacementFormat
from whisparr.models.command import Command
from whisparr.models.command_priority import CommandPriority
from whisparr.models.command_resource import CommandResource
from whisparr.models.command_result import CommandResult
from whisparr.models.command_status import CommandStatus
from whisparr.models.command_trigger import CommandTrigger
from whisparr.models.credit_resource import CreditResource
from whisparr.models.credit_type import CreditType
from whisparr.models.custom_filter_resource import CustomFilterResource
from whisparr.models.custom_format_resource import CustomFormatResource
from whisparr.models.custom_format_specification_schema import CustomFormatSpecificationSchema
from whisparr.models.database_type import DatabaseType
from whisparr.models.delay_profile_resource import DelayProfileResource
from whisparr.models.disk_space_resource import DiskSpaceResource
from whisparr.models.download_client_bulk_resource import DownloadClientBulkResource
from whisparr.models.download_client_config_resource import DownloadClientConfigResource
from whisparr.models.download_client_resource import DownloadClientResource
from whisparr.models.download_protocol import DownloadProtocol
from whisparr.models.extra_file_resource import ExtraFileResource
from whisparr.models.extra_file_type import ExtraFileType
from whisparr.models.field import Field
from whisparr.models.file_date_type import FileDateType
from whisparr.models.health_check_result import HealthCheckResult
from whisparr.models.health_resource import HealthResource
from whisparr.models.history_resource import HistoryResource
from whisparr.models.history_resource_paging_resource import HistoryResourcePagingResource
from whisparr.models.host_config_resource import HostConfigResource
from whisparr.models.import_exclusions_resource import ImportExclusionsResource
from whisparr.models.import_list_bulk_resource import ImportListBulkResource
from whisparr.models.import_list_config_resource import ImportListConfigResource
from whisparr.models.import_list_resource import ImportListResource
from whisparr.models.import_list_type import ImportListType
from whisparr.models.indexer_bulk_resource import IndexerBulkResource
from whisparr.models.indexer_config_resource import IndexerConfigResource
from whisparr.models.indexer_flag_resource import IndexerFlagResource
from whisparr.models.indexer_resource import IndexerResource
from whisparr.models.language import Language
from whisparr.models.language_resource import LanguageResource
from whisparr.models.localization_language_resource import LocalizationLanguageResource
from whisparr.models.log_file_resource import LogFileResource
from whisparr.models.log_resource import LogResource
from whisparr.models.log_resource_paging_resource import LogResourcePagingResource
from whisparr.models.manual_import_reprocess_resource import ManualImportReprocessResource
from whisparr.models.manual_import_resource import ManualImportResource
from whisparr.models.media_cover import MediaCover
from whisparr.models.media_cover_types import MediaCoverTypes
from whisparr.models.media_info_resource import MediaInfoResource
from whisparr.models.media_management_config_resource import MediaManagementConfigResource
from whisparr.models.metadata_config_resource import MetadataConfigResource
from whisparr.models.metadata_resource import MetadataResource
from whisparr.models.modifier import Modifier
from whisparr.models.monitor_types import MonitorTypes
from whisparr.models.movie_collection_resource import MovieCollectionResource
from whisparr.models.movie_editor_resource import MovieEditorResource
from whisparr.models.movie_file_list_resource import MovieFileListResource
from whisparr.models.movie_file_resource import MovieFileResource
from whisparr.models.movie_history_event_type import MovieHistoryEventType
from whisparr.models.movie_resource import MovieResource
from whisparr.models.movie_runtime_format_type import MovieRuntimeFormatType
from whisparr.models.movie_statistics_resource import MovieStatisticsResource
from whisparr.models.movie_status_type import MovieStatusType
from whisparr.models.naming_config_resource import NamingConfigResource
from whisparr.models.notification_resource import NotificationResource
from whisparr.models.parse_resource import ParseResource
from whisparr.models.parsed_movie_info import ParsedMovieInfo
from whisparr.models.ping_resource import PingResource
from whisparr.models.privacy_level import PrivacyLevel
from whisparr.models.profile_format_item_resource import ProfileFormatItemResource
from whisparr.models.proper_download_types import ProperDownloadTypes
from whisparr.models.provider_message import ProviderMessage
from whisparr.models.provider_message_type import ProviderMessageType
from whisparr.models.proxy_type import ProxyType
from whisparr.models.quality import Quality
from whisparr.models.quality_definition_resource import QualityDefinitionResource
from whisparr.models.quality_model import QualityModel
from whisparr.models.quality_profile_quality_item_resource import QualityProfileQualityItemResource
from whisparr.models.quality_profile_resource import QualityProfileResource
from whisparr.models.quality_source import QualitySource
from whisparr.models.queue_bulk_resource import QueueBulkResource
from whisparr.models.queue_resource import QueueResource
from whisparr.models.queue_resource_paging_resource import QueueResourcePagingResource
from whisparr.models.queue_status_resource import QueueStatusResource
from whisparr.models.rating_child import RatingChild
from whisparr.models.rating_type import RatingType
from whisparr.models.ratings import Ratings
from whisparr.models.rejection import Rejection
from whisparr.models.rejection_type import RejectionType
from whisparr.models.release_profile_resource import ReleaseProfileResource
from whisparr.models.release_resource import ReleaseResource
from whisparr.models.remote_path_mapping_resource import RemotePathMappingResource
from whisparr.models.rename_movie_resource import RenameMovieResource
from whisparr.models.rescan_after_refresh_type import RescanAfterRefreshType
from whisparr.models.revision import Revision
from whisparr.models.root_folder_resource import RootFolderResource
from whisparr.models.runtime_mode import RuntimeMode
from whisparr.models.select_option import SelectOption
from whisparr.models.sort_direction import SortDirection
from whisparr.models.source_type import SourceType
from whisparr.models.system_resource import SystemResource
from whisparr.models.tmdb_country_code import TMDbCountryCode
from whisparr.models.tag_details_resource import TagDetailsResource
from whisparr.models.tag_resource import TagResource
from whisparr.models.task_resource import TaskResource
from whisparr.models.tracked_download_state import TrackedDownloadState
from whisparr.models.tracked_download_status import TrackedDownloadStatus
from whisparr.models.tracked_download_status_message import TrackedDownloadStatusMessage
from whisparr.models.ui_config_resource import UiConfigResource
from whisparr.models.unmapped_folder import UnmappedFolder
from whisparr.models.update_changes import UpdateChanges
from whisparr.models.update_mechanism import UpdateMechanism
from whisparr.models.update_resource import UpdateResource
