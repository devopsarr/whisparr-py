# MovieCollection


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**tmdb_id** | **int** |  | [optional] 
**images** | [**List[MediaCover]**](MediaCover.md) |  | [optional] 

## Example

```python
from whisparr.models.movie_collection import MovieCollection

# TODO update the JSON string below
json = "{}"
# create an instance of MovieCollection from a JSON string
movie_collection_instance = MovieCollection.from_json(json)
# print the JSON string representation of the object
print MovieCollection.to_json()

# convert the object into a dict
movie_collection_dict = movie_collection_instance.to_dict()
# create an instance of MovieCollection from a dict
movie_collection_form_dict = movie_collection.from_dict(movie_collection_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


