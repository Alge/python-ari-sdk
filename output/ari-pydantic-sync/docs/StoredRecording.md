# StoredRecording

A past recording that may be played back.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**format** | **str** |  | 
**name** | **str** |  | 

## Example

```python
from ari_sync_sdk.models.stored_recording import StoredRecording

# TODO update the JSON string below
json = "{}"
# create an instance of StoredRecording from a JSON string
stored_recording_instance = StoredRecording.from_json(json)
# print the JSON string representation of the object
print StoredRecording.to_json()

# convert the object into a dict
stored_recording_dict = stored_recording_instance.to_dict()
# create an instance of StoredRecording from a dict
stored_recording_from_dict = StoredRecording.from_dict(stored_recording_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


