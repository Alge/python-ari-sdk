# StatusInfo

Info about Asterisk status

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**last_reload_time** | **date** | Time when Asterisk was last reloaded. | 
**startup_time** | **date** | Time when Asterisk was started. | 

## Example

```python
from ari_sync_sdk.models.status_info import StatusInfo

# TODO update the JSON string below
json = "{}"
# create an instance of StatusInfo from a JSON string
status_info_instance = StatusInfo.from_json(json)
# print the JSON string representation of the object
print(StatusInfo.to_json())

# convert the object into a dict
status_info_dict = status_info_instance.to_dict()
# create an instance of StatusInfo from a dict
status_info_from_dict = StatusInfo.from_dict(status_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


