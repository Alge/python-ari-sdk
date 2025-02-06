# BridgeVideoSourceChanged


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bridge** | [**Bridge**](Bridge.md) |  | 
**old_video_source_id** | **str** |  | [optional] 

## Example

```python
from ari_sync_sdk.models.bridge_video_source_changed import BridgeVideoSourceChanged

# TODO update the JSON string below
json = "{}"
# create an instance of BridgeVideoSourceChanged from a JSON string
bridge_video_source_changed_instance = BridgeVideoSourceChanged.from_json(json)
# print the JSON string representation of the object
print(BridgeVideoSourceChanged.to_json())

# convert the object into a dict
bridge_video_source_changed_dict = bridge_video_source_changed_instance.to_dict()
# create an instance of BridgeVideoSourceChanged from a dict
bridge_video_source_changed_from_dict = BridgeVideoSourceChanged.from_dict(bridge_video_source_changed_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


