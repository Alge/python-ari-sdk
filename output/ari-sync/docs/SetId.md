# SetId

Effective user/group id

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**group** | **str** | Effective group id. | 
**user** | **str** | Effective user id. | 

## Example

```python
from ari_sync_sdk.models.set_id import SetId

# TODO update the JSON string below
json = "{}"
# create an instance of SetId from a JSON string
set_id_instance = SetId.from_json(json)
# print the JSON string representation of the object
print(SetId.to_json())

# convert the object into a dict
set_id_dict = set_id_instance.to_dict()
# create an instance of SetId from a dict
set_id_from_dict = SetId.from_dict(set_id_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


