# FormatLangPair

Identifies the format and language of a sound file

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**format** | **str** |  | 
**language** | **str** |  | 

## Example

```python
from ari_async_sdk.models.format_lang_pair import FormatLangPair

# TODO update the JSON string below
json = "{}"
# create an instance of FormatLangPair from a JSON string
format_lang_pair_instance = FormatLangPair.from_json(json)
# print the JSON string representation of the object
print FormatLangPair.to_json()

# convert the object into a dict
format_lang_pair_dict = format_lang_pair_instance.to_dict()
# create an instance of FormatLangPair from a dict
format_lang_pair_from_dict = FormatLangPair.from_dict(format_lang_pair_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


