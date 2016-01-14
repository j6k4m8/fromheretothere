# fromheretothere

A python script to draw lines that map the elevation of a path between two points. Google is very nice to supply an API to help us out.

## Usage

```
python make_obj.py > out.obj
```

You can also use `fromheretothere` as its own standalone python module:

```python
>>> import fromheretothere as fh
>>> elvs = fh.get_elevation_array()
>>> elvs
[512, 499, 339, ... ]
>>> fh.make_graph(elvs) # yields a matplotlib window with a graph of elevation
```

Locations default to starting from the Empire State Building and ending at the Golden Gate Bridge. You can change these by supplying start and stop parameters to `get_elevation_array()`:

```python
>>> import fromheretothere as fh
>>> fh.get_elevation_array(start="40.748416,-73.9856605", stop="37.8113798,-122.4773046")
```

It is also possible to change the resolution of the map by using the `samples` parameter:

```python
>>> import fromheretothere as fh
>>> fh.get_elevation_array(samples=500)
```

`samples` defaults to 100.
