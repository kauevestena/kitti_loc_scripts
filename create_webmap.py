import folium
import os
from lib import *
import geopandas as gpd


layerlist = listdir_fullpath('layers')

# function to create a folium map from a list of geojson files
def create_map(layerlist,location=[49.015, 8.43], zoom_start=10, outpath='map.html', drop_columns=None):
    m = folium.Map(location=location, zoom_start=zoom_start,tiles='OpenStreetMap')
    
    for layer in layerlist:
        gdf = gpd.read_file(layer)
        if drop_columns:
            gdf = gdf.drop(columns=drop_columns)
            
        folium.GeoJson(gdf,embed=False).add_to(m)
    
    m.save(outpath)

create_map(layerlist)