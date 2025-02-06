# PeerStatusChange


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**endpoint** | [**Endpoint**](Endpoint.md) |  | 
**peer** | [**Peer**](Peer.md) |  | 

## Example

```python
from ari_sync_sdk.models.peer_status_change import PeerStatusChange

# TODO update the JSON string below
json = "{}"
# create an instance of PeerStatusChange from a JSON string
peer_status_change_instance = PeerStatusChange.from_json(json)
# print the JSON string representation of the object
print(PeerStatusChange.to_json())

# convert the object into a dict
peer_status_change_dict = peer_status_change_instance.to_dict()
# create an instance of PeerStatusChange from a dict
peer_status_change_from_dict = PeerStatusChange.from_dict(peer_status_change_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


