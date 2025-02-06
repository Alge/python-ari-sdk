# TextMessage

A text message.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**body** | **str** | The text of the message. | 
**var_from** | **str** | A technology specific URI specifying the source of the message. For sip and pjsip technologies, any SIP URI can be specified. For xmpp, the URI must correspond to the client connection being used to send the message. | 
**to** | **str** | A technology specific URI specifying the destination of the message. Valid technologies include sip, pjsip, and xmp. The destination of a message should be an endpoint. | 
**variables** | **object** | Technology specific key/value pairs (JSON object) associated with the message. | [optional] 

## Example

```python
from ari_sync_sdk.models.text_message import TextMessage

# TODO update the JSON string below
json = "{}"
# create an instance of TextMessage from a JSON string
text_message_instance = TextMessage.from_json(json)
# print the JSON string representation of the object
print TextMessage.to_json()

# convert the object into a dict
text_message_dict = text_message_instance.to_dict()
# create an instance of TextMessage from a dict
text_message_from_dict = TextMessage.from_dict(text_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


