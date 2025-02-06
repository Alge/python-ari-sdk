# ConfigTuple

A key/value pair that makes up part of a configuration object.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attribute** | **str** | A configuration object attribute. | 
**value** | **str** | The value for the attribute. | 

## Example

```python
from ari_sync_sdk.models.config_tuple import ConfigTuple

# TODO update the JSON string below
json = "{}"
# create an instance of ConfigTuple from a JSON string
config_tuple_instance = ConfigTuple.from_json(json)
# print the JSON string representation of the object
print ConfigTuple.to_json()

# convert the object into a dict
config_tuple_dict = config_tuple_instance.to_dict()
# create an instance of ConfigTuple from a dict
config_tuple_from_dict = ConfigTuple.from_dict(config_tuple_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


