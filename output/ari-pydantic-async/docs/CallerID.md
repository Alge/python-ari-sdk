# CallerID

Caller identification

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**number** | **str** |  | 

## Example

```python
from ari_async_sdk.models.caller_id import CallerID

# TODO update the JSON string below
json = "{}"
# create an instance of CallerID from a JSON string
caller_id_instance = CallerID.from_json(json)
# print the JSON string representation of the object
print CallerID.to_json()

# convert the object into a dict
caller_id_dict = caller_id_instance.to_dict()
# create an instance of CallerID from a dict
caller_id_from_dict = CallerID.from_dict(caller_id_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


