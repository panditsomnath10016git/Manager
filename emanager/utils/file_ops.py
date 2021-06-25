# methods for adding files during initial setup &

import os
import pickle as pkl
# from emanager.utils.directories import MAPFILE_DIRS


# def init_all_acc_mapfile():
#    for path in MAPFILE_DIRS:
#       init_acc_mapfile(path)


def init_acc_mapfile(path_to_file):
    with open(path_to_file, "wb") as mapfile:
        pkl.dump({"ID": "ACCOUNT_NO"}, mapfile)


def map_acc(path_to_data_dir, new_map={"ID": "ACCOUNT_NO"}):
    file_path = f"{path_to_data_dir}/acc_map.pkl"
    try:
        open(file_path, "rb")
    except FileNotFoundError:
        init_acc_mapfile(file_path)

    with open(file_path, "rb") as mapfile:
        map_data = pkl.load(mapfile)
    map_data.update(new_map)
    with open(file_path, "wb") as mapfile:
        pkl.dump(map_data, mapfile)


def get_acc_no(dir_of_mapfile, id_):
    with open(f"{dir_of_mapfile}/acc_map.pkl", "rb") as mapfile:
        map_data = pkl.load(mapfile)
    return map_data[id_]


def guarantee_existence(path):
    if not os.path.exists(path):
        os.makedirs(path)
    return os.path.abspath(path)
