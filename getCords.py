import json

def cords(file):
    global cords
    cords = []
    with open(file) as f:
        data = json.load(f)
    for feature in data['features']:
        cords +=  feature['geometry']['coordinates'][0]
    return cords

file = '1_stepinieki8.geojson'

cords(file)