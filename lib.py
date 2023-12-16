import os
import numpy as np

def create_dir_if_not_exists(path):
    if not os.path.exists(path):
        os.makedirs(path)

# function to get last part of a path:
def get_last_part(path):
    return os.path.basename(path)

# function to get the second last part of a path:
def get_second_last_part(path):
    return os.path.basename(os.path.dirname(path))

# function to iterate through all folders in a directory, returning full paths to all subfolders contained within
def listdir_fullpath(d):
    return [os.path.join(d, f) for f in os.listdir(d)]

# function to read a .txt file, returning a tokenized list, shall give the option to user input the desired separator:
def read_txt(filename, separator=' '):
    with open(filename) as f:
        return [element for line in f for element in line.rstrip('\n').split(separator)]

def parse_pointcloud(filepath,outpath=None):
    import struct

    size_float = 4
    list_pcd = []
    with open(filepath, "rb") as f:
        byte = f.read(size_float * 4)
        while byte:
            x, y, z, intensity = struct.unpack("ffff", byte)
            list_pcd.append([x, y, z, intensity])
            byte = f.read(size_float * 4)
    
    if outpath:
        np.savetxt(outpath,np.asarray(list_pcd))

    return np.asarray(list_pcd)