#!/usr/bin/env python
# -*- coding: utf-8 -*-

from geopy.geocoders import Nominatim
geolocator = Nominatim()
location = geolocator.geocode("carrera 11 #82 - 71, Bogotá, Colombia")

print(location.address)
# Carrera 11, El Nogal, Chapinero, Bogotá, Calle 82 No 10 - 33 Piso 5, Colombia

print((location.latitude, location.longitude))
# (4.6678326, -74.0514441)

print(location.raw)
'''
{u'display_name': u'Carrera 11, El Nogal, Chapinero, Bogot\xe1, Calle 82 No 10 - 33 Piso 5, Colombia',
u'importance': 0.42, u'place_id': u'145766568', u'lon': u'-74.0514441', u'lat': u'4.6678326',
u'osm_type': u'way',
u'licence': u'Data \xa9 OpenStreetMap contributors, ODbL 1.0. http://www.openstreetmap.org/copyright',
u'osm_id': u'375277348', u'boundingbox': [u'4.6678202', u'4.6678741', u'-74.0515172', u'-74.0514222'],
u'type': u'secondary', u'class': u'highway'}
'''
