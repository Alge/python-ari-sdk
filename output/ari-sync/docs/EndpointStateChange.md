# EndpointStateChange


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**endpoint** | [**Endpoint**](Endpoint.md) |  | 

## Example

```python
from ari_sync_sdk.models.endpoint_state_change import EndpointStateChange

# TODO update the JSON string below
json = "{}"
# create an instance of EndpointStateChange from a JSON string
endpoint_state_change_instance = EndpointStateChange.from_json(json)
# print the JSON string representation of the object
print(EndpointStateChange.to_json())

# convert the object into a dict
endpoint_state_change_dict = endpoint_state_change_instance.to_dict()
# create an instance of EndpointStateChange from a dict
endpoint_state_change_from_dict = EndpointStateChange.from_dict(endpoint_state_change_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


