# ari_sync_sdk.ChannelsApi

All URIs are relative to *http://localhost:8088/ari*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_moh**](ChannelsApi.md#add_moh) | **POST** /channels/{channelId}/moh | Play music on hold to a channel.
[**answer**](ChannelsApi.md#answer) | **POST** /channels/{channelId}/answer | Answer a channel.
[**continue_in_dialplan**](ChannelsApi.md#continue_in_dialplan) | **POST** /channels/{channelId}/continue | Exit application; continue execution in the dialplan.
[**createchannel**](ChannelsApi.md#createchannel) | **POST** /channels/create | Create channel.
[**deletemoh**](ChannelsApi.md#deletemoh) | **DELETE** /channels/{channelId}/moh | Stop playing music on hold to a channel.
[**dial**](ChannelsApi.md#dial) | **POST** /channels/{channelId}/dial | Dial a created channel.
[**external_media**](ChannelsApi.md#external_media) | **POST** /channels/externalMedia | Start an External Media session.
[**get_channel_var**](ChannelsApi.md#get_channel_var) | **GET** /channels/{channelId}/variable | Get the value of a channel variable or function.
[**getchannel**](ChannelsApi.md#getchannel) | **GET** /channels/{channelId} | Channel details.
[**hangup**](ChannelsApi.md#hangup) | **DELETE** /channels/{channelId} | Delete (i.e. hangup) a channel.
[**hold**](ChannelsApi.md#hold) | **POST** /channels/{channelId}/hold | Hold a channel.
[**listchannels**](ChannelsApi.md#listchannels) | **GET** /channels | List all active channels in Asterisk.
[**move**](ChannelsApi.md#move) | **POST** /channels/{channelId}/move | Move the channel from one Stasis application to another.
[**mute**](ChannelsApi.md#mute) | **POST** /channels/{channelId}/mute | Mute a channel.
[**originate**](ChannelsApi.md#originate) | **POST** /channels | Create a new channel (originate).
[**originate_with_id**](ChannelsApi.md#originate_with_id) | **POST** /channels/{channelId} | Create a new channel (originate with id).
[**play_sound_with_id**](ChannelsApi.md#play_sound_with_id) | **POST** /channels/{channelId}/play/{playbackId} | Start playback of media and specify the playbackId.
[**playsound**](ChannelsApi.md#playsound) | **POST** /channels/{channelId}/play | Start playback of media.
[**recordchannel**](ChannelsApi.md#recordchannel) | **POST** /channels/{channelId}/record | Start a recording.
[**redirect**](ChannelsApi.md#redirect) | **POST** /channels/{channelId}/redirect | Redirect the channel to a different location.
[**ring**](ChannelsApi.md#ring) | **POST** /channels/{channelId}/ring | Indicate ringing to a channel.
[**ring_stop**](ChannelsApi.md#ring_stop) | **DELETE** /channels/{channelId}/ring | Stop ringing indication on a channel if locally generated.
[**rtpstatistics**](ChannelsApi.md#rtpstatistics) | **GET** /channels/{channelId}/rtp_statistics | RTP stats on a channel.
[**send_dtmf**](ChannelsApi.md#send_dtmf) | **POST** /channels/{channelId}/dtmf | Send provided DTMF to a given channel.
[**set_channel_var**](ChannelsApi.md#set_channel_var) | **POST** /channels/{channelId}/variable | Set the value of a channel variable or function.
[**snoop_channel**](ChannelsApi.md#snoop_channel) | **POST** /channels/{channelId}/snoop | Start snooping.
[**snoop_channel_with_id**](ChannelsApi.md#snoop_channel_with_id) | **POST** /channels/{channelId}/snoop/{snoopId} | Start snooping.
[**start_silence**](ChannelsApi.md#start_silence) | **POST** /channels/{channelId}/silence | Play silence to a channel.
[**stop_silence**](ChannelsApi.md#stop_silence) | **DELETE** /channels/{channelId}/silence | Stop playing silence to a channel.
[**unhold**](ChannelsApi.md#unhold) | **DELETE** /channels/{channelId}/hold | Remove a channel from hold.
[**unmute**](ChannelsApi.md#unmute) | **DELETE** /channels/{channelId}/mute | Unmute a channel.


# **add_moh**
> add_moh(channel_id, moh_class=moh_class)

Play music on hold to a channel.

Using media operations such as /play on a channel playing MOH in this manner will suspend MOH without resuming automatically. If continuing music on hold is desired, the stasis application must reinitiate music on hold.

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
    api_instance = ari_sync_sdk.ChannelsApi(api_client)
    channel_id = 'channel_id_example' # str | Channel's id
    moh_class = 'moh_class_example' # str | Music on hold class to use (optional)

    try:
        # Play music on hold to a channel.
        await api_instance.add_moh(channel_id, moh_class=moh_class)
    except Exception as e:
        print("Exception when calling ChannelsApi->add_moh: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channel_id** | **str**| Channel&#39;s id | 
 **moh_class** | **str**| Music on hold class to use | [optional] 

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

# **answer**
> answer(channel_id)

Answer a channel.

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
    api_instance = ari_sync_sdk.ChannelsApi(api_client)
    channel_id = 'channel_id_example' # str | Channel's id

    try:
        # Answer a channel.
        await api_instance.answer(channel_id)
    except Exception as e:
        print("Exception when calling ChannelsApi->answer: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
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

# **continue_in_dialplan**
> continue_in_dialplan(channel_id, context=context, extension=extension, priority=priority, label=label)

Exit application; continue execution in the dialplan.

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
    api_instance = ari_sync_sdk.ChannelsApi(api_client)
    channel_id = 'channel_id_example' # str | Channel's id
    context = 'context_example' # str | The context to continue to. (optional)
    extension = 'extension_example' # str | The extension to continue to. (optional)
    priority = 56 # int | The priority to continue to. (optional)
    label = 'label_example' # str | The label to continue to - will supersede 'priority' if both are provided. (optional)

    try:
        # Exit application; continue execution in the dialplan.
        await api_instance.continue_in_dialplan(channel_id, context=context, extension=extension, priority=priority, label=label)
    except Exception as e:
        print("Exception when calling ChannelsApi->continue_in_dialplan: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channel_id** | **str**| Channel&#39;s id | 
 **context** | **str**| The context to continue to. | [optional] 
 **extension** | **str**| The extension to continue to. | [optional] 
 **priority** | **int**| The priority to continue to. | [optional] 
 **label** | **str**| The label to continue to - will supersede &#39;priority&#39; if both are provided. | [optional] 

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

# **createchannel**
> Channel createchannel(endpoint, app, app_args=app_args, channel_id=channel_id, other_channel_id=other_channel_id, originator=originator, formats=formats, variables=variables)

Create channel.

### Example

```python
import time
import os
import ari_sync_sdk
from ari_sync_sdk.models.channel import Channel
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
    api_instance = ari_sync_sdk.ChannelsApi(api_client)
    endpoint = 'endpoint_example' # str | Endpoint for channel communication
    app = 'app_example' # str | Stasis Application to place channel into
    app_args = 'app_args_example' # str | The application arguments to pass to the Stasis application provided by 'app'. Mutually exclusive with 'context', 'extension', 'priority', and 'label'. (optional)
    channel_id = 'channel_id_example' # str | The unique id to assign the channel on creation. (optional)
    other_channel_id = 'other_channel_id_example' # str | The unique id to assign the second channel when using local channels. (optional)
    originator = 'originator_example' # str | Unique ID of the calling channel (optional)
    formats = 'formats_example' # str | The format name capability list to use if originator is not specified. Ex. \"ulaw,slin16\".  Format names can be found with \"core show codecs\". (optional)
    variables = None # object | The \"variables\" key in the body object holds variable key/value pairs to set on the channel on creation. Other keys in the body object are interpreted as query parameters. Ex. { \"endpoint\": \"SIP/Alice\", \"variables\": { \"CALLERID(name)\": \"Alice\" } } (optional)

    try:
        # Create channel.
        api_response = await api_instance.createchannel(endpoint, app, app_args=app_args, channel_id=channel_id, other_channel_id=other_channel_id, originator=originator, formats=formats, variables=variables)
        print("The response of ChannelsApi->createchannel:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ChannelsApi->createchannel: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **endpoint** | **str**| Endpoint for channel communication | 
 **app** | **str**| Stasis Application to place channel into | 
 **app_args** | **str**| The application arguments to pass to the Stasis application provided by &#39;app&#39;. Mutually exclusive with &#39;context&#39;, &#39;extension&#39;, &#39;priority&#39;, and &#39;label&#39;. | [optional] 
 **channel_id** | **str**| The unique id to assign the channel on creation. | [optional] 
 **other_channel_id** | **str**| The unique id to assign the second channel when using local channels. | [optional] 
 **originator** | **str**| Unique ID of the calling channel | [optional] 
 **formats** | **str**| The format name capability list to use if originator is not specified. Ex. \&quot;ulaw,slin16\&quot;.  Format names can be found with \&quot;core show codecs\&quot;. | [optional] 
 **variables** | **object**| The \&quot;variables\&quot; key in the body object holds variable key/value pairs to set on the channel on creation. Other keys in the body object are interpreted as query parameters. Ex. { \&quot;endpoint\&quot;: \&quot;SIP/Alice\&quot;, \&quot;variables\&quot;: { \&quot;CALLERID(name)\&quot;: \&quot;Alice\&quot; } } | [optional] 

### Return type

[**Channel**](Channel.md)

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

# **deletemoh**
> deletemoh(channel_id)

Stop playing music on hold to a channel.

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
    api_instance = ari_sync_sdk.ChannelsApi(api_client)
    channel_id = 'channel_id_example' # str | Channel's id

    try:
        # Stop playing music on hold to a channel.
        await api_instance.deletemoh(channel_id)
    except Exception as e:
        print("Exception when calling ChannelsApi->deletemoh: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
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

# **dial**
> dial(channel_id, caller=caller, timeout=timeout)

Dial a created channel.

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
    api_instance = ari_sync_sdk.ChannelsApi(api_client)
    channel_id = 'channel_id_example' # str | Channel's id
    caller = 'caller_example' # str | Channel ID of caller (optional)
    timeout = 0 # int | Dial timeout (optional) (default to 0)

    try:
        # Dial a created channel.
        await api_instance.dial(channel_id, caller=caller, timeout=timeout)
    except Exception as e:
        print("Exception when calling ChannelsApi->dial: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channel_id** | **str**| Channel&#39;s id | 
 **caller** | **str**| Channel ID of caller | [optional] 
 **timeout** | **int**| Dial timeout | [optional] [default to 0]

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

# **external_media**
> Channel external_media(app, external_host, format, channel_id=channel_id, encapsulation=encapsulation, transport=transport, connection_type=connection_type, direction=direction, data=data, variables=variables)

Start an External Media session.

Create a channel to an External Media source/sink.

### Example

```python
import time
import os
import ari_sync_sdk
from ari_sync_sdk.models.channel import Channel
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
    api_instance = ari_sync_sdk.ChannelsApi(api_client)
    app = 'app_example' # str | Stasis Application to place channel into
    external_host = 'external_host_example' # str | Hostname/ip:port of external host
    format = 'format_example' # str | Format to encode audio in
    channel_id = 'channel_id_example' # str | The unique id to assign the channel on creation. (optional)
    encapsulation = 'rtp' # str | Payload encapsulation protocol (optional) (default to 'rtp')
    transport = 'udp' # str | Transport protocol (optional) (default to 'udp')
    connection_type = 'client' # str | Connection type (client/server) (optional) (default to 'client')
    direction = 'both' # str | External media direction (optional) (default to 'both')
    data = 'data_example' # str | An arbitrary data field (optional)
    variables = None # object | The \"variables\" key in the body object holds variable key/value pairs to set on the channel on creation. Other keys in the body object are interpreted as query parameters. Ex. { \"endpoint\": \"SIP/Alice\", \"variables\": { \"CALLERID(name)\": \"Alice\" } } (optional)

    try:
        # Start an External Media session.
        api_response = await api_instance.external_media(app, external_host, format, channel_id=channel_id, encapsulation=encapsulation, transport=transport, connection_type=connection_type, direction=direction, data=data, variables=variables)
        print("The response of ChannelsApi->external_media:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ChannelsApi->external_media: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app** | **str**| Stasis Application to place channel into | 
 **external_host** | **str**| Hostname/ip:port of external host | 
 **format** | **str**| Format to encode audio in | 
 **channel_id** | **str**| The unique id to assign the channel on creation. | [optional] 
 **encapsulation** | **str**| Payload encapsulation protocol | [optional] [default to &#39;rtp&#39;]
 **transport** | **str**| Transport protocol | [optional] [default to &#39;udp&#39;]
 **connection_type** | **str**| Connection type (client/server) | [optional] [default to &#39;client&#39;]
 **direction** | **str**| External media direction | [optional] [default to &#39;both&#39;]
 **data** | **str**| An arbitrary data field | [optional] 
 **variables** | **object**| The \&quot;variables\&quot; key in the body object holds variable key/value pairs to set on the channel on creation. Other keys in the body object are interpreted as query parameters. Ex. { \&quot;endpoint\&quot;: \&quot;SIP/Alice\&quot;, \&quot;variables\&quot;: { \&quot;CALLERID(name)\&quot;: \&quot;Alice\&quot; } } | [optional] 

### Return type

[**Channel**](Channel.md)

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

# **get_channel_var**
> Variable get_channel_var(channel_id, variable)

Get the value of a channel variable or function.

### Example

```python
import time
import os
import ari_sync_sdk
from ari_sync_sdk.models.variable import Variable
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
    api_instance = ari_sync_sdk.ChannelsApi(api_client)
    channel_id = 'channel_id_example' # str | Channel's id
    variable = 'variable_example' # str | The channel variable or function to get

    try:
        # Get the value of a channel variable or function.
        api_response = await api_instance.get_channel_var(channel_id, variable)
        print("The response of ChannelsApi->get_channel_var:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ChannelsApi->get_channel_var: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channel_id** | **str**| Channel&#39;s id | 
 **variable** | **str**| The channel variable or function to get | 

### Return type

[**Variable**](Variable.md)

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

# **getchannel**
> Channel getchannel(channel_id)

Channel details.

### Example

```python
import time
import os
import ari_sync_sdk
from ari_sync_sdk.models.channel import Channel
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
    api_instance = ari_sync_sdk.ChannelsApi(api_client)
    channel_id = 'channel_id_example' # str | Channel's id

    try:
        # Channel details.
        api_response = await api_instance.getchannel(channel_id)
        print("The response of ChannelsApi->getchannel:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ChannelsApi->getchannel: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channel_id** | **str**| Channel&#39;s id | 

### Return type

[**Channel**](Channel.md)

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

# **hangup**
> hangup(channel_id, reason_code=reason_code, reason=reason)

Delete (i.e. hangup) a channel.

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
    api_instance = ari_sync_sdk.ChannelsApi(api_client)
    channel_id = 'channel_id_example' # str | Channel's id
    reason_code = 'reason_code_example' # str | The reason code for hanging up the channel for detail use. Mutually exclusive with 'reason'. See detail hangup codes at here. https://wiki.asterisk.org/wiki/display/AST/Hangup+Cause+Mappings (optional)
    reason = 'reason_example' # str | Reason for hanging up the channel for simple use. Mutually exclusive with 'reason_code'. (optional)

    try:
        # Delete (i.e. hangup) a channel.
        await api_instance.hangup(channel_id, reason_code=reason_code, reason=reason)
    except Exception as e:
        print("Exception when calling ChannelsApi->hangup: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channel_id** | **str**| Channel&#39;s id | 
 **reason_code** | **str**| The reason code for hanging up the channel for detail use. Mutually exclusive with &#39;reason&#39;. See detail hangup codes at here. https://wiki.asterisk.org/wiki/display/AST/Hangup+Cause+Mappings | [optional] 
 **reason** | **str**| Reason for hanging up the channel for simple use. Mutually exclusive with &#39;reason_code&#39;. | [optional] 

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

# **hold**
> hold(channel_id)

Hold a channel.

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
    api_instance = ari_sync_sdk.ChannelsApi(api_client)
    channel_id = 'channel_id_example' # str | Channel's id

    try:
        # Hold a channel.
        await api_instance.hold(channel_id)
    except Exception as e:
        print("Exception when calling ChannelsApi->hold: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
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

# **listchannels**
> List[Channel] listchannels()

List all active channels in Asterisk.

### Example

```python
import time
import os
import ari_sync_sdk
from ari_sync_sdk.models.channel import Channel
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
    api_instance = ari_sync_sdk.ChannelsApi(api_client)

    try:
        # List all active channels in Asterisk.
        api_response = await api_instance.listchannels()
        print("The response of ChannelsApi->listchannels:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ChannelsApi->listchannels: %s\n" % e)
```



### Parameters
This endpoint does not need any parameter.

### Return type

[**List[Channel]**](Channel.md)

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

# **move**
> move(channel_id, app, app_args=app_args)

Move the channel from one Stasis application to another.

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
    api_instance = ari_sync_sdk.ChannelsApi(api_client)
    channel_id = 'channel_id_example' # str | Channel's id
    app = 'app_example' # str | The channel will be passed to this Stasis application.
    app_args = 'app_args_example' # str | The application arguments to pass to the Stasis application provided by 'app'. (optional)

    try:
        # Move the channel from one Stasis application to another.
        await api_instance.move(channel_id, app, app_args=app_args)
    except Exception as e:
        print("Exception when calling ChannelsApi->move: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channel_id** | **str**| Channel&#39;s id | 
 **app** | **str**| The channel will be passed to this Stasis application. | 
 **app_args** | **str**| The application arguments to pass to the Stasis application provided by &#39;app&#39;. | [optional] 

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

# **mute**
> mute(channel_id, direction=direction)

Mute a channel.

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
    api_instance = ari_sync_sdk.ChannelsApi(api_client)
    channel_id = 'channel_id_example' # str | Channel's id
    direction = 'both' # str | Direction in which to mute audio (optional) (default to 'both')

    try:
        # Mute a channel.
        await api_instance.mute(channel_id, direction=direction)
    except Exception as e:
        print("Exception when calling ChannelsApi->mute: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channel_id** | **str**| Channel&#39;s id | 
 **direction** | **str**| Direction in which to mute audio | [optional] [default to &#39;both&#39;]

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

# **originate**
> Channel originate(endpoint, extension=extension, context=context, priority=priority, label=label, app=app, app_args=app_args, caller_id=caller_id, timeout=timeout, channel_id=channel_id, other_channel_id=other_channel_id, originator=originator, formats=formats, variables=variables)

Create a new channel (originate).

The new channel is created immediately and a snapshot of it returned. If a Stasis application is provided it will be automatically subscribed to the originated channel for further events and updates.

### Example

```python
import time
import os
import ari_sync_sdk
from ari_sync_sdk.models.channel import Channel
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
    api_instance = ari_sync_sdk.ChannelsApi(api_client)
    endpoint = 'endpoint_example' # str | Endpoint to call.
    extension = 'extension_example' # str | The extension to dial after the endpoint answers. Mutually exclusive with 'app'. (optional)
    context = 'context_example' # str | The context to dial after the endpoint answers. If omitted, uses 'default'. Mutually exclusive with 'app'. (optional)
    priority = 56 # int | The priority to dial after the endpoint answers. If omitted, uses 1. Mutually exclusive with 'app'. (optional)
    label = 'label_example' # str | The label to dial after the endpoint answers. Will supersede 'priority' if provided. Mutually exclusive with 'app'. (optional)
    app = 'app_example' # str | The application that is subscribed to the originated channel. When the channel is answered, it will be passed to this Stasis application. Mutually exclusive with 'context', 'extension', 'priority', and 'label'. (optional)
    app_args = 'app_args_example' # str | The application arguments to pass to the Stasis application provided by 'app'. Mutually exclusive with 'context', 'extension', 'priority', and 'label'. (optional)
    caller_id = 'caller_id_example' # str | CallerID to use when dialing the endpoint or extension. (optional)
    timeout = 30 # int | Timeout (in seconds) before giving up dialing, or -1 for no timeout. (optional) (default to 30)
    channel_id = 'channel_id_example' # str | The unique id to assign the channel on creation. (optional)
    other_channel_id = 'other_channel_id_example' # str | The unique id to assign the second channel when using local channels. (optional)
    originator = 'originator_example' # str | The unique id of the channel which is originating this one. (optional)
    formats = 'formats_example' # str | The format name capability list to use if originator is not specified. Ex. \"ulaw,slin16\".  Format names can be found with \"core show codecs\". (optional)
    variables = None # object | The \"variables\" key in the body object holds variable key/value pairs to set on the channel on creation. Other keys in the body object are interpreted as query parameters. Ex. { \"endpoint\": \"SIP/Alice\", \"variables\": { \"CALLERID(name)\": \"Alice\" } } (optional)

    try:
        # Create a new channel (originate).
        api_response = await api_instance.originate(endpoint, extension=extension, context=context, priority=priority, label=label, app=app, app_args=app_args, caller_id=caller_id, timeout=timeout, channel_id=channel_id, other_channel_id=other_channel_id, originator=originator, formats=formats, variables=variables)
        print("The response of ChannelsApi->originate:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ChannelsApi->originate: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **endpoint** | **str**| Endpoint to call. | 
 **extension** | **str**| The extension to dial after the endpoint answers. Mutually exclusive with &#39;app&#39;. | [optional] 
 **context** | **str**| The context to dial after the endpoint answers. If omitted, uses &#39;default&#39;. Mutually exclusive with &#39;app&#39;. | [optional] 
 **priority** | **int**| The priority to dial after the endpoint answers. If omitted, uses 1. Mutually exclusive with &#39;app&#39;. | [optional] 
 **label** | **str**| The label to dial after the endpoint answers. Will supersede &#39;priority&#39; if provided. Mutually exclusive with &#39;app&#39;. | [optional] 
 **app** | **str**| The application that is subscribed to the originated channel. When the channel is answered, it will be passed to this Stasis application. Mutually exclusive with &#39;context&#39;, &#39;extension&#39;, &#39;priority&#39;, and &#39;label&#39;. | [optional] 
 **app_args** | **str**| The application arguments to pass to the Stasis application provided by &#39;app&#39;. Mutually exclusive with &#39;context&#39;, &#39;extension&#39;, &#39;priority&#39;, and &#39;label&#39;. | [optional] 
 **caller_id** | **str**| CallerID to use when dialing the endpoint or extension. | [optional] 
 **timeout** | **int**| Timeout (in seconds) before giving up dialing, or -1 for no timeout. | [optional] [default to 30]
 **channel_id** | **str**| The unique id to assign the channel on creation. | [optional] 
 **other_channel_id** | **str**| The unique id to assign the second channel when using local channels. | [optional] 
 **originator** | **str**| The unique id of the channel which is originating this one. | [optional] 
 **formats** | **str**| The format name capability list to use if originator is not specified. Ex. \&quot;ulaw,slin16\&quot;.  Format names can be found with \&quot;core show codecs\&quot;. | [optional] 
 **variables** | **object**| The \&quot;variables\&quot; key in the body object holds variable key/value pairs to set on the channel on creation. Other keys in the body object are interpreted as query parameters. Ex. { \&quot;endpoint\&quot;: \&quot;SIP/Alice\&quot;, \&quot;variables\&quot;: { \&quot;CALLERID(name)\&quot;: \&quot;Alice\&quot; } } | [optional] 

### Return type

[**Channel**](Channel.md)

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

# **originate_with_id**
> Channel originate_with_id(channel_id, endpoint, extension=extension, context=context, priority=priority, label=label, app=app, app_args=app_args, caller_id=caller_id, timeout=timeout, other_channel_id=other_channel_id, originator=originator, formats=formats, variables=variables)

Create a new channel (originate with id).

The new channel is created immediately and a snapshot of it returned. If a Stasis application is provided it will be automatically subscribed to the originated channel for further events and updates.

### Example

```python
import time
import os
import ari_sync_sdk
from ari_sync_sdk.models.channel import Channel
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
    api_instance = ari_sync_sdk.ChannelsApi(api_client)
    channel_id = 'channel_id_example' # str | The unique id to assign the channel on creation.
    endpoint = 'endpoint_example' # str | Endpoint to call.
    extension = 'extension_example' # str | The extension to dial after the endpoint answers. Mutually exclusive with 'app'. (optional)
    context = 'context_example' # str | The context to dial after the endpoint answers. If omitted, uses 'default'. Mutually exclusive with 'app'. (optional)
    priority = 56 # int | The priority to dial after the endpoint answers. If omitted, uses 1. Mutually exclusive with 'app'. (optional)
    label = 'label_example' # str | The label to dial after the endpoint answers. Will supersede 'priority' if provided. Mutually exclusive with 'app'. (optional)
    app = 'app_example' # str | The application that is subscribed to the originated channel. When the channel is answered, it will be passed to this Stasis application. Mutually exclusive with 'context', 'extension', 'priority', and 'label'. (optional)
    app_args = 'app_args_example' # str | The application arguments to pass to the Stasis application provided by 'app'. Mutually exclusive with 'context', 'extension', 'priority', and 'label'. (optional)
    caller_id = 'caller_id_example' # str | CallerID to use when dialing the endpoint or extension. (optional)
    timeout = 30 # int | Timeout (in seconds) before giving up dialing, or -1 for no timeout. (optional) (default to 30)
    other_channel_id = 'other_channel_id_example' # str | The unique id to assign the second channel when using local channels. (optional)
    originator = 'originator_example' # str | The unique id of the channel which is originating this one. (optional)
    formats = 'formats_example' # str | The format name capability list to use if originator is not specified. Ex. \"ulaw,slin16\".  Format names can be found with \"core show codecs\". (optional)
    variables = None # object | The \"variables\" key in the body object holds variable key/value pairs to set on the channel on creation. Other keys in the body object are interpreted as query parameters. Ex. { \"endpoint\": \"SIP/Alice\", \"variables\": { \"CALLERID(name)\": \"Alice\" } } (optional)

    try:
        # Create a new channel (originate with id).
        api_response = await api_instance.originate_with_id(channel_id, endpoint, extension=extension, context=context, priority=priority, label=label, app=app, app_args=app_args, caller_id=caller_id, timeout=timeout, other_channel_id=other_channel_id, originator=originator, formats=formats, variables=variables)
        print("The response of ChannelsApi->originate_with_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ChannelsApi->originate_with_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channel_id** | **str**| The unique id to assign the channel on creation. | 
 **endpoint** | **str**| Endpoint to call. | 
 **extension** | **str**| The extension to dial after the endpoint answers. Mutually exclusive with &#39;app&#39;. | [optional] 
 **context** | **str**| The context to dial after the endpoint answers. If omitted, uses &#39;default&#39;. Mutually exclusive with &#39;app&#39;. | [optional] 
 **priority** | **int**| The priority to dial after the endpoint answers. If omitted, uses 1. Mutually exclusive with &#39;app&#39;. | [optional] 
 **label** | **str**| The label to dial after the endpoint answers. Will supersede &#39;priority&#39; if provided. Mutually exclusive with &#39;app&#39;. | [optional] 
 **app** | **str**| The application that is subscribed to the originated channel. When the channel is answered, it will be passed to this Stasis application. Mutually exclusive with &#39;context&#39;, &#39;extension&#39;, &#39;priority&#39;, and &#39;label&#39;. | [optional] 
 **app_args** | **str**| The application arguments to pass to the Stasis application provided by &#39;app&#39;. Mutually exclusive with &#39;context&#39;, &#39;extension&#39;, &#39;priority&#39;, and &#39;label&#39;. | [optional] 
 **caller_id** | **str**| CallerID to use when dialing the endpoint or extension. | [optional] 
 **timeout** | **int**| Timeout (in seconds) before giving up dialing, or -1 for no timeout. | [optional] [default to 30]
 **other_channel_id** | **str**| The unique id to assign the second channel when using local channels. | [optional] 
 **originator** | **str**| The unique id of the channel which is originating this one. | [optional] 
 **formats** | **str**| The format name capability list to use if originator is not specified. Ex. \&quot;ulaw,slin16\&quot;.  Format names can be found with \&quot;core show codecs\&quot;. | [optional] 
 **variables** | **object**| The \&quot;variables\&quot; key in the body object holds variable key/value pairs to set on the channel on creation. Other keys in the body object are interpreted as query parameters. Ex. { \&quot;endpoint\&quot;: \&quot;SIP/Alice\&quot;, \&quot;variables\&quot;: { \&quot;CALLERID(name)\&quot;: \&quot;Alice\&quot; } } | [optional] 

### Return type

[**Channel**](Channel.md)

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

# **play_sound_with_id**
> Playback play_sound_with_id(channel_id, playback_id, media, lang=lang, offsetms=offsetms, skipms=skipms)

Start playback of media and specify the playbackId.

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
async with ari_sync_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ari_sync_sdk.ChannelsApi(api_client)
    channel_id = 'channel_id_example' # str | Channel's id
    playback_id = 'playback_id_example' # str | Playback ID.
    media = ['media_example'] # List[str] | Media URIs to play.
    lang = 'lang_example' # str | For sounds, selects language for sound. (optional)
    offsetms = 56 # int | Number of milliseconds to skip before playing. Only applies to the first URI if multiple media URIs are specified. (optional)
    skipms = 3000 # int | Number of milliseconds to skip for forward/reverse operations. (optional) (default to 3000)

    try:
        # Start playback of media and specify the playbackId.
        api_response = await api_instance.play_sound_with_id(channel_id, playback_id, media, lang=lang, offsetms=offsetms, skipms=skipms)
        print("The response of ChannelsApi->play_sound_with_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ChannelsApi->play_sound_with_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channel_id** | **str**| Channel&#39;s id | 
 **playback_id** | **str**| Playback ID. | 
 **media** | [**List[str]**](str.md)| Media URIs to play. | 
 **lang** | **str**| For sounds, selects language for sound. | [optional] 
 **offsetms** | **int**| Number of milliseconds to skip before playing. Only applies to the first URI if multiple media URIs are specified. | [optional] 
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

# **playsound**
> Playback playsound(channel_id, media, lang=lang, offsetms=offsetms, skipms=skipms, playback_id=playback_id)

Start playback of media.

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
async with ari_sync_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ari_sync_sdk.ChannelsApi(api_client)
    channel_id = 'channel_id_example' # str | Channel's id
    media = ['media_example'] # List[str] | Media URIs to play.
    lang = 'lang_example' # str | For sounds, selects language for sound. (optional)
    offsetms = 56 # int | Number of milliseconds to skip before playing. Only applies to the first URI if multiple media URIs are specified. (optional)
    skipms = 3000 # int | Number of milliseconds to skip for forward/reverse operations. (optional) (default to 3000)
    playback_id = 'playback_id_example' # str | Playback ID. (optional)

    try:
        # Start playback of media.
        api_response = await api_instance.playsound(channel_id, media, lang=lang, offsetms=offsetms, skipms=skipms, playback_id=playback_id)
        print("The response of ChannelsApi->playsound:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ChannelsApi->playsound: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channel_id** | **str**| Channel&#39;s id | 
 **media** | [**List[str]**](str.md)| Media URIs to play. | 
 **lang** | **str**| For sounds, selects language for sound. | [optional] 
 **offsetms** | **int**| Number of milliseconds to skip before playing. Only applies to the first URI if multiple media URIs are specified. | [optional] 
 **skipms** | **int**| Number of milliseconds to skip for forward/reverse operations. | [optional] [default to 3000]
 **playback_id** | **str**| Playback ID. | [optional] 

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

# **recordchannel**
> LiveRecording recordchannel(channel_id, name, format, max_duration_seconds=max_duration_seconds, max_silence_seconds=max_silence_seconds, if_exists=if_exists, beep=beep, terminate_on=terminate_on)

Start a recording.

Record audio from a channel. Note that this will not capture audio sent to the channel. The bridge itself has a record feature if that's what you want.

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
    api_instance = ari_sync_sdk.ChannelsApi(api_client)
    channel_id = 'channel_id_example' # str | Channel's id
    name = 'name_example' # str | Recording's filename
    format = 'format_example' # str | Format to encode audio in
    max_duration_seconds = 0 # int | Maximum duration of the recording, in seconds. 0 for no limit (optional) (default to 0)
    max_silence_seconds = 0 # int | Maximum duration of silence, in seconds. 0 for no limit (optional) (default to 0)
    if_exists = 'fail' # str | Action to take if a recording with the same name already exists. (optional) (default to 'fail')
    beep = False # bool | Play beep when recording begins (optional) (default to False)
    terminate_on = 'none' # str | DTMF input to terminate recording (optional) (default to 'none')

    try:
        # Start a recording.
        api_response = await api_instance.recordchannel(channel_id, name, format, max_duration_seconds=max_duration_seconds, max_silence_seconds=max_silence_seconds, if_exists=if_exists, beep=beep, terminate_on=terminate_on)
        print("The response of ChannelsApi->recordchannel:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ChannelsApi->recordchannel: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channel_id** | **str**| Channel&#39;s id | 
 **name** | **str**| Recording&#39;s filename | 
 **format** | **str**| Format to encode audio in | 
 **max_duration_seconds** | **int**| Maximum duration of the recording, in seconds. 0 for no limit | [optional] [default to 0]
 **max_silence_seconds** | **int**| Maximum duration of silence, in seconds. 0 for no limit | [optional] [default to 0]
 **if_exists** | **str**| Action to take if a recording with the same name already exists. | [optional] [default to &#39;fail&#39;]
 **beep** | **bool**| Play beep when recording begins | [optional] [default to False]
 **terminate_on** | **str**| DTMF input to terminate recording | [optional] [default to &#39;none&#39;]

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

# **redirect**
> redirect(channel_id, endpoint)

Redirect the channel to a different location.

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
    api_instance = ari_sync_sdk.ChannelsApi(api_client)
    channel_id = 'channel_id_example' # str | Channel's id
    endpoint = 'endpoint_example' # str | The endpoint to redirect the channel to

    try:
        # Redirect the channel to a different location.
        await api_instance.redirect(channel_id, endpoint)
    except Exception as e:
        print("Exception when calling ChannelsApi->redirect: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channel_id** | **str**| Channel&#39;s id | 
 **endpoint** | **str**| The endpoint to redirect the channel to | 

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

# **ring**
> ring(channel_id)

Indicate ringing to a channel.

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
    api_instance = ari_sync_sdk.ChannelsApi(api_client)
    channel_id = 'channel_id_example' # str | Channel's id

    try:
        # Indicate ringing to a channel.
        await api_instance.ring(channel_id)
    except Exception as e:
        print("Exception when calling ChannelsApi->ring: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
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

# **ring_stop**
> ring_stop(channel_id)

Stop ringing indication on a channel if locally generated.

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
    api_instance = ari_sync_sdk.ChannelsApi(api_client)
    channel_id = 'channel_id_example' # str | Channel's id

    try:
        # Stop ringing indication on a channel if locally generated.
        await api_instance.ring_stop(channel_id)
    except Exception as e:
        print("Exception when calling ChannelsApi->ring_stop: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
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

# **rtpstatistics**
> RTPstat rtpstatistics(channel_id)

RTP stats on a channel.

### Example

```python
import time
import os
import ari_sync_sdk
from ari_sync_sdk.models.rt_pstat import RTPstat
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
    api_instance = ari_sync_sdk.ChannelsApi(api_client)
    channel_id = 'channel_id_example' # str | Channel's id

    try:
        # RTP stats on a channel.
        api_response = await api_instance.rtpstatistics(channel_id)
        print("The response of ChannelsApi->rtpstatistics:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ChannelsApi->rtpstatistics: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channel_id** | **str**| Channel&#39;s id | 

### Return type

[**RTPstat**](RTPstat.md)

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

# **send_dtmf**
> send_dtmf(channel_id, dtmf=dtmf, before=before, between=between, duration=duration, after=after)

Send provided DTMF to a given channel.

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
    api_instance = ari_sync_sdk.ChannelsApi(api_client)
    channel_id = 'channel_id_example' # str | Channel's id
    dtmf = 'dtmf_example' # str | DTMF To send. (optional)
    before = 0 # int | Amount of time to wait before DTMF digits (specified in milliseconds) start. (optional) (default to 0)
    between = 100 # int | Amount of time in between DTMF digits (specified in milliseconds). (optional) (default to 100)
    duration = 100 # int | Length of each DTMF digit (specified in milliseconds). (optional) (default to 100)
    after = 0 # int | Amount of time to wait after DTMF digits (specified in milliseconds) end. (optional) (default to 0)

    try:
        # Send provided DTMF to a given channel.
        await api_instance.send_dtmf(channel_id, dtmf=dtmf, before=before, between=between, duration=duration, after=after)
    except Exception as e:
        print("Exception when calling ChannelsApi->send_dtmf: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channel_id** | **str**| Channel&#39;s id | 
 **dtmf** | **str**| DTMF To send. | [optional] 
 **before** | **int**| Amount of time to wait before DTMF digits (specified in milliseconds) start. | [optional] [default to 0]
 **between** | **int**| Amount of time in between DTMF digits (specified in milliseconds). | [optional] [default to 100]
 **duration** | **int**| Length of each DTMF digit (specified in milliseconds). | [optional] [default to 100]
 **after** | **int**| Amount of time to wait after DTMF digits (specified in milliseconds) end. | [optional] [default to 0]

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

# **set_channel_var**
> set_channel_var(channel_id, variable, value=value)

Set the value of a channel variable or function.

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
    api_instance = ari_sync_sdk.ChannelsApi(api_client)
    channel_id = 'channel_id_example' # str | Channel's id
    variable = 'variable_example' # str | The channel variable or function to set
    value = 'value_example' # str | The value to set the variable to (optional)

    try:
        # Set the value of a channel variable or function.
        await api_instance.set_channel_var(channel_id, variable, value=value)
    except Exception as e:
        print("Exception when calling ChannelsApi->set_channel_var: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channel_id** | **str**| Channel&#39;s id | 
 **variable** | **str**| The channel variable or function to set | 
 **value** | **str**| The value to set the variable to | [optional] 

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

# **snoop_channel**
> Channel snoop_channel(channel_id, app, spy=spy, whisper=whisper, app_args=app_args, snoop_id=snoop_id)

Start snooping.

Snoop (spy/whisper) on a specific channel.

### Example

```python
import time
import os
import ari_sync_sdk
from ari_sync_sdk.models.channel import Channel
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
    api_instance = ari_sync_sdk.ChannelsApi(api_client)
    channel_id = 'channel_id_example' # str | Channel's id
    app = 'app_example' # str | Application the snooping channel is placed into
    spy = 'none' # str | Direction of audio to spy on (optional) (default to 'none')
    whisper = 'none' # str | Direction of audio to whisper into (optional) (default to 'none')
    app_args = 'app_args_example' # str | The application arguments to pass to the Stasis application (optional)
    snoop_id = 'snoop_id_example' # str | Unique ID to assign to snooping channel (optional)

    try:
        # Start snooping.
        api_response = await api_instance.snoop_channel(channel_id, app, spy=spy, whisper=whisper, app_args=app_args, snoop_id=snoop_id)
        print("The response of ChannelsApi->snoop_channel:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ChannelsApi->snoop_channel: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channel_id** | **str**| Channel&#39;s id | 
 **app** | **str**| Application the snooping channel is placed into | 
 **spy** | **str**| Direction of audio to spy on | [optional] [default to &#39;none&#39;]
 **whisper** | **str**| Direction of audio to whisper into | [optional] [default to &#39;none&#39;]
 **app_args** | **str**| The application arguments to pass to the Stasis application | [optional] 
 **snoop_id** | **str**| Unique ID to assign to snooping channel | [optional] 

### Return type

[**Channel**](Channel.md)

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

# **snoop_channel_with_id**
> Channel snoop_channel_with_id(channel_id, snoop_id, app, spy=spy, whisper=whisper, app_args=app_args)

Start snooping.

Snoop (spy/whisper) on a specific channel.

### Example

```python
import time
import os
import ari_sync_sdk
from ari_sync_sdk.models.channel import Channel
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
    api_instance = ari_sync_sdk.ChannelsApi(api_client)
    channel_id = 'channel_id_example' # str | Channel's id
    snoop_id = 'snoop_id_example' # str | Unique ID to assign to snooping channel
    app = 'app_example' # str | Application the snooping channel is placed into
    spy = 'none' # str | Direction of audio to spy on (optional) (default to 'none')
    whisper = 'none' # str | Direction of audio to whisper into (optional) (default to 'none')
    app_args = 'app_args_example' # str | The application arguments to pass to the Stasis application (optional)

    try:
        # Start snooping.
        api_response = await api_instance.snoop_channel_with_id(channel_id, snoop_id, app, spy=spy, whisper=whisper, app_args=app_args)
        print("The response of ChannelsApi->snoop_channel_with_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ChannelsApi->snoop_channel_with_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channel_id** | **str**| Channel&#39;s id | 
 **snoop_id** | **str**| Unique ID to assign to snooping channel | 
 **app** | **str**| Application the snooping channel is placed into | 
 **spy** | **str**| Direction of audio to spy on | [optional] [default to &#39;none&#39;]
 **whisper** | **str**| Direction of audio to whisper into | [optional] [default to &#39;none&#39;]
 **app_args** | **str**| The application arguments to pass to the Stasis application | [optional] 

### Return type

[**Channel**](Channel.md)

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

# **start_silence**
> start_silence(channel_id)

Play silence to a channel.

Using media operations such as /play on a channel playing silence in this manner will suspend silence without resuming automatically.

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
    api_instance = ari_sync_sdk.ChannelsApi(api_client)
    channel_id = 'channel_id_example' # str | Channel's id

    try:
        # Play silence to a channel.
        await api_instance.start_silence(channel_id)
    except Exception as e:
        print("Exception when calling ChannelsApi->start_silence: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
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

# **stop_silence**
> stop_silence(channel_id)

Stop playing silence to a channel.

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
    api_instance = ari_sync_sdk.ChannelsApi(api_client)
    channel_id = 'channel_id_example' # str | Channel's id

    try:
        # Stop playing silence to a channel.
        await api_instance.stop_silence(channel_id)
    except Exception as e:
        print("Exception when calling ChannelsApi->stop_silence: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
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

# **unhold**
> unhold(channel_id)

Remove a channel from hold.

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
    api_instance = ari_sync_sdk.ChannelsApi(api_client)
    channel_id = 'channel_id_example' # str | Channel's id

    try:
        # Remove a channel from hold.
        await api_instance.unhold(channel_id)
    except Exception as e:
        print("Exception when calling ChannelsApi->unhold: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
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

# **unmute**
> unmute(channel_id, direction=direction)

Unmute a channel.

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
    api_instance = ari_sync_sdk.ChannelsApi(api_client)
    channel_id = 'channel_id_example' # str | Channel's id
    direction = 'both' # str | Direction in which to unmute audio (optional) (default to 'both')

    try:
        # Unmute a channel.
        await api_instance.unmute(channel_id, direction=direction)
    except Exception as e:
        print("Exception when calling ChannelsApi->unmute: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channel_id** | **str**| Channel&#39;s id | 
 **direction** | **str**| Direction in which to unmute audio | [optional] [default to &#39;both&#39;]

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

