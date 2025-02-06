# BridgeMerged


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bridge** | [**Bridge**](Bridge.md) |  | 
**bridge_from** | [**Bridge**](Bridge.md) |  | 

## Example

```python
from ari_sync_sdk.models.bridge_merged import BridgeMerged

# TODO update the JSON string below
json = "{}"
# create an instance of BridgeMerged from a JSON string
bridge_merged_instance = BridgeMerged.from_json(json)
# print the JSON string representation of the object
print(BridgeMerged.to_json())

# convert the object into a dict
bridge_merged_dict = bridge_merged_instance.to_dict()
# create an instance of BridgeMerged from a dict
bridge_merged_from_dict = BridgeMerged.from_dict(bridge_merged_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


