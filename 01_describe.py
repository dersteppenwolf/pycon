import fiona
import pprint

data_path = "data/world_borders/TM_WORLD_BORDERS-0.3.shp"
c = fiona.open(data_path)

print c.driver
# 'ESRI Shapefile'

#  coordinate reference system (CRS)
print c.crs
# {'init': u'epsg:4326'}

# number of records
print len(c)
# 246

# minimum bounding rectangle (MBR)
print c.bounds
# (-179.99999999999997, -90.0, 180.0, 83.62359600000008)

pprint.pprint(c.schema)
'''
{'geometry': 'Polygon',
 'properties': OrderedDict([(u'FIPS', 'str:2'), (u'ISO2', 'str:2'),
 (u'ISO3', 'str:3'), (u'UN', 'int:3'), (u'NAME', 'str:50'),
 (u'AREA', 'int:7'), (u'POP2005', 'int:10'), (u'REGION', 'int:3'),
 (u'SUBREGION', 'int:3'), (u'LON', 'float:8.3'), (u'LAT', 'float:7.3')])}
'''
