# Mailbox

Represents the state of a mailbox.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of the mailbox. | 
**new_messages** | **int** | Count of new messages in the mailbox. | 
**old_messages** | **int** | Count of old messages in the mailbox. | 

## Example

```python
from ari_sync_sdk.models.mailbox import Mailbox

# TODO update the JSON string below
json = "{}"
# create an instance of Mailbox from a JSON string
mailbox_instance = Mailbox.from_json(json)
# print the JSON string representation of the object
print(Mailbox.to_json())

# convert the object into a dict
mailbox_dict = mailbox_instance.to_dict()
# create an instance of Mailbox from a dict
mailbox_from_dict = Mailbox.from_dict(mailbox_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


