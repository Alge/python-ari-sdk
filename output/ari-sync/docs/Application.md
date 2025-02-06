# Application

Details of a Stasis application

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bridge_ids** | **List[str]** | Id&#39;s for bridges subscribed to. | 
**channel_ids** | **List[str]** | Id&#39;s for channels subscribed to. | 
**device_names** | **List[str]** | Names of the devices subscribed to. | 
**endpoint_ids** | **List[str]** | {tech}/{resource} for endpoints subscribed to. | 
**events_allowed** | **List[object]** | Event types sent to the application. | 
**events_disallowed** | **List[object]** | Event types not sent to the application. | 
**name** | **str** | Name of this application | 

## Example

```python
from ari_sync_sdk.models.application import Application

# TODO update the JSON string below
json = "{}"
# create an instance of Application from a JSON string
application_instance = Application.from_json(json)
# print the JSON string representation of the object
print(Application.to_json())

# convert the object into a dict
application_dict = application_instance.to_dict()
# create an instance of Application from a dict
application_from_dict = Application.from_dict(application_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


