import csv
from shapely.geometry import Point, mapping
from fiona import collection
from fiona.crs import from_epsg

schema = { 'geometry': 'Point', 'properties': { 'depth': 'float:7.3', 'magnitude' : 'float:7.3' } }

with collection("data/shp/earthquakes.shp", "w", crs=from_epsg(4326),
                driver='ESRI Shapefile', schema=schema) as output:
    with open('data/earthquakes.csv', 'rb') as f:
        reader = csv.DictReader(f)
        for row in reader:
            point = Point(float(row['Longitude']), float(row['Latitude']))
            output.write({
                'properties': {
                    'depth': row['Depth'],'magnitude': row['Magnitude']
                },
                'geometry': mapping(point)
            })
