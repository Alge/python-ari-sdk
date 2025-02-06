# ApplicationMoveFailed


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**args** | **List[str]** | Arguments to the application | 
**channel** | [**Channel**](Channel.md) |  | 
**destination** | **str** |  | 

## Example

```python
from ari_async_sdk.models.application_move_failed import ApplicationMoveFailed

# TODO update the JSON string below
json = "{}"
# create an instance of ApplicationMoveFailed from a JSON string
application_move_failed_instance = ApplicationMoveFailed.from_json(json)
# print the JSON string representation of the object
print ApplicationMoveFailed.to_json()

# convert the object into a dict
application_move_failed_dict = application_move_failed_instance.to_dict()
# create an instance of ApplicationMoveFailed from a dict
application_move_failed_from_dict = ApplicationMoveFailed.from_dict(application_move_failed_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


