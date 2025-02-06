# DeviceState

Represents the state of a device.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of the device. | 
**state** | **str** | Device&#39;s state | 

## Example

```python
from ari_sync_sdk.models.device_state import DeviceState

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceState from a JSON string
device_state_instance = DeviceState.from_json(json)
# print the JSON string representation of the object
print(DeviceState.to_json())

# convert the object into a dict
device_state_dict = device_state_instance.to_dict()
# create an instance of DeviceState from a dict
device_state_from_dict = DeviceState.from_dict(device_state_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


