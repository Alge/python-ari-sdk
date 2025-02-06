# ChannelCreated


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**channel** | [**Channel**](Channel.md) |  | 

## Example

```python
from ari_async_sdk.models.channel_created import ChannelCreated

# TODO update the JSON string below
json = "{}"
# create an instance of ChannelCreated from a JSON string
channel_created_instance = ChannelCreated.from_json(json)
# print the JSON string representation of the object
print ChannelCreated.to_json()

# convert the object into a dict
channel_created_dict = channel_created_instance.to_dict()
# create an instance of ChannelCreated from a dict
channel_created_from_dict = ChannelCreated.from_dict(channel_created_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


