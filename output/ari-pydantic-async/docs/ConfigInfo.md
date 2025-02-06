# ConfigInfo

Info about Asterisk configuration

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**default_language** | **str** | Default language for media playback. | 
**max_channels** | **int** | Maximum number of simultaneous channels. | [optional] 
**max_load** | **float** | Maximum load avg on system. | [optional] 
**max_open_files** | **int** | Maximum number of open file handles (files, sockets). | [optional] 
**name** | **str** | Asterisk system name. | 
**setid** | [**SetId**](SetId.md) |  | 

## Example

```python
from ari_sync_sdk.models.config_info import ConfigInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ConfigInfo from a JSON string
config_info_instance = ConfigInfo.from_json(json)
# print the JSON string representation of the object
print ConfigInfo.to_json()

# convert the object into a dict
config_info_dict = config_info_instance.to_dict()
# create an instance of ConfigInfo from a dict
config_info_from_dict = ConfigInfo.from_dict(config_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


