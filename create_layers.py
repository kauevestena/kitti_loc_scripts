import os
from time import sleep
import geopandas as gpd
from shapely import Point
from tqdm import tqdm
from lib import *


inpultfolderpath = r'..\KITTI_lidar\data'
outfolderpath = r"layers"

create_dir_if_not_exists(outfolderpath)

# function that given a list of txt files, parse them using "read_txt" function, and transform them into a geopandas dataframe. The geometry must be defined as latitude and longitude coordinates being the first two entries of each list:
def txtfile_list_to_geopandas(inputpath, crs='EPSG:4326'):
    data_dict = {
        'geometry': [],
        'alt': [],
        'roll': [],
        'pitch': [],
        'yaw': [],
        'vn': [],
        've': [],
        'vf': [],
        'vl': [],
        'vu': [],
        'ax': [],
        'ay': [],
        'az': [],
        'af': [],
        'al': [],
        'au': [],
        'wx': [],
        'wy': [],
        'wz': [],
        'wf': [],
        'wl': [],
        'wu': [],
        'posacc': [],
        'velacc': [],
        'navstat': [],
        'numsats': [],
        'posmode': [],
        'velmode': [],
        'orimode': [],
        'capture' : [],
    }

    for txtfile in listdir_fullpath(inputpath):
        parsed = read_txt(txtfile)

        filename = get_last_part(txtfile).split('.')[0]

        lat, lon, *data = parsed
        coords = Point(lon, lat)
        data_dict['geometry'].append(coords)
        for i, value in enumerate(data):
            data_dict[list(data_dict.keys())[i + 1]].append(value)

        data_dict['capture'].append(filename)

    return gpd.GeoDataFrame(data_dict, geometry='geometry', crs=crs)



for dirpath in tqdm(listdir_fullpath(inpultfolderpath)):
    for subfolderpath in listdir_fullpath(dirpath):
        for subsubfolderpath in listdir_fullpath(subfolderpath):

            oxt_path = os.path.join(subsubfolderpath, 'oxts','data')

            as_gdf = txtfile_list_to_geopandas(oxt_path)

            foldername = get_last_part(subsubfolderpath)

            outfilename = foldername + '.geojson'

            outfilepath = os.path.join(outfolderpath, outfilename)

            as_gdf.to_file(outfilepath,driver='GeoJSON')






