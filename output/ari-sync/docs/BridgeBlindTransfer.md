# BridgeBlindTransfer


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bridge** | [**Bridge**](Bridge.md) |  | [optional] 
**channel** | [**Channel**](Channel.md) |  | 
**context** | **str** | The context transferred to | 
**exten** | **str** | The extension transferred to | 
**is_external** | **bool** | Whether the transfer was externally initiated or not | 
**replace_channel** | [**Channel**](Channel.md) |  | [optional] 
**result** | **str** | The result of the transfer attempt | 
**transferee** | [**Channel**](Channel.md) |  | [optional] 

## Example

```python
from ari_sync_sdk.models.bridge_blind_transfer import BridgeBlindTransfer

# TODO update the JSON string below
json = "{}"
# create an instance of BridgeBlindTransfer from a JSON string
bridge_blind_transfer_instance = BridgeBlindTransfer.from_json(json)
# print the JSON string representation of the object
print(BridgeBlindTransfer.to_json())

# convert the object into a dict
bridge_blind_transfer_dict = bridge_blind_transfer_instance.to_dict()
# create an instance of BridgeBlindTransfer from a dict
bridge_blind_transfer_from_dict = BridgeBlindTransfer.from_dict(bridge_blind_transfer_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


