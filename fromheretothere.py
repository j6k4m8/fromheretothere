import json
import urllib

DEFAULT_START = "40.748416,-73.9856605" # empire state building
DEFAULT_STOP = "37.8113798,-122.4773046" # golden gate bridge


def get_elevation_array(start=DEFAULT_START, stop=DEFAULT_STOP, samples=100):
    args = {
        "path": "{}|{}".format(start, stop),
        "samples": samples,
        "sensor": "false"
    }

    base_url = "http://maps.google.com/maps/api/elevation/json"
    url = "{}?{}".format(base_url, urllib.urlencode(args))

    response = json.loads(urllib.urlopen(url).read())
    return [r['elevation'] for r in response['results']]

def make_graph(data):
    import matplotlib.pyplot as plt
    plt.plot(data)
    plt.ylabel('Elevation')
    plt.show()
