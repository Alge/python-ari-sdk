# ContactStatusChange


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**contact_info** | [**ContactInfo**](ContactInfo.md) |  | 
**endpoint** | [**Endpoint**](Endpoint.md) |  | 

## Example

```python
from ari_sync_sdk.models.contact_status_change import ContactStatusChange

# TODO update the JSON string below
json = "{}"
# create an instance of ContactStatusChange from a JSON string
contact_status_change_instance = ContactStatusChange.from_json(json)
# print the JSON string representation of the object
print ContactStatusChange.to_json()

# convert the object into a dict
contact_status_change_dict = contact_status_change_instance.to_dict()
# create an instance of ContactStatusChange from a dict
contact_status_change_from_dict = ContactStatusChange.from_dict(contact_status_change_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


