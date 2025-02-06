# Playback

Object representing the playback of media to a channel

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | ID for this playback operation | 
**language** | **str** | For media types that support multiple languages, the language requested for playback. | [optional] 
**media_uri** | **str** | The URI for the media currently being played back. | 
**next_media_uri** | **str** | If a list of URIs is being played, the next media URI to be played back. | [optional] 
**state** | **str** | Current state of the playback operation. | 
**target_uri** | **str** | URI for the channel or bridge to play the media on | 

## Example

```python
from ari_sync_sdk.models.playback import Playback

# TODO update the JSON string below
json = "{}"
# create an instance of Playback from a JSON string
playback_instance = Playback.from_json(json)
# print the JSON string representation of the object
print(Playback.to_json())

# convert the object into a dict
playback_dict = playback_instance.to_dict()
# create an instance of Playback from a dict
playback_from_dict = Playback.from_dict(playback_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


