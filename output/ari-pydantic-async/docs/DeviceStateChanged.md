# DeviceStateChanged


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**device_state** | [**DeviceState**](DeviceState.md) |  | 

## Example

```python
from ari_async_sdk.models.device_state_changed import DeviceStateChanged

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceStateChanged from a JSON string
device_state_changed_instance = DeviceStateChanged.from_json(json)
# print the JSON string representation of the object
print DeviceStateChanged.to_json()

# convert the object into a dict
device_state_changed_dict = device_state_changed_instance.to_dict()
# create an instance of DeviceStateChanged from a dict
device_state_changed_from_dict = DeviceStateChanged.from_dict(device_state_changed_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


