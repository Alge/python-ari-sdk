# ari_async_sdk.ApplicationsApi

All URIs are relative to *http://localhost:8088/ari*

Method | HTTP request | Description
------------- | ------------- | -------------
[**filter**](ApplicationsApi.md#filter) | **PUT** /applications/{applicationName}/eventFilter | Filter application events types.
[**get**](ApplicationsApi.md#get) | **GET** /applications/{applicationName} | Get details of an application.
[**list**](ApplicationsApi.md#list) | **GET** /applications | List all applications.
[**subscribe**](ApplicationsApi.md#subscribe) | **POST** /applications/{applicationName}/subscription | Subscribe an application to a event source.
[**unsubscribe**](ApplicationsApi.md#unsubscribe) | **DELETE** /applications/{applicationName}/subscription | Unsubscribe an application from an event source.


# **filter**
> Application filter(application_name, filter=filter)

Filter application events types.

Allowed and/or disallowed event type filtering can be done. The body (parameter) should specify a JSON key/value object that describes the type of event filtering needed. One, or both of the following keys can be designated:<br /><br />\"allowed\" - Specifies an allowed list of event types<br />\"disallowed\" - Specifies a disallowed list of event types<br /><br />Further, each of those key's value should be a JSON array that holds zero, or more JSON key/value objects. Each of these objects must contain the following key with an associated value:<br /><br />\"type\" - The type name of the event to filter<br /><br />The value must be the string name (case sensitive) of the event type that needs filtering. For example:<br /><br />{ \"allowed\": [ { \"type\": \"StasisStart\" }, { \"type\": \"StasisEnd\" } ] }<br /><br />As this specifies only an allowed list, then only those two event type messages are sent to the application. No other event messages are sent.<br /><br />The following rules apply:<br /><br />* If the body is empty, both the allowed and disallowed filters are set empty.<br />* If both list types are given then both are set to their respective values (note, specifying an empty array for a given type sets that type to empty).<br />* If only one list type is given then only that type is set. The other type is not updated.<br />* An empty \"allowed\" list means all events are allowed.<br />* An empty \"disallowed\" list means no events are disallowed.<br />* Disallowed events take precedence over allowed events if the event type is specified in both lists.

### Example

```python
import time
import os
import ari_async_sdk
from ari_async_sdk.models.application import Application
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
    api_instance = ari_async_sdk.ApplicationsApi(api_client)
    application_name = 'application_name_example' # str | Application's name
    filter = None # object | Specify which event types to allow/disallow (optional)

    try:
        # Filter application events types.
        api_response = await api_instance.filter(application_name, filter=filter)
        print("The response of ApplicationsApi->filter:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApplicationsApi->filter: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application_name** | **str**| Application&#39;s name | 
 **filter** | **object**| Specify which event types to allow/disallow | [optional] 

### Return type

[**Application**](Application.md)

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

# **get**
> Application get(application_name)

Get details of an application.

### Example

```python
import time
import os
import ari_async_sdk
from ari_async_sdk.models.application import Application
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
    api_instance = ari_async_sdk.ApplicationsApi(api_client)
    application_name = 'application_name_example' # str | Application's name

    try:
        # Get details of an application.
        api_response = await api_instance.get(application_name)
        print("The response of ApplicationsApi->get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApplicationsApi->get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application_name** | **str**| Application&#39;s name | 

### Return type

[**Application**](Application.md)

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

# **list**
> List[Application] list()

List all applications.

### Example

```python
import time
import os
import ari_async_sdk
from ari_async_sdk.models.application import Application
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
    api_instance = ari_async_sdk.ApplicationsApi(api_client)

    try:
        # List all applications.
        api_response = await api_instance.list()
        print("The response of ApplicationsApi->list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApplicationsApi->list: %s\n" % e)
```



### Parameters
This endpoint does not need any parameter.

### Return type

[**List[Application]**](Application.md)

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

# **subscribe**
> Application subscribe(application_name, event_source)

Subscribe an application to a event source.

Returns the state of the application after the subscriptions have changed

### Example

```python
import time
import os
import ari_async_sdk
from ari_async_sdk.models.application import Application
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
    api_instance = ari_async_sdk.ApplicationsApi(api_client)
    application_name = 'application_name_example' # str | Application's name
    event_source = ['event_source_example'] # List[str] | URI for event source (channel:{channelId}, bridge:{bridgeId}, endpoint:{tech}[/{resource}], deviceState:{deviceName}

    try:
        # Subscribe an application to a event source.
        api_response = await api_instance.subscribe(application_name, event_source)
        print("The response of ApplicationsApi->subscribe:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApplicationsApi->subscribe: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application_name** | **str**| Application&#39;s name | 
 **event_source** | [**List[str]**](str.md)| URI for event source (channel:{channelId}, bridge:{bridgeId}, endpoint:{tech}[/{resource}], deviceState:{deviceName} | 

### Return type

[**Application**](Application.md)

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

# **unsubscribe**
> Application unsubscribe(application_name, event_source)

Unsubscribe an application from an event source.

Returns the state of the application after the subscriptions have changed

### Example

```python
import time
import os
import ari_async_sdk
from ari_async_sdk.models.application import Application
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
    api_instance = ari_async_sdk.ApplicationsApi(api_client)
    application_name = 'application_name_example' # str | Application's name
    event_source = ['event_source_example'] # List[str] | URI for event source (channel:{channelId}, bridge:{bridgeId}, endpoint:{tech}[/{resource}], deviceState:{deviceName}

    try:
        # Unsubscribe an application from an event source.
        api_response = await api_instance.unsubscribe(application_name, event_source)
        print("The response of ApplicationsApi->unsubscribe:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApplicationsApi->unsubscribe: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application_name** | **str**| Application&#39;s name | 
 **event_source** | [**List[str]**](str.md)| URI for event source (channel:{channelId}, bridge:{bridgeId}, endpoint:{tech}[/{resource}], deviceState:{deviceName} | 

### Return type

[**Application**](Application.md)

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

