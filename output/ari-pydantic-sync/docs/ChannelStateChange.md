# ChannelStateChange


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**channel** | [**Channel**](Channel.md) |  | 

## Example

```python
from ari_sync_sdk.models.channel_state_change import ChannelStateChange

# TODO update the JSON string below
json = "{}"
# create an instance of ChannelStateChange from a JSON string
channel_state_change_instance = ChannelStateChange.from_json(json)
# print the JSON string representation of the object
print ChannelStateChange.to_json()

# convert the object into a dict
channel_state_change_dict = channel_state_change_instance.to_dict()
# create an instance of ChannelStateChange from a dict
channel_state_change_from_dict = ChannelStateChange.from_dict(channel_state_change_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


