# StasisStart


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**args** | **List[str]** | Arguments to the application | 
**channel** | [**Channel**](Channel.md) |  | 
**replace_channel** | [**Channel**](Channel.md) |  | [optional] 

## Example

```python
from ari_async_sdk.models.stasis_start import StasisStart

# TODO update the JSON string below
json = "{}"
# create an instance of StasisStart from a JSON string
stasis_start_instance = StasisStart.from_json(json)
# print the JSON string representation of the object
print StasisStart.to_json()

# convert the object into a dict
stasis_start_dict = stasis_start_instance.to_dict()
# create an instance of StasisStart from a dict
stasis_start_from_dict = StasisStart.from_dict(stasis_start_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


