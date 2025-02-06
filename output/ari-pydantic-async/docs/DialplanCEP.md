# DialplanCEP

Dialplan location (context/extension/priority)

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**app_data** | **str** | Parameter of current dialplan application | 
**app_name** | **str** | Name of current dialplan application | 
**context** | **str** | Context in the dialplan | 
**exten** | **str** | Extension in the dialplan | 
**priority** | **int** | Priority in the dialplan | 

## Example

```python
from ari_sync_sdk.models.dialplan_cep import DialplanCEP

# TODO update the JSON string below
json = "{}"
# create an instance of DialplanCEP from a JSON string
dialplan_cep_instance = DialplanCEP.from_json(json)
# print the JSON string representation of the object
print DialplanCEP.to_json()

# convert the object into a dict
dialplan_cep_dict = dialplan_cep_instance.to_dict()
# create an instance of DialplanCEP from a dict
dialplan_cep_from_dict = DialplanCEP.from_dict(dialplan_cep_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


