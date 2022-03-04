import geocoder

g = geocoder.ip('me')
print(g.latlng[0])
print(g.latlng[1])
