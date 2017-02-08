from geopy.geocoders import Nominatim
geolocator = Nominatim()
location = geolocator.reverse("4.638194, -74.0663803")
print(location.address)
# surti libros, Calle 51, Mariscal Sucre, Chapinero, Bogotá, 111311, Colombia
