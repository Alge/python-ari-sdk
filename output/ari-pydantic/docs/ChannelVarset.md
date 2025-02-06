# ChannelVarset


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**channel** | [**Channel**](Channel.md) |  | [optional] 
**value** | **str** | The new value of the variable. | 
**variable** | **str** | The variable that changed. | 

## Example

```python
from ari_sync_sdk.models.channel_varset import ChannelVarset

# TODO update the JSON string below
json = "{}"
# create an instance of ChannelVarset from a JSON string
channel_varset_instance = ChannelVarset.from_json(json)
# print the JSON string representation of the object
print ChannelVarset.to_json()

# convert the object into a dict
channel_varset_dict = channel_varset_instance.to_dict()
# create an instance of ChannelVarset from a dict
channel_varset_from_dict = ChannelVarset.from_dict(channel_varset_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


