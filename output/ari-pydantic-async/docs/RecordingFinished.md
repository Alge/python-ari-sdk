# RecordingFinished


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**recording** | [**LiveRecording**](LiveRecording.md) |  | 

## Example

```python
from ari_async_sdk.models.recording_finished import RecordingFinished

# TODO update the JSON string below
json = "{}"
# create an instance of RecordingFinished from a JSON string
recording_finished_instance = RecordingFinished.from_json(json)
# print the JSON string representation of the object
print RecordingFinished.to_json()

# convert the object into a dict
recording_finished_dict = recording_finished_instance.to_dict()
# create an instance of RecordingFinished from a dict
recording_finished_from_dict = RecordingFinished.from_dict(recording_finished_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


