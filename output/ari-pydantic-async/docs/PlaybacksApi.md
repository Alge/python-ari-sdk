# ari_async_sdk.PlaybacksApi

All URIs are relative to *http://localhost:8088/ari*

Method | HTTP request | Description
------------- | ------------- | -------------
[**control**](PlaybacksApi.md#control) | **POST** /playbacks/{playbackId}/control | Control a playback.
[**getplayback**](PlaybacksApi.md#getplayback) | **GET** /playbacks/{playbackId} | Get a playback&#39;s details.
[**stop**](PlaybacksApi.md#stop) | **DELETE** /playbacks/{playbackId} | Stop a playback.


# **control**
> control(playback_id, operation)

Control a playback.

### Example

```python
import time
import os
import ari_async_sdk
from ari_async_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:8088/ari
# See configuration.py for a list of all supported configuration parameters.
configuration = ari_async_sdk.Configuration(
    host = "http://localhost:8088/ari"
)


# Enter a context with an instance of the API client
async with ari_async_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ari_async_sdk.PlaybacksApi(api_client)
    playback_id = 'playback_id_example' # str | Playback's id
    operation = 'operation_example' # str | Operation to perform on the playback.

    try:
        # Control a playback.
        await api_instance.control(playback_id, operation)
    except Exception as e:
        print("Exception when calling PlaybacksApi->control: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **playback_id** | **str**| Playback&#39;s id | 
 **operation** | **str**| Operation to perform on the playback. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | No response was specified |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **getplayback**
> Playback getplayback(playback_id)

Get a playback's details.

### Example

```python
import time
import os
import ari_async_sdk
from ari_async_sdk.models.playback import Playback
from ari_async_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:8088/ari
# See configuration.py for a list of all supported configuration parameters.
configuration = ari_async_sdk.Configuration(
    host = "http://localhost:8088/ari"
)


# Enter a context with an instance of the API client
async with ari_async_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ari_async_sdk.PlaybacksApi(api_client)
    playback_id = 'playback_id_example' # str | Playback's id

    try:
        # Get a playback's details.
        api_response = await api_instance.getplayback(playback_id)
        print("The response of PlaybacksApi->getplayback:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PlaybacksApi->getplayback: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **playback_id** | **str**| Playback&#39;s id | 

### Return type

[**Playback**](Playback.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | No response was specified |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **stop**
> stop(playback_id)

Stop a playback.

### Example

```python
import time
import os
import ari_async_sdk
from ari_async_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:8088/ari
# See configuration.py for a list of all supported configuration parameters.
configuration = ari_async_sdk.Configuration(
    host = "http://localhost:8088/ari"
)


# Enter a context with an instance of the API client
async with ari_async_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ari_async_sdk.PlaybacksApi(api_client)
    playback_id = 'playback_id_example' # str | Playback's id

    try:
        # Stop a playback.
        await api_instance.stop(playback_id)
    except Exception as e:
        print("Exception when calling PlaybacksApi->stop: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **playback_id** | **str**| Playback&#39;s id | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | No response was specified |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

