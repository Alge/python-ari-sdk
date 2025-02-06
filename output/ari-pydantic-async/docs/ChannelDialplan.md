# ChannelDialplan


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**channel** | [**Channel**](Channel.md) |  | 
**dialplan_app** | **str** | The application about to be executed. | 
**dialplan_app_data** | **str** | The data to be passed to the application. | 

## Example

```python
from ari_sync_sdk.models.channel_dialplan import ChannelDialplan

# TODO update the JSON string below
json = "{}"
# create an instance of ChannelDialplan from a JSON string
channel_dialplan_instance = ChannelDialplan.from_json(json)
# print the JSON string representation of the object
print ChannelDialplan.to_json()

# convert the object into a dict
channel_dialplan_dict = channel_dialplan_instance.to_dict()
# create an instance of ChannelDialplan from a dict
channel_dialplan_from_dict = ChannelDialplan.from_dict(channel_dialplan_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


