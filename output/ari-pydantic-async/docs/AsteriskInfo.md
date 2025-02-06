# AsteriskInfo

Asterisk system information

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**build** | [**BuildInfo**](BuildInfo.md) |  | [optional] 
**config** | [**ConfigInfo**](ConfigInfo.md) |  | [optional] 
**status** | [**StatusInfo**](StatusInfo.md) |  | [optional] 
**system** | [**SystemInfo**](SystemInfo.md) |  | [optional] 

## Example

```python
from ari_async_sdk.models.asterisk_info import AsteriskInfo

# TODO update the JSON string below
json = "{}"
# create an instance of AsteriskInfo from a JSON string
asterisk_info_instance = AsteriskInfo.from_json(json)
# print the JSON string representation of the object
print AsteriskInfo.to_json()

# convert the object into a dict
asterisk_info_dict = asterisk_info_instance.to_dict()
# create an instance of AsteriskInfo from a dict
asterisk_info_from_dict = AsteriskInfo.from_dict(asterisk_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


