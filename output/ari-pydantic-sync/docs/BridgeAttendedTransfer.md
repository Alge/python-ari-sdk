# BridgeAttendedTransfer


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**destination_application** | **str** | Application that has been transferred into | [optional] 
**destination_bridge** | **str** | Bridge that survived the merge result | [optional] 
**destination_link_first_leg** | [**Channel**](Channel.md) |  | [optional] 
**destination_link_second_leg** | [**Channel**](Channel.md) |  | [optional] 
**destination_threeway_bridge** | [**Bridge**](Bridge.md) |  | [optional] 
**destination_threeway_channel** | [**Channel**](Channel.md) |  | [optional] 
**destination_type** | **str** | How the transfer was accomplished | 
**is_external** | **bool** | Whether the transfer was externally initiated or not | 
**replace_channel** | [**Channel**](Channel.md) |  | [optional] 
**result** | **str** | The result of the transfer attempt | 
**transfer_target** | [**Channel**](Channel.md) |  | [optional] 
**transferee** | [**Channel**](Channel.md) |  | [optional] 
**transferer_first_leg** | [**Channel**](Channel.md) |  | 
**transferer_first_leg_bridge** | [**Bridge**](Bridge.md) |  | [optional] 
**transferer_second_leg** | [**Channel**](Channel.md) |  | 
**transferer_second_leg_bridge** | [**Bridge**](Bridge.md) |  | [optional] 

## Example

```python
from ari_sync_sdk.models.bridge_attended_transfer import BridgeAttendedTransfer

# TODO update the JSON string below
json = "{}"
# create an instance of BridgeAttendedTransfer from a JSON string
bridge_attended_transfer_instance = BridgeAttendedTransfer.from_json(json)
# print the JSON string representation of the object
print BridgeAttendedTransfer.to_json()

# convert the object into a dict
bridge_attended_transfer_dict = bridge_attended_transfer_instance.to_dict()
# create an instance of BridgeAttendedTransfer from a dict
bridge_attended_transfer_from_dict = BridgeAttendedTransfer.from_dict(bridge_attended_transfer_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


