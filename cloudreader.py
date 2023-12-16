import numpy as np
import struct, os

input_folderpath = r''

files_list = []

for filename in os.listdir(input_folderpath):
    print(filename)
    filepath = os.path.join(input_folderpath,filename)

    size_float = 4
    list_pcd = []
    with open(filepath, "rb") as f:
        byte = f.read(size_float * 4)
        while byte:
            x, y, z, intensity = struct.unpack("ffff", byte)
            list_pcd.append([x, y, z])
            byte = f.read(size_float * 4)
    as_array = np.asarray(list_pcd)

    files_list.append(as_array)

final_mat = np.vstack(files_list)

np.savetxt('all_files.txt',final_mat)