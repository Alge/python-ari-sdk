# TextMessageReceived


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**endpoint** | [**Endpoint**](Endpoint.md) |  | [optional] 
**message** | [**TextMessage**](TextMessage.md) |  | 

## Example

```python
from ari_sync_sdk.models.text_message_received import TextMessageReceived

# TODO update the JSON string below
json = "{}"
# create an instance of TextMessageReceived from a JSON string
text_message_received_instance = TextMessageReceived.from_json(json)
# print the JSON string representation of the object
print TextMessageReceived.to_json()

# convert the object into a dict
text_message_received_dict = text_message_received_instance.to_dict()
# create an instance of TextMessageReceived from a dict
text_message_received_from_dict = TextMessageReceived.from_dict(text_message_received_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


