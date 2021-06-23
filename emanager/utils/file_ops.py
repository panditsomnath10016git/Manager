import os


def guarantee_existence(path):
    if not os.path.exists(path):
        os.makedirs(path)
    return os.path.abspath(path)
