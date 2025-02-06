# AsteriskPing

Asterisk ping information

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**asterisk_id** | **str** | Asterisk id info | 
**ping** | **str** | Always string value is pong | 
**timestamp** | **str** | The timestamp string of request received time | 

## Example

```python
from ari_sync_sdk.models.asterisk_ping import AsteriskPing

# TODO update the JSON string below
json = "{}"
# create an instance of AsteriskPing from a JSON string
asterisk_ping_instance = AsteriskPing.from_json(json)
# print the JSON string representation of the object
print(AsteriskPing.to_json())

# convert the object into a dict
asterisk_ping_dict = asterisk_ping_instance.to_dict()
# create an instance of AsteriskPing from a dict
asterisk_ping_from_dict = AsteriskPing.from_dict(asterisk_ping_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


