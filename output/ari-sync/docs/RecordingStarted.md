# RecordingStarted


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**recording** | [**LiveRecording**](LiveRecording.md) |  | 

## Example

```python
from ari_sync_sdk.models.recording_started import RecordingStarted

# TODO update the JSON string below
json = "{}"
# create an instance of RecordingStarted from a JSON string
recording_started_instance = RecordingStarted.from_json(json)
# print the JSON string representation of the object
print(RecordingStarted.to_json())

# convert the object into a dict
recording_started_dict = recording_started_instance.to_dict()
# create an instance of RecordingStarted from a dict
recording_started_from_dict = RecordingStarted.from_dict(recording_started_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


