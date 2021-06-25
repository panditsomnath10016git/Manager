# methods for adding files during initial setup &

import os
import pandas as pd

# from emanager.utils.directories import MAPFILE_DIRS


# def init_all_acc_mapfile():
#    for path in MAPFILE_DIRS:
#       init_acc_mapfile(path)


def init_acc_mapfile(path_to_file):
    with open(path_to_file, "w") as mapfile:
        mapfile.write("ID,ACCOUNT_NO\n")


def map_acc(path_to_data_dir, ID, ACCOUNT_NO):
    file_path = f"{path_to_data_dir}/acc_map.csv"
    try:
        open(file_path, "r")
    except FileNotFoundError:
        init_acc_mapfile(file_path)

    with open(file_path, "a") as mapfile:
        mapfile.write(f"{ID},{ACCOUNT_NO}\n")


def get_acc_no(dir_of_mapfile, id_):
    acc_no = pd.read_csv(f"{dir_of_mapfile}/acc_map.csv", index_col="ID").loc[
        id_, "ACCOUNT_NO"
    ]
    return acc_no


def guarantee_existence(path):
    if not os.path.exists(path):
        os.makedirs(path)
    return os.path.abspath(path)
