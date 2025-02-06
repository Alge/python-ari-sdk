# ari_async_sdk.DeviceStatesApi

All URIs are relative to *http://localhost:8088/ari*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete**](DeviceStatesApi.md#delete) | **DELETE** /deviceStates/{deviceName} | Destroy a device-state controlled by ARI.
[**getdevicestate**](DeviceStatesApi.md#getdevicestate) | **GET** /deviceStates/{deviceName} | Retrieve the current state of a device.
[**list_device_states**](DeviceStatesApi.md#list_device_states) | **GET** /deviceStates | List all ARI controlled device states.
[**update**](DeviceStatesApi.md#update) | **PUT** /deviceStates/{deviceName} | Change the state of a device controlled by ARI. (Note - implicitly creates the device state).


# **delete**
> delete(device_name)

Destroy a device-state controlled by ARI.

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
    api_instance = ari_async_sdk.DeviceStatesApi(api_client)
    device_name = 'device_name_example' # str | Name of the device

    try:
        # Destroy a device-state controlled by ARI.
        await api_instance.delete(device_name)
    except Exception as e:
        print("Exception when calling DeviceStatesApi->delete: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_name** | **str**| Name of the device | 

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

# **getdevicestate**
> DeviceState getdevicestate(device_name)

Retrieve the current state of a device.

### Example

```python
import time
import os
import ari_async_sdk
from ari_async_sdk.models.device_state import DeviceState
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
    api_instance = ari_async_sdk.DeviceStatesApi(api_client)
    device_name = 'device_name_example' # str | Name of the device

    try:
        # Retrieve the current state of a device.
        api_response = await api_instance.getdevicestate(device_name)
        print("The response of DeviceStatesApi->getdevicestate:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DeviceStatesApi->getdevicestate: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_name** | **str**| Name of the device | 

### Return type

[**DeviceState**](DeviceState.md)

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

# **list_device_states**
> List[DeviceState] list_device_states()

List all ARI controlled device states.

### Example

```python
import time
import os
import ari_async_sdk
from ari_async_sdk.models.device_state import DeviceState
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
    api_instance = ari_async_sdk.DeviceStatesApi(api_client)

    try:
        # List all ARI controlled device states.
        api_response = await api_instance.list_device_states()
        print("The response of DeviceStatesApi->list_device_states:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DeviceStatesApi->list_device_states: %s\n" % e)
```



### Parameters
This endpoint does not need any parameter.

### Return type

[**List[DeviceState]**](DeviceState.md)

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

# **update**
> update(device_name, device_state)

Change the state of a device controlled by ARI. (Note - implicitly creates the device state).

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
    api_instance = ari_async_sdk.DeviceStatesApi(api_client)
    device_name = 'device_name_example' # str | Name of the device
    device_state = 'device_state_example' # str | Device state value

    try:
        # Change the state of a device controlled by ARI. (Note - implicitly creates the device state).
        await api_instance.update(device_name, device_state)
    except Exception as e:
        print("Exception when calling DeviceStatesApi->update: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_name** | **str**| Name of the device | 
 **device_state** | **str**| Device state value | 

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

