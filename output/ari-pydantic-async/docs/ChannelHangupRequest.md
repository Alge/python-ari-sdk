# ChannelHangupRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cause** | **int** | Integer representation of the cause of the hangup. | [optional] 
**channel** | [**Channel**](Channel.md) |  | 
**soft** | **bool** | Whether the hangup request was a soft hangup request. | [optional] 

## Example

```python
from ari_async_sdk.models.channel_hangup_request import ChannelHangupRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ChannelHangupRequest from a JSON string
channel_hangup_request_instance = ChannelHangupRequest.from_json(json)
# print the JSON string representation of the object
print ChannelHangupRequest.to_json()

# convert the object into a dict
channel_hangup_request_dict = channel_hangup_request_instance.to_dict()
# create an instance of ChannelHangupRequest from a dict
channel_hangup_request_from_dict = ChannelHangupRequest.from_dict(channel_hangup_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


