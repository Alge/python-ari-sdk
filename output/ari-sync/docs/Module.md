# Module

Details of an Asterisk module

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** | The description of this module | 
**name** | **str** | The name of this module | 
**status** | **str** | The running status of this module | 
**support_level** | **str** | The support state of this module | 
**use_count** | **int** | The number of times this module is being used | 

## Example

```python
from ari_sync_sdk.models.module import Module

# TODO update the JSON string below
json = "{}"
# create an instance of Module from a JSON string
module_instance = Module.from_json(json)
# print the JSON string representation of the object
print(Module.to_json())

# convert the object into a dict
module_dict = module_instance.to_dict()
# create an instance of Module from a dict
module_from_dict = Module.from_dict(module_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


