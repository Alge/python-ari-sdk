# ChannelEnteredBridge


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bridge** | [**Bridge**](Bridge.md) |  | 
**channel** | [**Channel**](Channel.md) |  | [optional] 

## Example

```python
from ari_async_sdk.models.channel_entered_bridge import ChannelEnteredBridge

# TODO update the JSON string below
json = "{}"
# create an instance of ChannelEnteredBridge from a JSON string
channel_entered_bridge_instance = ChannelEnteredBridge.from_json(json)
# print the JSON string representation of the object
print ChannelEnteredBridge.to_json()

# convert the object into a dict
channel_entered_bridge_dict = channel_entered_bridge_instance.to_dict()
# create an instance of ChannelEnteredBridge from a dict
channel_entered_bridge_from_dict = ChannelEnteredBridge.from_dict(channel_entered_bridge_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


