# whisparr.QueueDetailsApi

All URIs are relative to *http://localhost:6969*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_queue_details_by_id**](QueueDetailsApi.md#get_queue_details_by_id) | **GET** /api/v3/queue/details/{id} | 
[**list_queue_details**](QueueDetailsApi.md#list_queue_details) | **GET** /api/v3/queue/details | 


# **get_queue_details_by_id**
> QueueResource get_queue_details_by_id(id)



### Example

* Api Key Authentication (X-Api-Key):
```python
from __future__ import print_function
import time
import os
import whisparr
from whisparr.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:6969
# See configuration.py for a list of all supported configuration parameters.
configuration = whisparr.Configuration(
    host = "http://localhost:6969"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: X-Api-Key
configuration.api_key['X-Api-Key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Api-Key'] = 'Bearer'

# Configure API key authorization: apikey
configuration.api_key['apikey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apikey'] = 'Bearer'

# Enter a context with an instance of the API client
with whisparr.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = whisparr.QueueDetailsApi(api_client)
    id = 56 # int | 

    try:
        api_response = api_instance.get_queue_details_by_id(id)
        print("The response of QueueDetailsApi->get_queue_details_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QueueDetailsApi->get_queue_details_by_id: %s\n" % e)
```

* Api Key Authentication (apikey):
```python
from __future__ import print_function
import time
import os
import whisparr
from whisparr.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:6969
# See configuration.py for a list of all supported configuration parameters.
configuration = whisparr.Configuration(
    host = "http://localhost:6969"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: X-Api-Key
configuration.api_key['X-Api-Key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Api-Key'] = 'Bearer'

# Configure API key authorization: apikey
configuration.api_key['apikey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apikey'] = 'Bearer'

# Enter a context with an instance of the API client
with whisparr.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = whisparr.QueueDetailsApi(api_client)
    id = 56 # int | 

    try:
        api_response = api_instance.get_queue_details_by_id(id)
        print("The response of QueueDetailsApi->get_queue_details_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QueueDetailsApi->get_queue_details_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**QueueResource**](QueueResource.md)

### Authorization

[X-Api-Key](../README.md#X-Api-Key), [apikey](../README.md#apikey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_queue_details**
> List[QueueResource] list_queue_details(movie_id=movie_id, include_movie=include_movie)



### Example

* Api Key Authentication (X-Api-Key):
```python
from __future__ import print_function
import time
import os
import whisparr
from whisparr.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:6969
# See configuration.py for a list of all supported configuration parameters.
configuration = whisparr.Configuration(
    host = "http://localhost:6969"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: X-Api-Key
configuration.api_key['X-Api-Key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Api-Key'] = 'Bearer'

# Configure API key authorization: apikey
configuration.api_key['apikey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apikey'] = 'Bearer'

# Enter a context with an instance of the API client
with whisparr.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = whisparr.QueueDetailsApi(api_client)
    movie_id = 56 # int |  (optional)
    include_movie = False # bool |  (optional) (default to False)

    try:
        api_response = api_instance.list_queue_details(movie_id=movie_id, include_movie=include_movie)
        print("The response of QueueDetailsApi->list_queue_details:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QueueDetailsApi->list_queue_details: %s\n" % e)
```

* Api Key Authentication (apikey):
```python
from __future__ import print_function
import time
import os
import whisparr
from whisparr.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:6969
# See configuration.py for a list of all supported configuration parameters.
configuration = whisparr.Configuration(
    host = "http://localhost:6969"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: X-Api-Key
configuration.api_key['X-Api-Key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Api-Key'] = 'Bearer'

# Configure API key authorization: apikey
configuration.api_key['apikey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apikey'] = 'Bearer'

# Enter a context with an instance of the API client
with whisparr.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = whisparr.QueueDetailsApi(api_client)
    movie_id = 56 # int |  (optional)
    include_movie = False # bool |  (optional) (default to False)

    try:
        api_response = api_instance.list_queue_details(movie_id=movie_id, include_movie=include_movie)
        print("The response of QueueDetailsApi->list_queue_details:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QueueDetailsApi->list_queue_details: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **movie_id** | **int**|  | [optional] 
 **include_movie** | **bool**|  | [optional] [default to False]

### Return type

[**List[QueueResource]**](QueueResource.md)

### Authorization

[X-Api-Key](../README.md#X-Api-Key), [apikey](../README.md#apikey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

