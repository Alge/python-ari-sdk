# ari_sync_sdk.BridgesApi

All URIs are relative to *http://localhost:8088/ari*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_channel**](BridgesApi.md#add_channel) | **POST** /bridges/{bridgeId}/addChannel | Add a channel to a bridge.
[**clear_video_source**](BridgesApi.md#clear_video_source) | **DELETE** /bridges/{bridgeId}/videoSource | Removes any explicit video source in a multi-party mixing bridge. This operation has no effect on bridges with two or fewer participants. When no explicit video source is set, talk detection will be used to determine the active video stream.
[**create**](BridgesApi.md#create) | **POST** /bridges | Create a new bridge.
[**create_with_id**](BridgesApi.md#create_with_id) | **POST** /bridges/{bridgeId} | Create a new bridge or updates an existing one.
[**destroy**](BridgesApi.md#destroy) | **DELETE** /bridges/{bridgeId} | Shut down a bridge.
[**getbridge**](BridgesApi.md#getbridge) | **GET** /bridges/{bridgeId} | Get bridge details.
[**listbridges**](BridgesApi.md#listbridges) | **GET** /bridges | List all active bridges in Asterisk.
[**play**](BridgesApi.md#play) | **POST** /bridges/{bridgeId}/play | Start playback of media on a bridge.
[**play_with_id**](BridgesApi.md#play_with_id) | **POST** /bridges/{bridgeId}/play/{playbackId} | Start playback of media on a bridge.
[**record**](BridgesApi.md#record) | **POST** /bridges/{bridgeId}/record | Start a recording.
[**remove_channel**](BridgesApi.md#remove_channel) | **POST** /bridges/{bridgeId}/removeChannel | Remove a channel from a bridge.
[**set_video_source**](BridgesApi.md#set_video_source) | **POST** /bridges/{bridgeId}/videoSource/{channelId} | Set a channel as the video source in a multi-party mixing bridge. This operation has no effect on bridges with two or fewer participants.
[**start_moh**](BridgesApi.md#start_moh) | **POST** /bridges/{bridgeId}/moh | Play music on hold to a bridge or change the MOH class that is playing.
[**stop_moh**](BridgesApi.md#stop_moh) | **DELETE** /bridges/{bridgeId}/moh | Stop playing music on hold to a bridge.


# **add_channel**
> add_channel(bridge_id, channel, role=role, absorb_dtmf=absorb_dtmf, mute=mute, inhibit_connected_line_updates=inhibit_connected_line_updates)

Add a channel to a bridge.

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
with ari_sync_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ari_sync_sdk.BridgesApi(api_client)
    bridge_id = 'bridge_id_example' # str | Bridge's id
    channel = ['channel_example'] # List[str] | Ids of channels to add to bridge
    role = 'role_example' # str | Channel's role in the bridge (optional)
    absorb_dtmf = False # bool | Absorb DTMF coming from this channel, preventing it to pass through to the bridge (optional) (default to False)
    mute = False # bool | Mute audio from this channel, preventing it to pass through to the bridge (optional) (default to False)
    inhibit_connected_line_updates = False # bool | Do not present the identity of the newly connected channel to other bridge members (optional) (default to False)

    try:
        # Add a channel to a bridge.
        api_instance.add_channel(bridge_id, channel, role=role, absorb_dtmf=absorb_dtmf, mute=mute, inhibit_connected_line_updates=inhibit_connected_line_updates)
    except Exception as e:
        print("Exception when calling BridgesApi->add_channel: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bridge_id** | **str**| Bridge&#39;s id | 
 **channel** | [**List[str]**](str.md)| Ids of channels to add to bridge | 
 **role** | **str**| Channel&#39;s role in the bridge | [optional] 
 **absorb_dtmf** | **bool**| Absorb DTMF coming from this channel, preventing it to pass through to the bridge | [optional] [default to False]
 **mute** | **bool**| Mute audio from this channel, preventing it to pass through to the bridge | [optional] [default to False]
 **inhibit_connected_line_updates** | **bool**| Do not present the identity of the newly connected channel to other bridge members | [optional] [default to False]

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

# **clear_video_source**
> clear_video_source(bridge_id)

Removes any explicit video source in a multi-party mixing bridge. This operation has no effect on bridges with two or fewer participants. When no explicit video source is set, talk detection will be used to determine the active video stream.

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
with ari_sync_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ari_sync_sdk.BridgesApi(api_client)
    bridge_id = 'bridge_id_example' # str | Bridge's id

    try:
        # Removes any explicit video source in a multi-party mixing bridge. This operation has no effect on bridges with two or fewer participants. When no explicit video source is set, talk detection will be used to determine the active video stream.
        api_instance.clear_video_source(bridge_id)
    except Exception as e:
        print("Exception when calling BridgesApi->clear_video_source: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bridge_id** | **str**| Bridge&#39;s id | 

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

# **create**
> Bridge create(type=type, bridge_id=bridge_id, name=name)

Create a new bridge.

This bridge persists until it has been shut down, or Asterisk has been shut down.

### Example

```python
import time
import os
import ari_sync_sdk
from ari_sync_sdk.models.bridge import Bridge
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
    api_instance = ari_sync_sdk.BridgesApi(api_client)
    type = 'type_example' # str | Comma separated list of bridge type attributes (mixing, holding, dtmf_events, proxy_media, video_sfu). (optional)
    bridge_id = 'bridge_id_example' # str | Unique ID to give to the bridge being created. (optional)
    name = 'name_example' # str | Name to give to the bridge being created. (optional)

    try:
        # Create a new bridge.
        api_response = api_instance.create(type=type, bridge_id=bridge_id, name=name)
        print("The response of BridgesApi->create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BridgesApi->create: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | **str**| Comma separated list of bridge type attributes (mixing, holding, dtmf_events, proxy_media, video_sfu). | [optional] 
 **bridge_id** | **str**| Unique ID to give to the bridge being created. | [optional] 
 **name** | **str**| Name to give to the bridge being created. | [optional] 

### Return type

[**Bridge**](Bridge.md)

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

# **create_with_id**
> Bridge create_with_id(bridge_id, type=type, name=name)

Create a new bridge or updates an existing one.

This bridge persists until it has been shut down, or Asterisk has been shut down.

### Example

```python
import time
import os
import ari_sync_sdk
from ari_sync_sdk.models.bridge import Bridge
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
    api_instance = ari_sync_sdk.BridgesApi(api_client)
    bridge_id = 'bridge_id_example' # str | Unique ID to give to the bridge being created.
    type = 'type_example' # str | Comma separated list of bridge type attributes (mixing, holding, dtmf_events, proxy_media, video_sfu) to set. (optional)
    name = 'name_example' # str | Set the name of the bridge. (optional)

    try:
        # Create a new bridge or updates an existing one.
        api_response = api_instance.create_with_id(bridge_id, type=type, name=name)
        print("The response of BridgesApi->create_with_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BridgesApi->create_with_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bridge_id** | **str**| Unique ID to give to the bridge being created. | 
 **type** | **str**| Comma separated list of bridge type attributes (mixing, holding, dtmf_events, proxy_media, video_sfu) to set. | [optional] 
 **name** | **str**| Set the name of the bridge. | [optional] 

### Return type

[**Bridge**](Bridge.md)

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

# **destroy**
> destroy(bridge_id)

Shut down a bridge.

If any channels are in this bridge, they will be removed and resume whatever they were doing beforehand.

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
with ari_sync_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ari_sync_sdk.BridgesApi(api_client)
    bridge_id = 'bridge_id_example' # str | Bridge's id

    try:
        # Shut down a bridge.
        api_instance.destroy(bridge_id)
    except Exception as e:
        print("Exception when calling BridgesApi->destroy: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bridge_id** | **str**| Bridge&#39;s id | 

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

# **getbridge**
> Bridge getbridge(bridge_id)

Get bridge details.

### Example

```python
import time
import os
import ari_sync_sdk
from ari_sync_sdk.models.bridge import Bridge
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
    api_instance = ari_sync_sdk.BridgesApi(api_client)
    bridge_id = 'bridge_id_example' # str | Bridge's id

    try:
        # Get bridge details.
        api_response = api_instance.getbridge(bridge_id)
        print("The response of BridgesApi->getbridge:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BridgesApi->getbridge: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bridge_id** | **str**| Bridge&#39;s id | 

### Return type

[**Bridge**](Bridge.md)

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

# **listbridges**
> List[Bridge] listbridges()

List all active bridges in Asterisk.

### Example

```python
import time
import os
import ari_sync_sdk
from ari_sync_sdk.models.bridge import Bridge
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
    api_instance = ari_sync_sdk.BridgesApi(api_client)

    try:
        # List all active bridges in Asterisk.
        api_response = api_instance.listbridges()
        print("The response of BridgesApi->listbridges:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BridgesApi->listbridges: %s\n" % e)
```



### Parameters
This endpoint does not need any parameter.

### Return type

[**List[Bridge]**](Bridge.md)

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

# **play**
> Playback play(bridge_id, media, lang=lang, offsetms=offsetms, skipms=skipms, playback_id=playback_id)

Start playback of media on a bridge.

The media URI may be any of a number of URI's. Currently sound:, recording:, number:, digits:, characters:, and tone: URI's are supported. This operation creates a playback resource that can be used to control the playback of media (pause, rewind, fast forward, etc.)

### Example

```python
import time
import os
import ari_sync_sdk
from ari_sync_sdk.models.playback import Playback
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
    api_instance = ari_sync_sdk.BridgesApi(api_client)
    bridge_id = 'bridge_id_example' # str | Bridge's id
    media = ['media_example'] # List[str] | Media URIs to play.
    lang = 'lang_example' # str | For sounds, selects language for sound. (optional)
    offsetms = 0 # int | Number of milliseconds to skip before playing. Only applies to the first URI if multiple media URIs are specified. (optional) (default to 0)
    skipms = 3000 # int | Number of milliseconds to skip for forward/reverse operations. (optional) (default to 3000)
    playback_id = 'playback_id_example' # str | Playback Id. (optional)

    try:
        # Start playback of media on a bridge.
        api_response = api_instance.play(bridge_id, media, lang=lang, offsetms=offsetms, skipms=skipms, playback_id=playback_id)
        print("The response of BridgesApi->play:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BridgesApi->play: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bridge_id** | **str**| Bridge&#39;s id | 
 **media** | [**List[str]**](str.md)| Media URIs to play. | 
 **lang** | **str**| For sounds, selects language for sound. | [optional] 
 **offsetms** | **int**| Number of milliseconds to skip before playing. Only applies to the first URI if multiple media URIs are specified. | [optional] [default to 0]
 **skipms** | **int**| Number of milliseconds to skip for forward/reverse operations. | [optional] [default to 3000]
 **playback_id** | **str**| Playback Id. | [optional] 

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

# **play_with_id**
> Playback play_with_id(bridge_id, playback_id, media, lang=lang, offsetms=offsetms, skipms=skipms)

Start playback of media on a bridge.

The media URI may be any of a number of URI's. Currently sound:, recording:, number:, digits:, characters:, and tone: URI's are supported. This operation creates a playback resource that can be used to control the playback of media (pause, rewind, fast forward, etc.)

### Example

```python
import time
import os
import ari_sync_sdk
from ari_sync_sdk.models.playback import Playback
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
    api_instance = ari_sync_sdk.BridgesApi(api_client)
    bridge_id = 'bridge_id_example' # str | Bridge's id
    playback_id = 'playback_id_example' # str | Playback ID.
    media = ['media_example'] # List[str] | Media URIs to play.
    lang = 'lang_example' # str | For sounds, selects language for sound. (optional)
    offsetms = 0 # int | Number of milliseconds to skip before playing. Only applies to the first URI if multiple media URIs are specified. (optional) (default to 0)
    skipms = 3000 # int | Number of milliseconds to skip for forward/reverse operations. (optional) (default to 3000)

    try:
        # Start playback of media on a bridge.
        api_response = api_instance.play_with_id(bridge_id, playback_id, media, lang=lang, offsetms=offsetms, skipms=skipms)
        print("The response of BridgesApi->play_with_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BridgesApi->play_with_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bridge_id** | **str**| Bridge&#39;s id | 
 **playback_id** | **str**| Playback ID. | 
 **media** | [**List[str]**](str.md)| Media URIs to play. | 
 **lang** | **str**| For sounds, selects language for sound. | [optional] 
 **offsetms** | **int**| Number of milliseconds to skip before playing. Only applies to the first URI if multiple media URIs are specified. | [optional] [default to 0]
 **skipms** | **int**| Number of milliseconds to skip for forward/reverse operations. | [optional] [default to 3000]

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

# **record**
> LiveRecording record(bridge_id, name, format, max_duration_seconds=max_duration_seconds, max_silence_seconds=max_silence_seconds, if_exists=if_exists, beep=beep, terminate_on=terminate_on)

Start a recording.

This records the mixed audio from all channels participating in this bridge.

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
with ari_sync_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ari_sync_sdk.BridgesApi(api_client)
    bridge_id = 'bridge_id_example' # str | Bridge's id
    name = 'name_example' # str | Recording's filename
    format = 'format_example' # str | Format to encode audio in
    max_duration_seconds = 0 # int | Maximum duration of the recording, in seconds. 0 for no limit. (optional) (default to 0)
    max_silence_seconds = 0 # int | Maximum duration of silence, in seconds. 0 for no limit. (optional) (default to 0)
    if_exists = 'fail' # str | Action to take if a recording with the same name already exists. (optional) (default to 'fail')
    beep = False # bool | Play beep when recording begins (optional) (default to False)
    terminate_on = 'none' # str | DTMF input to terminate recording. (optional) (default to 'none')

    try:
        # Start a recording.
        api_response = api_instance.record(bridge_id, name, format, max_duration_seconds=max_duration_seconds, max_silence_seconds=max_silence_seconds, if_exists=if_exists, beep=beep, terminate_on=terminate_on)
        print("The response of BridgesApi->record:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BridgesApi->record: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bridge_id** | **str**| Bridge&#39;s id | 
 **name** | **str**| Recording&#39;s filename | 
 **format** | **str**| Format to encode audio in | 
 **max_duration_seconds** | **int**| Maximum duration of the recording, in seconds. 0 for no limit. | [optional] [default to 0]
 **max_silence_seconds** | **int**| Maximum duration of silence, in seconds. 0 for no limit. | [optional] [default to 0]
 **if_exists** | **str**| Action to take if a recording with the same name already exists. | [optional] [default to &#39;fail&#39;]
 **beep** | **bool**| Play beep when recording begins | [optional] [default to False]
 **terminate_on** | **str**| DTMF input to terminate recording. | [optional] [default to &#39;none&#39;]

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

# **remove_channel**
> remove_channel(bridge_id, channel)

Remove a channel from a bridge.

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
with ari_sync_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ari_sync_sdk.BridgesApi(api_client)
    bridge_id = 'bridge_id_example' # str | Bridge's id
    channel = ['channel_example'] # List[str] | Ids of channels to remove from bridge

    try:
        # Remove a channel from a bridge.
        api_instance.remove_channel(bridge_id, channel)
    except Exception as e:
        print("Exception when calling BridgesApi->remove_channel: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bridge_id** | **str**| Bridge&#39;s id | 
 **channel** | [**List[str]**](str.md)| Ids of channels to remove from bridge | 

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

# **set_video_source**
> set_video_source(bridge_id, channel_id)

Set a channel as the video source in a multi-party mixing bridge. This operation has no effect on bridges with two or fewer participants.

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
with ari_sync_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ari_sync_sdk.BridgesApi(api_client)
    bridge_id = 'bridge_id_example' # str | Bridge's id
    channel_id = 'channel_id_example' # str | Channel's id

    try:
        # Set a channel as the video source in a multi-party mixing bridge. This operation has no effect on bridges with two or fewer participants.
        api_instance.set_video_source(bridge_id, channel_id)
    except Exception as e:
        print("Exception when calling BridgesApi->set_video_source: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bridge_id** | **str**| Bridge&#39;s id | 
 **channel_id** | **str**| Channel&#39;s id | 

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

# **start_moh**
> start_moh(bridge_id, moh_class=moh_class)

Play music on hold to a bridge or change the MOH class that is playing.

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
with ari_sync_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ari_sync_sdk.BridgesApi(api_client)
    bridge_id = 'bridge_id_example' # str | Bridge's id
    moh_class = 'moh_class_example' # str | Channel's id (optional)

    try:
        # Play music on hold to a bridge or change the MOH class that is playing.
        api_instance.start_moh(bridge_id, moh_class=moh_class)
    except Exception as e:
        print("Exception when calling BridgesApi->start_moh: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bridge_id** | **str**| Bridge&#39;s id | 
 **moh_class** | **str**| Channel&#39;s id | [optional] 

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

# **stop_moh**
> stop_moh(bridge_id)

Stop playing music on hold to a bridge.

This will only stop music on hold being played via POST bridges/{bridgeId}/moh.

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
with ari_sync_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ari_sync_sdk.BridgesApi(api_client)
    bridge_id = 'bridge_id_example' # str | Bridge's id

    try:
        # Stop playing music on hold to a bridge.
        api_instance.stop_moh(bridge_id)
    except Exception as e:
        print("Exception when calling BridgesApi->stop_moh: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bridge_id** | **str**| Bridge&#39;s id | 

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

