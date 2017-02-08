from shapely.geometry import mapping, shape
import fiona
# Read the original Shapefile
input = fiona.open('data.shp', 'r')
# bounds of the original shapefile
input.bounds
(258018.9133083854, 158162.863836, 268763.670357, 162621.686305)
# clip the shapefile with the raster bounds
clipped = input.filter(bbox=((262236.3101588468, 159973.80344954136, 263491.7250217228, 160827.485556297)))
# create the clipped shapefile with the same schema
clipped_schema = input.schema.copy()
with fiona.collection('clipped.shp', 'w', 'ESRI Shapefile', clipped_schema) as output:
    for elem in clipped:
           output.write({'properties': elem['properties'],'geometry': mapping(shape(elem['geometry']))})
