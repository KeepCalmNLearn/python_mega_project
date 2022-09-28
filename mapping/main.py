import folium
import pandas
from util import *

map = folium.Map(location=[38.58, -99.09], zoom_start=6, tiles="Stamen Terrain")
feature_group = folium.FeatureGroup("My Map Features")

data = pandas.read_csv("/Users/hemant.bharti/workspace/python/python_mega/mapping/Volcanoes.txt")
lat = data['LAT']
lon = data['LON']
elev = data['ELEV']

for lt, ln, el in zip(lat,lon,elev):
    feature_group.add_child(folium.Marker(location=[lt, ln], popup=f'Eleveation: {el}m', icon=folium.Icon(color=color_producer(el), icon="info-sign")))

map.add_child(feature_group)
map.save("map1.html")

