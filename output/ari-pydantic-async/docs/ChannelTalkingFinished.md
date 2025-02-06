# ChannelTalkingFinished


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**channel** | [**Channel**](Channel.md) |  | 
**duration** | **int** | The length of time, in milliseconds, that talking was detected on the channel | 

## Example

```python
from ari_async_sdk.models.channel_talking_finished import ChannelTalkingFinished

# TODO update the JSON string below
json = "{}"
# create an instance of ChannelTalkingFinished from a JSON string
channel_talking_finished_instance = ChannelTalkingFinished.from_json(json)
# print the JSON string representation of the object
print ChannelTalkingFinished.to_json()

# convert the object into a dict
channel_talking_finished_dict = channel_talking_finished_instance.to_dict()
# create an instance of ChannelTalkingFinished from a dict
channel_talking_finished_from_dict = ChannelTalkingFinished.from_dict(channel_talking_finished_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


