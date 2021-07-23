import emanager.stock.item as itm
import pandas as pd
from emanager.utils.directories import STOCK_DATA_DIR


class Stock:
    def __init__(self):
        pass

    def ledger(self, item):
        pass

    def add_new_item(self, *args, **kwargs):
        itm.add_new_item(*args, **kwargs)

    def add_item(self, item):
        pass

    def remove_item(self, item):
        pass

    def current_state(self):
        pass

    def analytics(self):
        pass
