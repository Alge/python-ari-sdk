# ChannelLeftBridge


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bridge** | [**Bridge**](Bridge.md) |  | 
**channel** | [**Channel**](Channel.md) |  | 

## Example

```python
from ari_async_sdk.models.channel_left_bridge import ChannelLeftBridge

# TODO update the JSON string below
json = "{}"
# create an instance of ChannelLeftBridge from a JSON string
channel_left_bridge_instance = ChannelLeftBridge.from_json(json)
# print the JSON string representation of the object
print ChannelLeftBridge.to_json()

# convert the object into a dict
channel_left_bridge_dict = channel_left_bridge_instance.to_dict()
# create an instance of ChannelLeftBridge from a dict
channel_left_bridge_from_dict = ChannelLeftBridge.from_dict(channel_left_bridge_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


