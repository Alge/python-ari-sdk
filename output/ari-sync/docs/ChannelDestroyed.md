# ChannelDestroyed


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cause** | **int** | Integer representation of the cause of the hangup | 
**cause_txt** | **str** | Text representation of the cause of the hangup | 
**channel** | [**Channel**](Channel.md) |  | 

## Example

```python
from ari_sync_sdk.models.channel_destroyed import ChannelDestroyed

# TODO update the JSON string below
json = "{}"
# create an instance of ChannelDestroyed from a JSON string
channel_destroyed_instance = ChannelDestroyed.from_json(json)
# print the JSON string representation of the object
print(ChannelDestroyed.to_json())

# convert the object into a dict
channel_destroyed_dict = channel_destroyed_instance.to_dict()
# create an instance of ChannelDestroyed from a dict
channel_destroyed_from_dict = ChannelDestroyed.from_dict(channel_destroyed_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


