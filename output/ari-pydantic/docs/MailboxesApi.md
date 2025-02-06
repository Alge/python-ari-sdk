# ari_sync_sdk.MailboxesApi

All URIs are relative to *http://localhost:8088/ari*

Method | HTTP request | Description
------------- | ------------- | -------------
[**deletemailbox**](MailboxesApi.md#deletemailbox) | **DELETE** /mailboxes/{mailboxName} | Destroy a mailbox.
[**getmailbox**](MailboxesApi.md#getmailbox) | **GET** /mailboxes/{mailboxName} | Retrieve the current state of a mailbox.
[**listmailboxes**](MailboxesApi.md#listmailboxes) | **GET** /mailboxes | List all mailboxes.
[**updatemailbox**](MailboxesApi.md#updatemailbox) | **PUT** /mailboxes/{mailboxName} | Change the state of a mailbox. (Note - implicitly creates the mailbox).


# **deletemailbox**
> deletemailbox(mailbox_name)

Destroy a mailbox.

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
    api_instance = ari_sync_sdk.MailboxesApi(api_client)
    mailbox_name = 'mailbox_name_example' # str | Name of the mailbox

    try:
        # Destroy a mailbox.
        api_instance.deletemailbox(mailbox_name)
    except Exception as e:
        print("Exception when calling MailboxesApi->deletemailbox: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mailbox_name** | **str**| Name of the mailbox | 

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

# **getmailbox**
> Mailbox getmailbox(mailbox_name)

Retrieve the current state of a mailbox.

### Example

```python
import time
import os
import ari_sync_sdk
from ari_sync_sdk.models.mailbox import Mailbox
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
    api_instance = ari_sync_sdk.MailboxesApi(api_client)
    mailbox_name = 'mailbox_name_example' # str | Name of the mailbox

    try:
        # Retrieve the current state of a mailbox.
        api_response = api_instance.getmailbox(mailbox_name)
        print("The response of MailboxesApi->getmailbox:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MailboxesApi->getmailbox: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mailbox_name** | **str**| Name of the mailbox | 

### Return type

[**Mailbox**](Mailbox.md)

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

# **listmailboxes**
> List[Mailbox] listmailboxes()

List all mailboxes.

### Example

```python
import time
import os
import ari_sync_sdk
from ari_sync_sdk.models.mailbox import Mailbox
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
    api_instance = ari_sync_sdk.MailboxesApi(api_client)

    try:
        # List all mailboxes.
        api_response = api_instance.listmailboxes()
        print("The response of MailboxesApi->listmailboxes:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MailboxesApi->listmailboxes: %s\n" % e)
```



### Parameters
This endpoint does not need any parameter.

### Return type

[**List[Mailbox]**](Mailbox.md)

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

# **updatemailbox**
> updatemailbox(mailbox_name, old_messages, new_messages)

Change the state of a mailbox. (Note - implicitly creates the mailbox).

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
    api_instance = ari_sync_sdk.MailboxesApi(api_client)
    mailbox_name = 'mailbox_name_example' # str | Name of the mailbox
    old_messages = 56 # int | Count of old messages in the mailbox
    new_messages = 56 # int | Count of new messages in the mailbox

    try:
        # Change the state of a mailbox. (Note - implicitly creates the mailbox).
        api_instance.updatemailbox(mailbox_name, old_messages, new_messages)
    except Exception as e:
        print("Exception when calling MailboxesApi->updatemailbox: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mailbox_name** | **str**| Name of the mailbox | 
 **old_messages** | **int**| Count of old messages in the mailbox | 
 **new_messages** | **int**| Count of new messages in the mailbox | 

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

