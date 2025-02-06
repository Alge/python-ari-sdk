# LiveRecording

A recording that is in progress

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cause** | **str** | Cause for recording failure if failed | [optional] 
**duration** | **int** | Duration in seconds of the recording | [optional] 
**format** | **str** | Recording format (wav, gsm, etc.) | 
**name** | **str** | Base name for the recording | 
**silence_duration** | **int** | Duration of silence, in seconds, detected in the recording. This is only available if the recording was initiated with a non-zero maxSilenceSeconds. | [optional] 
**state** | **str** |  | 
**talking_duration** | **int** | Duration of talking, in seconds, detected in the recording. This is only available if the recording was initiated with a non-zero maxSilenceSeconds. | [optional] 
**target_uri** | **str** | URI for the channel or bridge being recorded | 

## Example

```python
from ari_sync_sdk.models.live_recording import LiveRecording

# TODO update the JSON string below
json = "{}"
# create an instance of LiveRecording from a JSON string
live_recording_instance = LiveRecording.from_json(json)
# print the JSON string representation of the object
print(LiveRecording.to_json())

# convert the object into a dict
live_recording_dict = live_recording_instance.to_dict()
# create an instance of LiveRecording from a dict
live_recording_from_dict = LiveRecording.from_dict(live_recording_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


