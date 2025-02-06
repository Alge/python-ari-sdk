# ari_sync_sdk.SoundsApi

All URIs are relative to *http://localhost:8088/ari*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getsound**](SoundsApi.md#getsound) | **GET** /sounds/{soundId} | Get a sound&#39;s details.
[**listsounds**](SoundsApi.md#listsounds) | **GET** /sounds | List all sounds.


# **getsound**
> Sound getsound(sound_id)

Get a sound's details.

### Example

```python
import time
import os
import ari_sync_sdk
from ari_sync_sdk.models.sound import Sound
from ari_sync_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:8088/ari
# See configuration.py for a list of all supported configuration parameters.
configuration = ari_sync_sdk.Configuration(
    host = "http://localhost:8088/ari"
)


# Enter a context with an instance of the API client
with ari_sync_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ari_sync_sdk.SoundsApi(api_client)
    sound_id = 'sound_id_example' # str | Sound's id

    try:
        # Get a sound's details.
        api_response = api_instance.getsound(sound_id)
        print("The response of SoundsApi->getsound:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SoundsApi->getsound: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sound_id** | **str**| Sound&#39;s id | 

### Return type

[**Sound**](Sound.md)

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

# **listsounds**
> List[Sound] listsounds(lang=lang, format=format)

List all sounds.

### Example

```python
import time
import os
import ari_sync_sdk
from ari_sync_sdk.models.sound import Sound
from ari_sync_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:8088/ari
# See configuration.py for a list of all supported configuration parameters.
configuration = ari_sync_sdk.Configuration(
    host = "http://localhost:8088/ari"
)


# Enter a context with an instance of the API client
with ari_sync_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ari_sync_sdk.SoundsApi(api_client)
    lang = 'lang_example' # str | Lookup sound for a specific language. (optional)
    format = 'format_example' # str | Lookup sound in a specific format. (optional)

    try:
        # List all sounds.
        api_response = api_instance.listsounds(lang=lang, format=format)
        print("The response of SoundsApi->listsounds:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SoundsApi->listsounds: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **lang** | **str**| Lookup sound for a specific language. | [optional] 
 **format** | **str**| Lookup sound in a specific format. | [optional] 

### Return type

[**List[Sound]**](Sound.md)

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

