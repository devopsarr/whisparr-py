# whisparr.TaskApi

All URIs are relative to *http://localhost:7878*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_system_task_by_id**](TaskApi.md#get_system_task_by_id) | **GET** /api/v3/system/task/{id} | 
[**list_system_task**](TaskApi.md#list_system_task) | **GET** /api/v3/system/task | 


# **get_system_task_by_id**
> TaskResource get_system_task_by_id(id)

### Example

* Api Key Authentication (apikey):
* Api Key Authentication (X-Api-Key):

```python
import whisparr
from whisparr.models.task_resource import TaskResource
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
    api_instance = whisparr.TaskApi(api_client)
    id = 56 # int | 

    try:
        api_response = api_instance.get_system_task_by_id(id)
        print("The response of TaskApi->get_system_task_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TaskApi->get_system_task_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**TaskResource**](TaskResource.md)

### Authorization

[apikey](../README.md#apikey), [X-Api-Key](../README.md#X-Api-Key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**2XX** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_system_task**
> List[TaskResource] list_system_task()

### Example

* Api Key Authentication (apikey):
* Api Key Authentication (X-Api-Key):

```python
import whisparr
from whisparr.models.task_resource import TaskResource
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
    api_instance = whisparr.TaskApi(api_client)

    try:
        api_response = api_instance.list_system_task()
        print("The response of TaskApi->list_system_task:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TaskApi->list_system_task: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[TaskResource]**](TaskResource.md)

### Authorization

[apikey](../README.md#apikey), [X-Api-Key](../README.md#X-Api-Key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**2XX** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

