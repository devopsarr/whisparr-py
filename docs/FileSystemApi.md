# whisparr.FileSystemApi

All URIs are relative to *http://localhost:7878*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_file_system**](FileSystemApi.md#get_file_system) | **GET** /api/v3/filesystem | 
[**get_file_system_mediafiles**](FileSystemApi.md#get_file_system_mediafiles) | **GET** /api/v3/filesystem/mediafiles | 
[**get_file_system_type**](FileSystemApi.md#get_file_system_type) | **GET** /api/v3/filesystem/type | 


# **get_file_system**
> get_file_system(path=path, include_files=include_files, allow_folders_without_trailing_slashes=allow_folders_without_trailing_slashes)

### Example

* Api Key Authentication (apikey):
* Api Key Authentication (X-Api-Key):

```python
import whisparr
from whisparr.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:7878
# See configuration.py for a list of all supported configuration parameters.
configuration = whisparr.Configuration(
    host = "http://localhost:7878"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apikey
configuration.api_key['apikey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apikey'] = 'Bearer'

# Configure API key authorization: X-Api-Key
configuration.api_key['X-Api-Key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Api-Key'] = 'Bearer'

# Enter a context with an instance of the API client
with whisparr.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = whisparr.FileSystemApi(api_client)
    path = 'path_example' # str |  (optional)
    include_files = False # bool |  (optional) (default to False)
    allow_folders_without_trailing_slashes = False # bool |  (optional) (default to False)

    try:
        api_instance.get_file_system(path=path, include_files=include_files, allow_folders_without_trailing_slashes=allow_folders_without_trailing_slashes)
    except Exception as e:
        print("Exception when calling FileSystemApi->get_file_system: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **path** | **str**|  | [optional] 
 **include_files** | **bool**|  | [optional] [default to False]
 **allow_folders_without_trailing_slashes** | **bool**|  | [optional] [default to False]

### Return type

void (empty response body)

### Authorization

[apikey](../README.md#apikey), [X-Api-Key](../README.md#X-Api-Key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**2XX** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_file_system_mediafiles**
> get_file_system_mediafiles(path=path)

### Example

* Api Key Authentication (apikey):
* Api Key Authentication (X-Api-Key):

```python
import whisparr
from whisparr.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:7878
# See configuration.py for a list of all supported configuration parameters.
configuration = whisparr.Configuration(
    host = "http://localhost:7878"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apikey
configuration.api_key['apikey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apikey'] = 'Bearer'

# Configure API key authorization: X-Api-Key
configuration.api_key['X-Api-Key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Api-Key'] = 'Bearer'

# Enter a context with an instance of the API client
with whisparr.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = whisparr.FileSystemApi(api_client)
    path = 'path_example' # str |  (optional)

    try:
        api_instance.get_file_system_mediafiles(path=path)
    except Exception as e:
        print("Exception when calling FileSystemApi->get_file_system_mediafiles: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **path** | **str**|  | [optional] 

### Return type

void (empty response body)

### Authorization

[apikey](../README.md#apikey), [X-Api-Key](../README.md#X-Api-Key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**2XX** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_file_system_type**
> get_file_system_type(path=path)

### Example

* Api Key Authentication (apikey):
* Api Key Authentication (X-Api-Key):

```python
import whisparr
from whisparr.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:7878
# See configuration.py for a list of all supported configuration parameters.
configuration = whisparr.Configuration(
    host = "http://localhost:7878"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apikey
configuration.api_key['apikey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apikey'] = 'Bearer'

# Configure API key authorization: X-Api-Key
configuration.api_key['X-Api-Key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Api-Key'] = 'Bearer'

# Enter a context with an instance of the API client
with whisparr.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = whisparr.FileSystemApi(api_client)
    path = 'path_example' # str |  (optional)

    try:
        api_instance.get_file_system_type(path=path)
    except Exception as e:
        print("Exception when calling FileSystemApi->get_file_system_type: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **path** | **str**|  | [optional] 

### Return type

void (empty response body)

### Authorization

[apikey](../README.md#apikey), [X-Api-Key](../README.md#X-Api-Key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**2XX** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

