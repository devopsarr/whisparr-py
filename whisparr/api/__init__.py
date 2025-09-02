# flake8: noqa

if __import__("typing").TYPE_CHECKING:
    # import apis into api package
    from whisparr.api.alternative_title_api import AlternativeTitleApi
    from whisparr.api.api_info_api import ApiInfoApi
    from whisparr.api.authentication_api import AuthenticationApi
    from whisparr.api.auto_tagging_api import AutoTaggingApi
    from whisparr.api.backup_api import BackupApi
    from whisparr.api.blocklist_api import BlocklistApi
    from whisparr.api.calendar_api import CalendarApi
    from whisparr.api.calendar_feed_api import CalendarFeedApi
    from whisparr.api.collection_api import CollectionApi
    from whisparr.api.command_api import CommandApi
    from whisparr.api.credit_api import CreditApi
    from whisparr.api.custom_filter_api import CustomFilterApi
    from whisparr.api.custom_format_api import CustomFormatApi
    from whisparr.api.delay_profile_api import DelayProfileApi
    from whisparr.api.disk_space_api import DiskSpaceApi
    from whisparr.api.download_client_api import DownloadClientApi
    from whisparr.api.download_client_config_api import DownloadClientConfigApi
    from whisparr.api.extra_file_api import ExtraFileApi
    from whisparr.api.file_system_api import FileSystemApi
    from whisparr.api.health_api import HealthApi
    from whisparr.api.history_api import HistoryApi
    from whisparr.api.host_config_api import HostConfigApi
    from whisparr.api.import_exclusions_api import ImportExclusionsApi
    from whisparr.api.import_list_api import ImportListApi
    from whisparr.api.import_list_config_api import ImportListConfigApi
    from whisparr.api.import_list_movies_api import ImportListMoviesApi
    from whisparr.api.indexer_api import IndexerApi
    from whisparr.api.indexer_config_api import IndexerConfigApi
    from whisparr.api.indexer_flag_api import IndexerFlagApi
    from whisparr.api.language_api import LanguageApi
    from whisparr.api.localization_api import LocalizationApi
    from whisparr.api.log_api import LogApi
    from whisparr.api.log_file_api import LogFileApi
    from whisparr.api.manual_import_api import ManualImportApi
    from whisparr.api.media_cover_api import MediaCoverApi
    from whisparr.api.media_management_config_api import MediaManagementConfigApi
    from whisparr.api.metadata_api import MetadataApi
    from whisparr.api.metadata_config_api import MetadataConfigApi
    from whisparr.api.movie_api import MovieApi
    from whisparr.api.movie_editor_api import MovieEditorApi
    from whisparr.api.movie_file_api import MovieFileApi
    from whisparr.api.movie_import_api import MovieImportApi
    from whisparr.api.movie_lookup_api import MovieLookupApi
    from whisparr.api.naming_config_api import NamingConfigApi
    from whisparr.api.notification_api import NotificationApi
    from whisparr.api.parse_api import ParseApi
    from whisparr.api.ping_api import PingApi
    from whisparr.api.quality_definition_api import QualityDefinitionApi
    from whisparr.api.quality_profile_api import QualityProfileApi
    from whisparr.api.quality_profile_schema_api import QualityProfileSchemaApi
    from whisparr.api.queue_api import QueueApi
    from whisparr.api.queue_action_api import QueueActionApi
    from whisparr.api.queue_details_api import QueueDetailsApi
    from whisparr.api.queue_status_api import QueueStatusApi
    from whisparr.api.release_api import ReleaseApi
    from whisparr.api.release_profile_api import ReleaseProfileApi
    from whisparr.api.release_push_api import ReleasePushApi
    from whisparr.api.remote_path_mapping_api import RemotePathMappingApi
    from whisparr.api.rename_movie_api import RenameMovieApi
    from whisparr.api.root_folder_api import RootFolderApi
    from whisparr.api.static_resource_api import StaticResourceApi
    from whisparr.api.system_api import SystemApi
    from whisparr.api.tag_api import TagApi
    from whisparr.api.tag_details_api import TagDetailsApi
    from whisparr.api.task_api import TaskApi
    from whisparr.api.ui_config_api import UiConfigApi
    from whisparr.api.update_api import UpdateApi
    from whisparr.api.update_log_file_api import UpdateLogFileApi
    
