# ari_async_sdk.AsteriskApi

All URIs are relative to *http://localhost:8088/ari*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_log**](AsteriskApi.md#add_log) | **POST** /asterisk/logging/{logChannelName} | Adds a log channel.
[**delete_log**](AsteriskApi.md#delete_log) | **DELETE** /asterisk/logging/{logChannelName} | Deletes a log channel.
[**delete_object**](AsteriskApi.md#delete_object) | **DELETE** /asterisk/config/dynamic/{configClass}/{objectType}/{id} | Delete a dynamic configuration object.
[**get_global_var**](AsteriskApi.md#get_global_var) | **GET** /asterisk/variable | Get the value of a global variable.
[**get_info**](AsteriskApi.md#get_info) | **GET** /asterisk/info | Gets Asterisk system information.
[**get_module**](AsteriskApi.md#get_module) | **GET** /asterisk/modules/{moduleName} | Get Asterisk module information.
[**get_object**](AsteriskApi.md#get_object) | **GET** /asterisk/config/dynamic/{configClass}/{objectType}/{id} | Retrieve a dynamic configuration object.
[**list_log_channels**](AsteriskApi.md#list_log_channels) | **GET** /asterisk/logging | Gets Asterisk log channel information.
[**list_modules**](AsteriskApi.md#list_modules) | **GET** /asterisk/modules | List Asterisk modules.
[**load_module**](AsteriskApi.md#load_module) | **POST** /asterisk/modules/{moduleName} | Load an Asterisk module.
[**ping**](AsteriskApi.md#ping) | **GET** /asterisk/ping | Response pong message.
[**reload_module**](AsteriskApi.md#reload_module) | **PUT** /asterisk/modules/{moduleName} | Reload an Asterisk module.
[**rotate_log**](AsteriskApi.md#rotate_log) | **PUT** /asterisk/logging/{logChannelName}/rotate | Rotates a log channel.
[**set_global_var**](AsteriskApi.md#set_global_var) | **POST** /asterisk/variable | Set the value of a global variable.
[**unload_module**](AsteriskApi.md#unload_module) | **DELETE** /asterisk/modules/{moduleName} | Unload an Asterisk module.
[**update_object**](AsteriskApi.md#update_object) | **PUT** /asterisk/config/dynamic/{configClass}/{objectType}/{id} | Create or update a dynamic configuration object.


# **add_log**
> add_log(log_channel_name, configuration)

Adds a log channel.

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
    api_instance = ari_async_sdk.AsteriskApi(api_client)
    log_channel_name = 'log_channel_name_example' # str | The log channel to add
    configuration = 'configuration_example' # str | levels of the log channel

    try:
        # Adds a log channel.
        await api_instance.add_log(log_channel_name, configuration)
    except Exception as e:
        print("Exception when calling AsteriskApi->add_log: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **log_channel_name** | **str**| The log channel to add | 
 **configuration** | **str**| levels of the log channel | 

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

# **delete_log**
> delete_log(log_channel_name)

Deletes a log channel.

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
    api_instance = ari_async_sdk.AsteriskApi(api_client)
    log_channel_name = 'log_channel_name_example' # str | Log channels name

    try:
        # Deletes a log channel.
        await api_instance.delete_log(log_channel_name)
    except Exception as e:
        print("Exception when calling AsteriskApi->delete_log: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **log_channel_name** | **str**| Log channels name | 

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

# **delete_object**
> delete_object(config_class, object_type, id)

Delete a dynamic configuration object.

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
    api_instance = ari_async_sdk.AsteriskApi(api_client)
    config_class = 'config_class_example' # str | The configuration class containing dynamic configuration objects.
    object_type = 'object_type_example' # str | The type of configuration object to delete.
    id = 'id_example' # str | The unique identifier of the object to delete.

    try:
        # Delete a dynamic configuration object.
        await api_instance.delete_object(config_class, object_type, id)
    except Exception as e:
        print("Exception when calling AsteriskApi->delete_object: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **config_class** | **str**| The configuration class containing dynamic configuration objects. | 
 **object_type** | **str**| The type of configuration object to delete. | 
 **id** | **str**| The unique identifier of the object to delete. | 

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

# **get_global_var**
> Variable get_global_var(variable)

Get the value of a global variable.

### Example

```python
import time
import os
import ari_async_sdk
from ari_async_sdk.models.variable import Variable
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
    api_instance = ari_async_sdk.AsteriskApi(api_client)
    variable = 'variable_example' # str | The variable to get

    try:
        # Get the value of a global variable.
        api_response = await api_instance.get_global_var(variable)
        print("The response of AsteriskApi->get_global_var:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AsteriskApi->get_global_var: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **variable** | **str**| The variable to get | 

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

# **get_info**
> AsteriskInfo get_info(only=only)

Gets Asterisk system information.

### Example

```python
import time
import os
import ari_async_sdk
from ari_async_sdk.models.asterisk_info import AsteriskInfo
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
    api_instance = ari_async_sdk.AsteriskApi(api_client)
    only = ['only_example'] # List[str] | Filter information returned (optional)

    try:
        # Gets Asterisk system information.
        api_response = await api_instance.get_info(only=only)
        print("The response of AsteriskApi->get_info:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AsteriskApi->get_info: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **only** | [**List[str]**](str.md)| Filter information returned | [optional] 

### Return type

[**AsteriskInfo**](AsteriskInfo.md)

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

# **get_module**
> Module get_module(module_name)

Get Asterisk module information.

### Example

```python
import time
import os
import ari_async_sdk
from ari_async_sdk.models.module import Module
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
    api_instance = ari_async_sdk.AsteriskApi(api_client)
    module_name = 'module_name_example' # str | Module's name

    try:
        # Get Asterisk module information.
        api_response = await api_instance.get_module(module_name)
        print("The response of AsteriskApi->get_module:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AsteriskApi->get_module: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **module_name** | **str**| Module&#39;s name | 

### Return type

[**Module**](Module.md)

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

# **get_object**
> List[ConfigTuple] get_object(config_class, object_type, id)

Retrieve a dynamic configuration object.

### Example

```python
import time
import os
import ari_async_sdk
from ari_async_sdk.models.config_tuple import ConfigTuple
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
    api_instance = ari_async_sdk.AsteriskApi(api_client)
    config_class = 'config_class_example' # str | The configuration class containing dynamic configuration objects.
    object_type = 'object_type_example' # str | The type of configuration object to retrieve.
    id = 'id_example' # str | The unique identifier of the object to retrieve.

    try:
        # Retrieve a dynamic configuration object.
        api_response = await api_instance.get_object(config_class, object_type, id)
        print("The response of AsteriskApi->get_object:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AsteriskApi->get_object: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **config_class** | **str**| The configuration class containing dynamic configuration objects. | 
 **object_type** | **str**| The type of configuration object to retrieve. | 
 **id** | **str**| The unique identifier of the object to retrieve. | 

### Return type

[**List[ConfigTuple]**](ConfigTuple.md)

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

# **list_log_channels**
> List[LogChannel] list_log_channels()

Gets Asterisk log channel information.

### Example

```python
import time
import os
import ari_async_sdk
from ari_async_sdk.models.log_channel import LogChannel
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
    api_instance = ari_async_sdk.AsteriskApi(api_client)

    try:
        # Gets Asterisk log channel information.
        api_response = await api_instance.list_log_channels()
        print("The response of AsteriskApi->list_log_channels:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AsteriskApi->list_log_channels: %s\n" % e)
```



### Parameters
This endpoint does not need any parameter.

### Return type

[**List[LogChannel]**](LogChannel.md)

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

# **list_modules**
> List[Module] list_modules()

List Asterisk modules.

### Example

```python
import time
import os
import ari_async_sdk
from ari_async_sdk.models.module import Module
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
    api_instance = ari_async_sdk.AsteriskApi(api_client)

    try:
        # List Asterisk modules.
        api_response = await api_instance.list_modules()
        print("The response of AsteriskApi->list_modules:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AsteriskApi->list_modules: %s\n" % e)
```



### Parameters
This endpoint does not need any parameter.

### Return type

[**List[Module]**](Module.md)

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

# **load_module**
> load_module(module_name)

Load an Asterisk module.

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
    api_instance = ari_async_sdk.AsteriskApi(api_client)
    module_name = 'module_name_example' # str | Module's name

    try:
        # Load an Asterisk module.
        await api_instance.load_module(module_name)
    except Exception as e:
        print("Exception when calling AsteriskApi->load_module: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **module_name** | **str**| Module&#39;s name | 

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

# **ping**
> AsteriskPing ping()

Response pong message.

### Example

```python
import time
import os
import ari_async_sdk
from ari_async_sdk.models.asterisk_ping import AsteriskPing
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
    api_instance = ari_async_sdk.AsteriskApi(api_client)

    try:
        # Response pong message.
        api_response = await api_instance.ping()
        print("The response of AsteriskApi->ping:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AsteriskApi->ping: %s\n" % e)
```



### Parameters
This endpoint does not need any parameter.

### Return type

[**AsteriskPing**](AsteriskPing.md)

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

# **reload_module**
> reload_module(module_name)

Reload an Asterisk module.

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
    api_instance = ari_async_sdk.AsteriskApi(api_client)
    module_name = 'module_name_example' # str | Module's name

    try:
        # Reload an Asterisk module.
        await api_instance.reload_module(module_name)
    except Exception as e:
        print("Exception when calling AsteriskApi->reload_module: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **module_name** | **str**| Module&#39;s name | 

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

# **rotate_log**
> rotate_log(log_channel_name)

Rotates a log channel.

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
    api_instance = ari_async_sdk.AsteriskApi(api_client)
    log_channel_name = 'log_channel_name_example' # str | Log channel's name

    try:
        # Rotates a log channel.
        await api_instance.rotate_log(log_channel_name)
    except Exception as e:
        print("Exception when calling AsteriskApi->rotate_log: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **log_channel_name** | **str**| Log channel&#39;s name | 

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

# **set_global_var**
> set_global_var(variable, value=value)

Set the value of a global variable.

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
    api_instance = ari_async_sdk.AsteriskApi(api_client)
    variable = 'variable_example' # str | The variable to set
    value = 'value_example' # str | The value to set the variable to (optional)

    try:
        # Set the value of a global variable.
        await api_instance.set_global_var(variable, value=value)
    except Exception as e:
        print("Exception when calling AsteriskApi->set_global_var: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **variable** | **str**| The variable to set | 
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

# **unload_module**
> unload_module(module_name)

Unload an Asterisk module.

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
    api_instance = ari_async_sdk.AsteriskApi(api_client)
    module_name = 'module_name_example' # str | Module's name

    try:
        # Unload an Asterisk module.
        await api_instance.unload_module(module_name)
    except Exception as e:
        print("Exception when calling AsteriskApi->unload_module: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **module_name** | **str**| Module&#39;s name | 

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

# **update_object**
> List[ConfigTuple] update_object(config_class, object_type, id, fields=fields)

Create or update a dynamic configuration object.

### Example

```python
import time
import os
import ari_async_sdk
from ari_async_sdk.models.config_tuple import ConfigTuple
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
    api_instance = ari_async_sdk.AsteriskApi(api_client)
    config_class = 'config_class_example' # str | The configuration class containing dynamic configuration objects.
    object_type = 'object_type_example' # str | The type of configuration object to create or update.
    id = 'id_example' # str | The unique identifier of the object to create or update.
    fields = None # object | The body object should have a value that is a list of ConfigTuples, which provide the fields to update. Ex. [ { \"attribute\": \"directmedia\", \"value\": \"false\" } ] (optional)

    try:
        # Create or update a dynamic configuration object.
        api_response = await api_instance.update_object(config_class, object_type, id, fields=fields)
        print("The response of AsteriskApi->update_object:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AsteriskApi->update_object: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **config_class** | **str**| The configuration class containing dynamic configuration objects. | 
 **object_type** | **str**| The type of configuration object to create or update. | 
 **id** | **str**| The unique identifier of the object to create or update. | 
 **fields** | **object**| The body object should have a value that is a list of ConfigTuples, which provide the fields to update. Ex. [ { \&quot;attribute\&quot;: \&quot;directmedia\&quot;, \&quot;value\&quot;: \&quot;false\&quot; } ] | [optional] 

### Return type

[**List[ConfigTuple]**](ConfigTuple.md)

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

