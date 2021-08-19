from copy import deepcopy

import pandas as pd
from emanager.constants import TIMESTAMP
from emanager.utils.data_types import ITEM_DATA, STOCK_DATA, STOCK_LEDGER_DATA
from emanager.utils.directories import STOCK_DATA_DIR

# TODO file inits
ITEM_TYPES = []
STOCK_LEDGER_FILE = STOCK_DATA_DIR + "/stock_ledger.csv"
STOCK_DATA_FILE = STOCK_DATA_DIR + "/stock_data.csv"
ITEMS_DATA_FILE = STOCK_DATA_DIR + "/items.csv"


class Item:
    def __init__(self, id):
        self.__id = id

    def details(self) -> dict:
        return (
            pd.read_csv(
                ITEMS_DATA_FILE, sep=",", dtype=ITEM_DATA, index_col="ID"
            )
            .loc[self.__id]
            .to_dict()
        )

    def price(self) -> float:
        """Ptice of the item"""
        return self.details()["PRICE"]

    def available_quantity(self):
        pass

    def update_price(self, price):
        """Upade price of the item"""
        item_stock = pd.read_csv(
            ITEMS_DATA_FILE, sep=",", index_col="ID", dtype=ITEM_DATA
        )
        item_stock.loc[self.__id, ["PRICE", "LAST_UPDATED"]] = [
            price,
            TIMESTAMP,
        ]
        item_stock.to_csv(ITEMS_DATA_FILE)
        print(f"{self.__id} 's new price {price}")

    def add_quantity(self, quantity):
        """Add more quantity of this item in Stock"""
        item_stock = pd.read_csv(
            STOCK_DATA_FILE, sep=",", index_col="ITEM", dtype=STOCK_DATA
        )
        try:
            quantity += item_stock.loc[self.__id, "QUANTITY"]
        except KeyError:
            print(f"New item quantity {quantity}.")
        item_stock.loc[self.__id, ["QUANTITY", "LAST_UPDATED"]] = [
            quantity,
            TIMESTAMP,
        ]
        # print(item_stock)
        item_stock.to_csv(STOCK_DATA_FILE)
        print(f"{quantity} {self.__id} items added.")

    def remove_quantity(self, quantity):
        """Remove some quantity of this item from Stock"""
        item_stock = pd.read_csv(
            STOCK_DATA_FILE, sep=",", index_col="ITEM", dtype=STOCK_DATA
        )
        item_stock.loc[self.__id, ["QUANTITY", "LAST_UPDATED"]] = [
            item_stock.loc[self.__id, "QUANTITY"] - quantity,
            TIMESTAMP,
        ]
        # print(item_stock)
        item_stock.to_csv(STOCK_DATA_FILE)
        print(f"{quantity} {self.__id} items removed.")


class StockLedger:
    def __init__(self):
        pass

    def write_ledger(
        self,
        item_id,
        mode="ADD/REMOVE/PRICE_CHANGE",
        remarks="",
    ):
        trans_data = deepcopy(STOCK_LEDGER_DATA)
        trans_data.update(
            DATE=TIMESTAMP.date(),
            ITEM=item_id,
            MODE=mode,
            REMARKS=remarks,
        )
        pd.DataFrame([trans_data]).to_csv(
            STOCK_LEDGER_FILE, mode="a", index=False, header=False
        )


class Stock:
    def __init__(self):
        pass

    def stock_value(self) -> float:
        stock_data = pd.read_csv(
            STOCK_DATA_FILE,
            sep=",",
            usecols=["ITEM", "QUANTITY"],
            dtype=STOCK_DATA,
        )
        item_prices = pd.read_csv(
            ITEMS_DATA_FILE, sep=",", usecols=["ID", "PRICE"], dtype=ITEM_DATA
        ).rename(columns={"ID": "ITEM"})
        stock_data = stock_data.merge(item_prices, on="ITEM", how="outer")
        # print(stock_data)
        return sum(stock_data["QUANTITY"] * stock_data["PRICE"])

    def item_groups(self) -> list:
        with open(f"{STOCK_DATA_DIR}/item_groups.txt", "r") as file:
            return file.read().split("\n")

    def add_item_group(self, group):
        with open(f"{STOCK_DATA_DIR}/item_groups.txt", "r+") as file:
            groups = set(file.read().split("\n"))
            file.seek(0)
            file.truncate()
            groups.add(group)
            groups.remove("")
            for name in groups:
                file.write(f"{name}\n")
        print(f"New item group {group} added.")

    def get_item_id(self, group, model, variant) -> str:
        # TODO restrict id clash
        return f"{group[0:3]}{model[0:3]}{variant}".upper()

    def add_new_item(
        self, group, model, description, price, variant="V1", img="file"
    ) -> str:
        item = deepcopy(ITEM_DATA)
        # TODO find better id generating method
        _id = self.get_item_id(group, model, variant)
        item.update(
            ID=_id,
            GROUP=group,
            MODEL=model,
            VARIANT=variant,
            DESCRIPTION=description,
            PRICE=price,
            IMAGE=img,
            LAST_UPDATED=TIMESTAMP,
        )
        try:
            item.pop("ID")
            items = pd.read_csv(ITEMS_DATA_FILE, sep=",", index_col="ID")
            items.loc[_id, list(item.keys())] = list(item.values())
            items.to_csv(ITEMS_DATA_FILE)
        except FileNotFoundError:
            pd.DataFrame([item]).to_csv(ITEMS_DATA_FILE, index=False)
        self.add_item(_id, 0)
        print(f"New item in group {group} added.")
        return _id

    def add_item(self, item_id, quantity):
        Item(item_id).add_quantity(quantity)
        StockLedger()

    def remove_item(self, item_id, quantity):
        Item(item_id).remove_quantity(quantity)
        StockLedger()

    def current_state(self):
        pass

    def analytics(self):
        pass
