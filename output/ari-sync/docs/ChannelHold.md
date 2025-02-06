# ChannelHold


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**channel** | [**Channel**](Channel.md) |  | 
**musicclass** | **str** | The music on hold class that the initiator requested. | [optional] 

## Example

```python
from ari_sync_sdk.models.channel_hold import ChannelHold

# TODO update the JSON string below
json = "{}"
# create an instance of ChannelHold from a JSON string
channel_hold_instance = ChannelHold.from_json(json)
# print the JSON string representation of the object
print(ChannelHold.to_json())

# convert the object into a dict
channel_hold_dict = channel_hold_instance.to_dict()
# create an instance of ChannelHold from a dict
channel_hold_from_dict = ChannelHold.from_dict(channel_hold_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


