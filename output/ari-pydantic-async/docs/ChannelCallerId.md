# ChannelCallerId


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**caller_presentation** | **int** | The integer representation of the Caller Presentation value. | 
**caller_presentation_txt** | **str** | The text representation of the Caller Presentation value. | 
**channel** | [**Channel**](Channel.md) |  | 

## Example

```python
from ari_sync_sdk.models.channel_caller_id import ChannelCallerId

# TODO update the JSON string below
json = "{}"
# create an instance of ChannelCallerId from a JSON string
channel_caller_id_instance = ChannelCallerId.from_json(json)
# print the JSON string representation of the object
print ChannelCallerId.to_json()

# convert the object into a dict
channel_caller_id_dict = channel_caller_id_instance.to_dict()
# create an instance of ChannelCallerId from a dict
channel_caller_id_from_dict = ChannelCallerId.from_dict(channel_caller_id_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


