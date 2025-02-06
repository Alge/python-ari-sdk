# PlaybackFinished


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**playback** | [**Playback**](Playback.md) |  | 

## Example

```python
from ari_sync_sdk.models.playback_finished import PlaybackFinished

# TODO update the JSON string below
json = "{}"
# create an instance of PlaybackFinished from a JSON string
playback_finished_instance = PlaybackFinished.from_json(json)
# print the JSON string representation of the object
print(PlaybackFinished.to_json())

# convert the object into a dict
playback_finished_dict = playback_finished_instance.to_dict()
# create an instance of PlaybackFinished from a dict
playback_finished_from_dict = PlaybackFinished.from_dict(playback_finished_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


