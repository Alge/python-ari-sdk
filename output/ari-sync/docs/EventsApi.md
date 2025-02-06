# ari_sync_sdk.EventsApi

All URIs are relative to *http://localhost:8088/ari*

Method | HTTP request | Description
------------- | ------------- | -------------
[**event_websocket**](EventsApi.md#event_websocket) | **GET** /events | WebSocket connection for events.
[**user_event**](EventsApi.md#user_event) | **POST** /events/user/{eventName} | Generate a user event.


# **event_websocket**
> Message event_websocket(app, subscribe_all=subscribe_all)

WebSocket connection for events.

### Example


```python
import ari_sync_sdk
from ari_sync_sdk.models.message import Message
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
    api_instance = ari_sync_sdk.EventsApi(api_client)
    app = ['app_example'] # List[str] | Applications to subscribe to.
    subscribe_all = True # bool | Subscribe to all Asterisk events. If provided, the applications listed will be subscribed to all events, effectively disabling the application specific subscriptions. Default is 'false'. (optional)

    try:
        # WebSocket connection for events.
        api_response = api_instance.event_websocket(app, subscribe_all=subscribe_all)
        print("The response of EventsApi->event_websocket:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EventsApi->event_websocket: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app** | [**List[str]**](str.md)| Applications to subscribe to. | 
 **subscribe_all** | **bool**| Subscribe to all Asterisk events. If provided, the applications listed will be subscribed to all events, effectively disabling the application specific subscriptions. Default is &#39;false&#39;. | [optional] 

### Return type

[**Message**](Message.md)

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

# **user_event**
> user_event(event_name, application, source=source, variables=variables)

Generate a user event.

### Example


```python
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
    api_instance = ari_sync_sdk.EventsApi(api_client)
    event_name = 'event_name_example' # str | Event name
    application = 'application_example' # str | The name of the application that will receive this event
    source = ['source_example'] # List[str] | URI for event source (channel:{channelId}, bridge:{bridgeId}, endpoint:{tech}/{resource}, deviceState:{deviceName} (optional)
    variables = None # object | The \"variables\" key in the body object holds custom key/value pairs to add to the user event. Ex. { \"variables\": { \"key\": \"value\" } } (optional)

    try:
        # Generate a user event.
        api_instance.user_event(event_name, application, source=source, variables=variables)
    except Exception as e:
        print("Exception when calling EventsApi->user_event: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **event_name** | **str**| Event name | 
 **application** | **str**| The name of the application that will receive this event | 
 **source** | [**List[str]**](str.md)| URI for event source (channel:{channelId}, bridge:{bridgeId}, endpoint:{tech}/{resource}, deviceState:{deviceName} | [optional] 
 **variables** | **object**| The \&quot;variables\&quot; key in the body object holds custom key/value pairs to add to the user event. Ex. { \&quot;variables\&quot;: { \&quot;key\&quot;: \&quot;value\&quot; } } | [optional] 

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

