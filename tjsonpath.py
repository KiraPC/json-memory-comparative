import json
import bigjson
from jsonpath_ng import jsonpath, parse

jsonpath_expr = parse('features[*].properties.test')

with open('huge.json', 'rb') as file:
    obj = bigjson.load(file)
    match = jsonpath_expr.find(obj)

    for k in match:
        print(k.value)

    # for feature in obj['features']:
    #     print(feature['properties']['MAPBLKLOT'])