# coding: utf-8

# flake8: noqa

"""
    Whisparr

    Whisparr API docs  # noqa: E501

    The version of the OpenAPI document: 3.0.0
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

# import models into model package
from whisparr.models.add_series_options import AddSeriesOptions
from whisparr.models.alternate_title_resource import AlternateTitleResource
from whisparr.models.apply_tags import ApplyTags
from whisparr.models.authentication_required_type import AuthenticationRequiredType
from whisparr.models.authentication_type import AuthenticationType
from whisparr.models.backup_resource import BackupResource
from whisparr.models.backup_type import BackupType
from whisparr.models.blocklist_bulk_resource import BlocklistBulkResource
from whisparr.models.blocklist_resource import BlocklistResource
from whisparr.models.blocklist_resource_paging_resource import BlocklistResourcePagingResource
from whisparr.models.certificate_validation_type import CertificateValidationType
from whisparr.models.command import Command
from whisparr.models.command_priority import CommandPriority
from whisparr.models.command_resource import CommandResource
from whisparr.models.command_status import CommandStatus
from whisparr.models.command_trigger import CommandTrigger
from whisparr.models.custom_filter_resource import CustomFilterResource
from whisparr.models.custom_format_resource import CustomFormatResource
from whisparr.models.custom_format_specification_schema import CustomFormatSpecificationSchema
from whisparr.models.delay_profile_resource import DelayProfileResource
from whisparr.models.disk_space_resource import DiskSpaceResource
from whisparr.models.download_client_config_resource import DownloadClientConfigResource
from whisparr.models.download_client_resource import DownloadClientResource
from whisparr.models.download_protocol import DownloadProtocol
from whisparr.models.episode_file_list_resource import EpisodeFileListResource
from whisparr.models.episode_file_resource import EpisodeFileResource
from whisparr.models.episode_history_event_type import EpisodeHistoryEventType
from whisparr.models.episode_resource import EpisodeResource
from whisparr.models.episode_resource_paging_resource import EpisodeResourcePagingResource
from whisparr.models.episode_title_required_type import EpisodeTitleRequiredType
from whisparr.models.episodes_monitored_resource import EpisodesMonitoredResource
from whisparr.models.field import Field
from whisparr.models.file_date_type import FileDateType
from whisparr.models.health_check_result import HealthCheckResult
from whisparr.models.health_resource import HealthResource
from whisparr.models.history_resource import HistoryResource
from whisparr.models.history_resource_paging_resource import HistoryResourcePagingResource
from whisparr.models.host_config_resource import HostConfigResource
from whisparr.models.import_list_exclusion_resource import ImportListExclusionResource
from whisparr.models.import_list_resource import ImportListResource
from whisparr.models.import_list_type import ImportListType
from whisparr.models.indexer_config_resource import IndexerConfigResource
from whisparr.models.indexer_resource import IndexerResource
from whisparr.models.language import Language
from whisparr.models.language_profile_item_resource import LanguageProfileItemResource
from whisparr.models.language_profile_resource import LanguageProfileResource
from whisparr.models.language_resource import LanguageResource
from whisparr.models.localization_resource import LocalizationResource
from whisparr.models.log_file_resource import LogFileResource
from whisparr.models.log_resource import LogResource
from whisparr.models.log_resource_paging_resource import LogResourcePagingResource
from whisparr.models.manual_import_reprocess_resource import ManualImportReprocessResource
from whisparr.models.manual_import_resource import ManualImportResource
from whisparr.models.media_cover import MediaCover
from whisparr.models.media_cover_types import MediaCoverTypes
from whisparr.models.media_info_resource import MediaInfoResource
from whisparr.models.media_management_config_resource import MediaManagementConfigResource
from whisparr.models.metadata_resource import MetadataResource
from whisparr.models.monitor_types import MonitorTypes
from whisparr.models.monitoring_options import MonitoringOptions
from whisparr.models.naming_config_resource import NamingConfigResource
from whisparr.models.notification_resource import NotificationResource
from whisparr.models.paging_resource_filter import PagingResourceFilter
from whisparr.models.parse_resource import ParseResource
from whisparr.models.parsed_episode_info import ParsedEpisodeInfo
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
from whisparr.models.ratings import Ratings
from whisparr.models.rejection import Rejection
from whisparr.models.rejection_type import RejectionType
from whisparr.models.release_profile_resource import ReleaseProfileResource
from whisparr.models.release_resource import ReleaseResource
from whisparr.models.remote_path_mapping_resource import RemotePathMappingResource
from whisparr.models.rename_episode_resource import RenameEpisodeResource
from whisparr.models.rescan_after_refresh_type import RescanAfterRefreshType
from whisparr.models.revision import Revision
from whisparr.models.root_folder_resource import RootFolderResource
from whisparr.models.runtime_mode import RuntimeMode
from whisparr.models.season_pass_resource import SeasonPassResource
from whisparr.models.season_pass_series_resource import SeasonPassSeriesResource
from whisparr.models.season_resource import SeasonResource
from whisparr.models.season_statistics_resource import SeasonStatisticsResource
from whisparr.models.select_option import SelectOption
from whisparr.models.series_editor_resource import SeriesEditorResource
from whisparr.models.series_resource import SeriesResource
from whisparr.models.series_statistics_resource import SeriesStatisticsResource
from whisparr.models.series_status_type import SeriesStatusType
from whisparr.models.series_title_info import SeriesTitleInfo
from whisparr.models.series_types import SeriesTypes
from whisparr.models.sort_direction import SortDirection
from whisparr.models.system_resource import SystemResource
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
