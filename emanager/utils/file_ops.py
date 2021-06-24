# methods for adding files during initial setup &

import os
import pickle


def init_acc_mapfile(path):
    with open(f"{path}/acc_map", "wb") as mapfile:
        pickle.dump({"ID": "ACCOUNT_NO"}, mapfile)


def guarantee_existence(path):
    if not os.path.exists(path):
        os.makedirs(path)
    return os.path.abspath(path)
