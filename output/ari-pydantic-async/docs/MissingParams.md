# MissingParams


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**params** | **List[str]** | A list of the missing parameters | 

## Example

```python
from ari_async_sdk.models.missing_params import MissingParams

# TODO update the JSON string below
json = "{}"
# create an instance of MissingParams from a JSON string
missing_params_instance = MissingParams.from_json(json)
# print the JSON string representation of the object
print MissingParams.to_json()

# convert the object into a dict
missing_params_dict = missing_params_instance.to_dict()
# create an instance of MissingParams from a dict
missing_params_from_dict = MissingParams.from_dict(missing_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


