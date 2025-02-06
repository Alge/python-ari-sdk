# ChannelDtmfReceived


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**channel** | [**Channel**](Channel.md) |  | 
**digit** | **str** | DTMF digit received (0-9, A-E, # or *) | 
**duration_ms** | **int** | Number of milliseconds DTMF was received | 

## Example

```python
from ari_sync_sdk.models.channel_dtmf_received import ChannelDtmfReceived

# TODO update the JSON string below
json = "{}"
# create an instance of ChannelDtmfReceived from a JSON string
channel_dtmf_received_instance = ChannelDtmfReceived.from_json(json)
# print the JSON string representation of the object
print(ChannelDtmfReceived.to_json())

# convert the object into a dict
channel_dtmf_received_dict = channel_dtmf_received_instance.to_dict()
# create an instance of ChannelDtmfReceived from a dict
channel_dtmf_received_from_dict = ChannelDtmfReceived.from_dict(channel_dtmf_received_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


