# Dial


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**caller** | [**Channel**](Channel.md) |  | [optional] 
**dialstatus** | **str** | Current status of the dialing attempt to the peer. | 
**dialstring** | **str** | The dial string for calling the peer channel. | [optional] 
**forward** | **str** | Forwarding target requested by the original dialed channel. | [optional] 
**forwarded** | [**Channel**](Channel.md) |  | [optional] 
**peer** | [**Channel**](Channel.md) |  | 

## Example

```python
from ari_async_sdk.models.dial import Dial

# TODO update the JSON string below
json = "{}"
# create an instance of Dial from a JSON string
dial_instance = Dial.from_json(json)
# print the JSON string representation of the object
print Dial.to_json()

# convert the object into a dict
dial_dict = dial_instance.to_dict()
# create an instance of Dial from a dict
dial_from_dict = Dial.from_dict(dial_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


