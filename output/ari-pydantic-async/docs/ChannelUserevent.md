# ChannelUserevent


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bridge** | [**Bridge**](Bridge.md) |  | [optional] 
**channel** | [**Channel**](Channel.md) |  | [optional] 
**endpoint** | [**Endpoint**](Endpoint.md) |  | [optional] 
**eventname** | **str** | The name of the user event. | 
**userevent** | **object** | Custom Userevent data | 

## Example

```python
from ari_async_sdk.models.channel_userevent import ChannelUserevent

# TODO update the JSON string below
json = "{}"
# create an instance of ChannelUserevent from a JSON string
channel_userevent_instance = ChannelUserevent.from_json(json)
# print the JSON string representation of the object
print ChannelUserevent.to_json()

# convert the object into a dict
channel_userevent_dict = channel_userevent_instance.to_dict()
# create an instance of ChannelUserevent from a dict
channel_userevent_from_dict = ChannelUserevent.from_dict(channel_userevent_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


