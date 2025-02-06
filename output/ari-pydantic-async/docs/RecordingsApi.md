# ari_sync_sdk.RecordingsApi

All URIs are relative to *http://localhost:8088/ari*

Method | HTTP request | Description
------------- | ------------- | -------------
[**cancel**](RecordingsApi.md#cancel) | **DELETE** /recordings/live/{recordingName} | Stop a live recording and discard it.
[**copy_stored**](RecordingsApi.md#copy_stored) | **POST** /recordings/stored/{recordingName}/copy | Copy a stored recording.
[**delete_stored**](RecordingsApi.md#delete_stored) | **DELETE** /recordings/stored/{recordingName} | Delete a stored recording.
[**get_live**](RecordingsApi.md#get_live) | **GET** /recordings/live/{recordingName} | List live recordings.
[**get_stored**](RecordingsApi.md#get_stored) | **GET** /recordings/stored/{recordingName} | Get a stored recording&#39;s details.
[**get_stored_file**](RecordingsApi.md#get_stored_file) | **GET** /recordings/stored/{recordingName}/file | Get the file associated with the stored recording.
[**list_stored**](RecordingsApi.md#list_stored) | **GET** /recordings/stored | List recordings that are complete.
[**muterecording**](RecordingsApi.md#muterecording) | **POST** /recordings/live/{recordingName}/mute | Mute a live recording.
[**pause**](RecordingsApi.md#pause) | **POST** /recordings/live/{recordingName}/pause | Pause a live recording.
[**stoprecording**](RecordingsApi.md#stoprecording) | **POST** /recordings/live/{recordingName}/stop | Stop a live recording and store it.
[**unmuterecording**](RecordingsApi.md#unmuterecording) | **DELETE** /recordings/live/{recordingName}/mute | Unmute a live recording.
[**unpause**](RecordingsApi.md#unpause) | **DELETE** /recordings/live/{recordingName}/pause | Unpause a live recording.


# **cancel**
> cancel(recording_name)

Stop a live recording and discard it.

### Example

```python
import time
import os
import ari_sync_sdk
from ari_sync_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:8088/ari
# See configuration.py for a list of all supported configuration parameters.
configuration = ari_sync_sdk.Configuration(
    host = "http://localhost:8088/ari"
)


# Enter a context with an instance of the API client
async with ari_sync_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ari_sync_sdk.RecordingsApi(api_client)
    recording_name = 'recording_name_example' # str | The name of the recording

    try:
        # Stop a live recording and discard it.
        await api_instance.cancel(recording_name)
    except Exception as e:
        print("Exception when calling RecordingsApi->cancel: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **recording_name** | **str**| The name of the recording | 

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

# **copy_stored**
> StoredRecording copy_stored(recording_name, destination_recording_name)

Copy a stored recording.

### Example

```python
import time
import os
import ari_sync_sdk
from ari_sync_sdk.models.stored_recording import StoredRecording
from ari_sync_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:8088/ari
# See configuration.py for a list of all supported configuration parameters.
configuration = ari_sync_sdk.Configuration(
    host = "http://localhost:8088/ari"
)


# Enter a context with an instance of the API client
async with ari_sync_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ari_sync_sdk.RecordingsApi(api_client)
    recording_name = 'recording_name_example' # str | The name of the recording to copy
    destination_recording_name = 'destination_recording_name_example' # str | The destination name of the recording

    try:
        # Copy a stored recording.
        api_response = await api_instance.copy_stored(recording_name, destination_recording_name)
        print("The response of RecordingsApi->copy_stored:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RecordingsApi->copy_stored: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **recording_name** | **str**| The name of the recording to copy | 
 **destination_recording_name** | **str**| The destination name of the recording | 

### Return type

[**StoredRecording**](StoredRecording.md)

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

# **delete_stored**
> delete_stored(recording_name)

Delete a stored recording.

### Example

```python
import time
import os
import ari_sync_sdk
from ari_sync_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:8088/ari
# See configuration.py for a list of all supported configuration parameters.
configuration = ari_sync_sdk.Configuration(
    host = "http://localhost:8088/ari"
)


# Enter a context with an instance of the API client
async with ari_sync_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ari_sync_sdk.RecordingsApi(api_client)
    recording_name = 'recording_name_example' # str | The name of the recording

    try:
        # Delete a stored recording.
        await api_instance.delete_stored(recording_name)
    except Exception as e:
        print("Exception when calling RecordingsApi->delete_stored: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **recording_name** | **str**| The name of the recording | 

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

# **get_live**
> LiveRecording get_live(recording_name)

List live recordings.

### Example

```python
import time
import os
import ari_sync_sdk
from ari_sync_sdk.models.live_recording import LiveRecording
from ari_sync_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:8088/ari
# See configuration.py for a list of all supported configuration parameters.
configuration = ari_sync_sdk.Configuration(
    host = "http://localhost:8088/ari"
)


# Enter a context with an instance of the API client
async with ari_sync_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ari_sync_sdk.RecordingsApi(api_client)
    recording_name = 'recording_name_example' # str | The name of the recording

    try:
        # List live recordings.
        api_response = await api_instance.get_live(recording_name)
        print("The response of RecordingsApi->get_live:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RecordingsApi->get_live: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **recording_name** | **str**| The name of the recording | 

### Return type

[**LiveRecording**](LiveRecording.md)

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

# **get_stored**
> StoredRecording get_stored(recording_name)

Get a stored recording's details.

### Example

```python
import time
import os
import ari_sync_sdk
from ari_sync_sdk.models.stored_recording import StoredRecording
from ari_sync_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:8088/ari
# See configuration.py for a list of all supported configuration parameters.
configuration = ari_sync_sdk.Configuration(
    host = "http://localhost:8088/ari"
)


# Enter a context with an instance of the API client
async with ari_sync_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ari_sync_sdk.RecordingsApi(api_client)
    recording_name = 'recording_name_example' # str | The name of the recording

    try:
        # Get a stored recording's details.
        api_response = await api_instance.get_stored(recording_name)
        print("The response of RecordingsApi->get_stored:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RecordingsApi->get_stored: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **recording_name** | **str**| The name of the recording | 

### Return type

[**StoredRecording**](StoredRecording.md)

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

# **get_stored_file**
> object get_stored_file(recording_name)

Get the file associated with the stored recording.

### Example

```python
import time
import os
import ari_sync_sdk
from ari_sync_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:8088/ari
# See configuration.py for a list of all supported configuration parameters.
configuration = ari_sync_sdk.Configuration(
    host = "http://localhost:8088/ari"
)


# Enter a context with an instance of the API client
async with ari_sync_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ari_sync_sdk.RecordingsApi(api_client)
    recording_name = 'recording_name_example' # str | The name of the recording

    try:
        # Get the file associated with the stored recording.
        api_response = await api_instance.get_stored_file(recording_name)
        print("The response of RecordingsApi->get_stored_file:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RecordingsApi->get_stored_file: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **recording_name** | **str**| The name of the recording | 

### Return type

**object**

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

# **list_stored**
> List[StoredRecording] list_stored()

List recordings that are complete.

### Example

```python
import time
import os
import ari_sync_sdk
from ari_sync_sdk.models.stored_recording import StoredRecording
from ari_sync_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:8088/ari
# See configuration.py for a list of all supported configuration parameters.
configuration = ari_sync_sdk.Configuration(
    host = "http://localhost:8088/ari"
)


# Enter a context with an instance of the API client
async with ari_sync_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ari_sync_sdk.RecordingsApi(api_client)

    try:
        # List recordings that are complete.
        api_response = await api_instance.list_stored()
        print("The response of RecordingsApi->list_stored:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RecordingsApi->list_stored: %s\n" % e)
```



### Parameters
This endpoint does not need any parameter.

### Return type

[**List[StoredRecording]**](StoredRecording.md)

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

# **muterecording**
> muterecording(recording_name)

Mute a live recording.

Muting a recording suspends silence detection, which will be restarted when the recording is unmuted.

### Example

```python
import time
import os
import ari_sync_sdk
from ari_sync_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:8088/ari
# See configuration.py for a list of all supported configuration parameters.
configuration = ari_sync_sdk.Configuration(
    host = "http://localhost:8088/ari"
)


# Enter a context with an instance of the API client
async with ari_sync_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ari_sync_sdk.RecordingsApi(api_client)
    recording_name = 'recording_name_example' # str | The name of the recording

    try:
        # Mute a live recording.
        await api_instance.muterecording(recording_name)
    except Exception as e:
        print("Exception when calling RecordingsApi->muterecording: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **recording_name** | **str**| The name of the recording | 

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

# **pause**
> pause(recording_name)

Pause a live recording.

Pausing a recording suspends silence detection, which will be restarted when the recording is unpaused. Paused time is not included in the accounting for maxDurationSeconds.

### Example

```python
import time
import os
import ari_sync_sdk
from ari_sync_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:8088/ari
# See configuration.py for a list of all supported configuration parameters.
configuration = ari_sync_sdk.Configuration(
    host = "http://localhost:8088/ari"
)


# Enter a context with an instance of the API client
async with ari_sync_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ari_sync_sdk.RecordingsApi(api_client)
    recording_name = 'recording_name_example' # str | The name of the recording

    try:
        # Pause a live recording.
        await api_instance.pause(recording_name)
    except Exception as e:
        print("Exception when calling RecordingsApi->pause: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **recording_name** | **str**| The name of the recording | 

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

# **stoprecording**
> stoprecording(recording_name)

Stop a live recording and store it.

### Example

```python
import time
import os
import ari_sync_sdk
from ari_sync_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:8088/ari
# See configuration.py for a list of all supported configuration parameters.
configuration = ari_sync_sdk.Configuration(
    host = "http://localhost:8088/ari"
)


# Enter a context with an instance of the API client
async with ari_sync_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ari_sync_sdk.RecordingsApi(api_client)
    recording_name = 'recording_name_example' # str | The name of the recording

    try:
        # Stop a live recording and store it.
        await api_instance.stoprecording(recording_name)
    except Exception as e:
        print("Exception when calling RecordingsApi->stoprecording: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **recording_name** | **str**| The name of the recording | 

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

# **unmuterecording**
> unmuterecording(recording_name)

Unmute a live recording.

### Example

```python
import time
import os
import ari_sync_sdk
from ari_sync_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:8088/ari
# See configuration.py for a list of all supported configuration parameters.
configuration = ari_sync_sdk.Configuration(
    host = "http://localhost:8088/ari"
)


# Enter a context with an instance of the API client
async with ari_sync_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ari_sync_sdk.RecordingsApi(api_client)
    recording_name = 'recording_name_example' # str | The name of the recording

    try:
        # Unmute a live recording.
        await api_instance.unmuterecording(recording_name)
    except Exception as e:
        print("Exception when calling RecordingsApi->unmuterecording: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **recording_name** | **str**| The name of the recording | 

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

# **unpause**
> unpause(recording_name)

Unpause a live recording.

### Example

```python
import time
import os
import ari_sync_sdk
from ari_sync_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:8088/ari
# See configuration.py for a list of all supported configuration parameters.
configuration = ari_sync_sdk.Configuration(
    host = "http://localhost:8088/ari"
)


# Enter a context with an instance of the API client
async with ari_sync_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ari_sync_sdk.RecordingsApi(api_client)
    recording_name = 'recording_name_example' # str | The name of the recording

    try:
        # Unpause a live recording.
        await api_instance.unpause(recording_name)
    except Exception as e:
        print("Exception when calling RecordingsApi->unpause: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **recording_name** | **str**| The name of the recording | 

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

