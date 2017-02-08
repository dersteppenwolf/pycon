import os.path
import mapnik

data_path = "data/world_borders/TM_WORLD_BORDERS-0.3.shp"

polygon_symbolizer = mapnik.PolygonSymbolizer()
polygon_symbolizer.fill = mapnik.Color('#a1d99b')
polygon_symbolizer.fill_opacity = 0.7

line_symbolizer = mapnik.LineSymbolizer()
line_symbolizer.stroke = mapnik.Color('rgb(50%,50%,50%)')
line_symbolizer.stroke_width = 0.2

rule = mapnik.Rule()
rule.symbols.append(polygon_symbolizer)
rule.symbols.append(line_symbolizer)

style = mapnik.Style()
style.rules.append(rule)

layer = mapnik.Layer("mapLayer")
layer.datasource = mapnik.Shapefile(file=data_path)
layer.styles.append("mapStyle")

map = mapnik.Map(1024, 600)
map.background = mapnik.Color("#deebf7")
map.append_style("mapStyle", style)
map.layers.append(layer)
map.zoom_all()
mapnik.render_to_file(map, "images/simple_map.png", "png")