else:
    from lazy_imports import LazyModule, as_package, load

    load(
        LazyModule(
            *as_package(__file__),
            """# import apis into api package
from whisparr.api.alternative_title_api import AlternativeTitleApi
from whisparr.api.api_info_api import ApiInfoApi
from whisparr.api.authentication_api import AuthenticationApi
from whisparr.api.auto_tagging_api import AutoTaggingApi
from whisparr.api.backup_api import BackupApi
from whisparr.api.blocklist_api import BlocklistApi
from whisparr.api.calendar_api import CalendarApi
from whisparr.api.calendar_feed_api import CalendarFeedApi
from whisparr.api.collection_api import CollectionApi
from whisparr.api.command_api import CommandApi
from whisparr.api.credit_api import CreditApi
from whisparr.api.custom_filter_api import CustomFilterApi
from whisparr.api.custom_format_api import CustomFormatApi
from whisparr.api.delay_profile_api import DelayProfileApi
from whisparr.api.disk_space_api import DiskSpaceApi
from whisparr.api.download_client_api import DownloadClientApi
from whisparr.api.download_client_config_api import DownloadClientConfigApi
from whisparr.api.extra_file_api import ExtraFileApi
from whisparr.api.file_system_api import FileSystemApi
from whisparr.api.health_api import HealthApi
from whisparr.api.history_api import HistoryApi
from whisparr.api.host_config_api import HostConfigApi
from whisparr.api.import_exclusions_api import ImportExclusionsApi
from whisparr.api.import_list_api import ImportListApi
from whisparr.api.import_list_config_api import ImportListConfigApi
from whisparr.api.import_list_movies_api import ImportListMoviesApi
from whisparr.api.indexer_api import IndexerApi
from whisparr.api.indexer_config_api import IndexerConfigApi
from whisparr.api.indexer_flag_api import IndexerFlagApi
from whisparr.api.language_api import LanguageApi
from whisparr.api.localization_api import LocalizationApi
from whisparr.api.log_api import LogApi
from whisparr.api.log_file_api import LogFileApi
from whisparr.api.manual_import_api import ManualImportApi
from whisparr.api.media_cover_api import MediaCoverApi
from whisparr.api.media_management_config_api import MediaManagementConfigApi
from whisparr.api.metadata_api import MetadataApi
from whisparr.api.metadata_config_api import MetadataConfigApi
from whisparr.api.movie_api import MovieApi
from whisparr.api.movie_editor_api import MovieEditorApi
from whisparr.api.movie_file_api import MovieFileApi
from whisparr.api.movie_import_api import MovieImportApi
from whisparr.api.movie_lookup_api import MovieLookupApi
from whisparr.api.naming_config_api import NamingConfigApi
from whisparr.api.notification_api import NotificationApi
from whisparr.api.parse_api import ParseApi
from whisparr.api.ping_api import PingApi
from whisparr.api.quality_definition_api import QualityDefinitionApi
from whisparr.api.quality_profile_api import QualityProfileApi
from whisparr.api.quality_profile_schema_api import QualityProfileSchemaApi
from whisparr.api.queue_api import QueueApi
from whisparr.api.queue_action_api import QueueActionApi
from whisparr.api.queue_details_api import QueueDetailsApi
from whisparr.api.queue_status_api import QueueStatusApi
from whisparr.api.release_api import ReleaseApi
from whisparr.api.release_profile_api import ReleaseProfileApi
from whisparr.api.release_push_api import ReleasePushApi
from whisparr.api.remote_path_mapping_api import RemotePathMappingApi
from whisparr.api.rename_movie_api import RenameMovieApi
from whisparr.api.root_folder_api import RootFolderApi
from whisparr.api.static_resource_api import StaticResourceApi
from whisparr.api.system_api import SystemApi
from whisparr.api.tag_api import TagApi
from whisparr.api.tag_details_api import TagDetailsApi
from whisparr.api.task_api import TaskApi
from whisparr.api.ui_config_api import UiConfigApi
from whisparr.api.update_api import UpdateApi
from whisparr.api.update_log_file_api import UpdateLogFileApi

""",
            name=__name__,
            doc=__doc__,
        )
    )
