from copy import deepcopy

import pandas as pd
from emanager.utils.data_types import ITEM_DATA
from emanager.utils.directories import STOCK_DATA_DIR

ITEM_TYPES = []
ITEMS_DATA_FILE = STOCK_DATA_DIR + "items.csv"


class Item:
    def __init__(self, id):
        self._id = id

    def available_quantity(self):
        pass

    def update_price(self):
        pass

    def add_quantity(self):
        pass

    def deduct_quantity(self):
        pass


def add_item_group(group):
    with open(f"{STOCK_DATA_DIR}/item_groups.txt", "a") as file:
        file.write(f"{group}\n")


def add_new_item(group, model, description, price, variant="V1"):
    item = deepcopy(ITEM_DATA)
    _id = f"{group[0:2]}{model[0:2]}{variant}".upper()
    item.update(
        ID=_id,
        GROUP=group,
        MODEL=model,
        VARIANT=variant,
        DESCRIPTION=description,
        PRICE=price,
    )
    item = pd.DataFrame(item)
    try:
        open(ITEMS_DATA_FILE, "r")
        item.to_csv(ITEMS_DATA_FILE, mode="a", header=False, index=False)
    except FileNotFoundError:
        item.to_csv(ITEMS_DATA_FILE, index=False)

    return _id
