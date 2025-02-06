# Channel

A specific communication connection between Asterisk and an Endpoint.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accountcode** | **str** |  | 
**caller** | [**CallerID**](CallerID.md) |  | 
**channelvars** | **object** | Channel variables | [optional] 
**connected** | [**CallerID**](CallerID.md) |  | 
**creationtime** | **date** | Timestamp when channel was created | 
**dialplan** | [**DialplanCEP**](DialplanCEP.md) |  | 
**id** | **str** | Unique identifier of the channel.  This is the same as the Uniqueid field in AMI. | 
**language** | **str** | The default spoken language | 
**name** | **str** | Name of the channel (i.e. SIP/foo-0000a7e3) | 
**state** | **str** |  | 

## Example

```python
from ari_sync_sdk.models.channel import Channel

# TODO update the JSON string below
json = "{}"
# create an instance of Channel from a JSON string
channel_instance = Channel.from_json(json)
# print the JSON string representation of the object
print(Channel.to_json())

# convert the object into a dict
channel_dict = channel_instance.to_dict()
# create an instance of Channel from a dict
channel_from_dict = Channel.from_dict(channel_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


