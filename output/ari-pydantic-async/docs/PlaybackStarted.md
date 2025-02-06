# PlaybackStarted


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**playback** | [**Playback**](Playback.md) |  | 

## Example

```python
from ari_sync_sdk.models.playback_started import PlaybackStarted

# TODO update the JSON string below
json = "{}"
# create an instance of PlaybackStarted from a JSON string
playback_started_instance = PlaybackStarted.from_json(json)
# print the JSON string representation of the object
print PlaybackStarted.to_json()

# convert the object into a dict
playback_started_dict = playback_started_instance.to_dict()
# create an instance of PlaybackStarted from a dict
playback_started_from_dict = PlaybackStarted.from_dict(playback_started_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


