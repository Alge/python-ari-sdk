# Sound

A media file that may be played back.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**formats** | [**List[FormatLangPair]**](FormatLangPair.md) | The formats and languages in which this sound is available. | 
**id** | **str** | Sound&#39;s identifier. | 
**text** | **str** | Text description of the sound, usually the words spoken. | [optional] 

## Example

```python
from ari_async_sdk.models.sound import Sound

# TODO update the JSON string below
json = "{}"
# create an instance of Sound from a JSON string
sound_instance = Sound.from_json(json)
# print the JSON string representation of the object
print Sound.to_json()

# convert the object into a dict
sound_dict = sound_instance.to_dict()
# create an instance of Sound from a dict
sound_from_dict = Sound.from_dict(sound_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


