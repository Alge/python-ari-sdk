# Bridge

The merging of media from one or more channels.  Everyone on the bridge receives the same audio.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bridge_class** | **str** | Bridging class | 
**bridge_type** | **str** | Type of bridge technology | 
**channels** | **List[str]** | Ids of channels participating in this bridge | 
**creationtime** | **date** | Timestamp when bridge was created | 
**creator** | **str** | Entity that created the bridge | 
**id** | **str** | Unique identifier for this bridge | 
**name** | **str** | Name the creator gave the bridge | 
**technology** | **str** | Name of the current bridging technology | 
**video_mode** | **str** | The video mode the bridge is using. One of &#39;none&#39;, &#39;talker&#39;, or &#39;single&#39;. | [optional] 
**video_source_id** | **str** | The ID of the channel that is the source of video in this bridge, if one exists. | [optional] 

## Example

```python
from ari_async_sdk.models.bridge import Bridge

# TODO update the JSON string below
json = "{}"
# create an instance of Bridge from a JSON string
bridge_instance = Bridge.from_json(json)
# print the JSON string representation of the object
print Bridge.to_json()

# convert the object into a dict
bridge_dict = bridge_instance.to_dict()
# create an instance of Bridge from a dict
bridge_from_dict = Bridge.from_dict(bridge_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


