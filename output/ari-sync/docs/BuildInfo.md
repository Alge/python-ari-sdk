# BuildInfo

Info about how Asterisk was built

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_date** | **str** | Date and time when Asterisk was built. | 
**kernel** | **str** | Kernel version Asterisk was built on. | 
**machine** | **str** | Machine architecture (x86_64, i686, ppc, etc.) | 
**options** | **str** | Compile time options, or empty string if default. | 
**os** | **str** | OS Asterisk was built on. | 
**user** | **str** | Username that build Asterisk | 

## Example

```python
from ari_sync_sdk.models.build_info import BuildInfo

# TODO update the JSON string below
json = "{}"
# create an instance of BuildInfo from a JSON string
build_info_instance = BuildInfo.from_json(json)
# print the JSON string representation of the object
print(BuildInfo.to_json())

# convert the object into a dict
build_info_dict = build_info_instance.to_dict()
# create an instance of BuildInfo from a dict
build_info_from_dict = BuildInfo.from_dict(build_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


