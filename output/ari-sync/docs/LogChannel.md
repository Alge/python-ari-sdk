# LogChannel

Details of an Asterisk log channel

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**channel** | **str** | The log channel path | 
**configuration** | **str** | The various log levels | 
**status** | **str** | Whether or not a log type is enabled | 
**type** | **str** | Types of logs for the log channel | 

## Example

```python
from ari_sync_sdk.models.log_channel import LogChannel

# TODO update the JSON string below
json = "{}"
# create an instance of LogChannel from a JSON string
log_channel_instance = LogChannel.from_json(json)
# print the JSON string representation of the object
print(LogChannel.to_json())

# convert the object into a dict
log_channel_dict = log_channel_instance.to_dict()
# create an instance of LogChannel from a dict
log_channel_from_dict = LogChannel.from_dict(log_channel_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


