# Peer

Detailed information about a remote peer that communicates with Asterisk.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address** | **str** | The IP address of the peer. | [optional] 
**cause** | **str** | An optional reason associated with the change in peer_status. | [optional] 
**peer_status** | **str** | The current state of the peer. Note that the values of the status are dependent on the underlying peer technology. | 
**port** | **str** | The port of the peer. | [optional] 
**time** | **str** | The last known time the peer was contacted. | [optional] 

## Example

```python
from ari_sync_sdk.models.peer import Peer

# TODO update the JSON string below
json = "{}"
# create an instance of Peer from a JSON string
peer_instance = Peer.from_json(json)
# print the JSON string representation of the object
print Peer.to_json()

# convert the object into a dict
peer_dict = peer_instance.to_dict()
# create an instance of Peer from a dict
peer_from_dict = Peer.from_dict(peer_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


