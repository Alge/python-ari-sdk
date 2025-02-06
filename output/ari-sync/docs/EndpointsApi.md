# ari_sync_sdk.EndpointsApi

All URIs are relative to *http://localhost:8088/ari*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getendpoint**](EndpointsApi.md#getendpoint) | **GET** /endpoints/{tech}/{resource} | Details for an endpoint.
[**list_by_tech**](EndpointsApi.md#list_by_tech) | **GET** /endpoints/{tech} | List available endoints for a given endpoint technology.
[**listendpoints**](EndpointsApi.md#listendpoints) | **GET** /endpoints | List all endpoints.
[**send_message**](EndpointsApi.md#send_message) | **PUT** /endpoints/sendMessage | Send a message to some technology URI or endpoint.
[**send_message_to_endpoint**](EndpointsApi.md#send_message_to_endpoint) | **PUT** /endpoints/{tech}/{resource}/sendMessage | Send a message to some endpoint in a technology.


# **getendpoint**
> Endpoint getendpoint(tech, resource)

Details for an endpoint.

### Example


```python
import ari_sync_sdk
from ari_sync_sdk.models.endpoint import Endpoint
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
    api_instance = ari_sync_sdk.EndpointsApi(api_client)
    tech = 'tech_example' # str | Technology of the endpoint
    resource = 'resource_example' # str | ID of the endpoint

    try:
        # Details for an endpoint.
        api_response = api_instance.getendpoint(tech, resource)
        print("The response of EndpointsApi->getendpoint:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EndpointsApi->getendpoint: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tech** | **str**| Technology of the endpoint | 
 **resource** | **str**| ID of the endpoint | 

### Return type

[**Endpoint**](Endpoint.md)

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

# **list_by_tech**
> List[Endpoint] list_by_tech(tech)

List available endoints for a given endpoint technology.

### Example


```python
import ari_sync_sdk
from ari_sync_sdk.models.endpoint import Endpoint
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
    api_instance = ari_sync_sdk.EndpointsApi(api_client)
    tech = 'tech_example' # str | Technology of the endpoints (sip,iax2,...)

    try:
        # List available endoints for a given endpoint technology.
        api_response = api_instance.list_by_tech(tech)
        print("The response of EndpointsApi->list_by_tech:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EndpointsApi->list_by_tech: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tech** | **str**| Technology of the endpoints (sip,iax2,...) | 

### Return type

[**List[Endpoint]**](Endpoint.md)

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

# **listendpoints**
> List[Endpoint] listendpoints()

List all endpoints.

### Example


```python
import ari_sync_sdk
from ari_sync_sdk.models.endpoint import Endpoint
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
    api_instance = ari_sync_sdk.EndpointsApi(api_client)

    try:
        # List all endpoints.
        api_response = api_instance.listendpoints()
        print("The response of EndpointsApi->listendpoints:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EndpointsApi->listendpoints: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[Endpoint]**](Endpoint.md)

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

# **send_message**
> send_message(to, var_from, body=body, variables=variables)

Send a message to some technology URI or endpoint.

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
    api_instance = ari_sync_sdk.EndpointsApi(api_client)
    to = 'to_example' # str | The endpoint resource or technology specific URI to send the message to. Valid resources are sip, pjsip, and xmpp.
    var_from = 'var_from_example' # str | The endpoint resource or technology specific identity to send this message from. Valid resources are sip, pjsip, and xmpp.
    body = 'body_example' # str | The body of the message (optional)
    variables = None # object |  (optional)

    try:
        # Send a message to some technology URI or endpoint.
        api_instance.send_message(to, var_from, body=body, variables=variables)
    except Exception as e:
        print("Exception when calling EndpointsApi->send_message: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **to** | **str**| The endpoint resource or technology specific URI to send the message to. Valid resources are sip, pjsip, and xmpp. | 
 **var_from** | **str**| The endpoint resource or technology specific identity to send this message from. Valid resources are sip, pjsip, and xmpp. | 
 **body** | **str**| The body of the message | [optional] 
 **variables** | **object**|  | [optional] 

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

# **send_message_to_endpoint**
> send_message_to_endpoint(tech, resource, var_from, body=body, variables=variables)

Send a message to some endpoint in a technology.

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
    api_instance = ari_sync_sdk.EndpointsApi(api_client)
    tech = 'tech_example' # str | Technology of the endpoint
    resource = 'resource_example' # str | ID of the endpoint
    var_from = 'var_from_example' # str | The endpoint resource or technology specific identity to send this message from. Valid resources are sip, pjsip, and xmpp.
    body = 'body_example' # str | The body of the message (optional)
    variables = None # object |  (optional)

    try:
        # Send a message to some endpoint in a technology.
        api_instance.send_message_to_endpoint(tech, resource, var_from, body=body, variables=variables)
    except Exception as e:
        print("Exception when calling EndpointsApi->send_message_to_endpoint: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tech** | **str**| Technology of the endpoint | 
 **resource** | **str**| ID of the endpoint | 
 **var_from** | **str**| The endpoint resource or technology specific identity to send this message from. Valid resources are sip, pjsip, and xmpp. | 
 **body** | **str**| The body of the message | [optional] 
 **variables** | **object**|  | [optional] 

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

