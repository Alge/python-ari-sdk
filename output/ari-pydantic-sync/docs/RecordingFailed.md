# RecordingFailed


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**recording** | [**LiveRecording**](LiveRecording.md) |  | 

## Example

```python
from ari_sync_sdk.models.recording_failed import RecordingFailed

# TODO update the JSON string below
json = "{}"
# create an instance of RecordingFailed from a JSON string
recording_failed_instance = RecordingFailed.from_json(json)
# print the JSON string representation of the object
print RecordingFailed.to_json()

# convert the object into a dict
recording_failed_dict = recording_failed_instance.to_dict()
# create an instance of RecordingFailed from a dict
recording_failed_from_dict = RecordingFailed.from_dict(recording_failed_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


