from copy import deepcopy

from emanager.utils.data_types import SUPPLIER_DATA
from emanager.utils.directories import BUY_DATA_DIR
from emanager.utils.stakeholder import *

BUY_DATA_FILE_NAME = "supplier_data.csv"
BUY_DATA_FILE_PATH = f"{BUY_DATA_DIR}/{BUY_DATA_FILE_NAME}"
SUPPLIER_GROUP = {"W": "Wood", "F": "Furniture", "H": "Hardware"}


class Supplier(StakeHolder):
    def __init__(self, id_):
        print(f"Supplier {id_}  initiated...")
        self.id_ = id_
        self.data_format = SUPPLIER_DATA
        self.data_dir = BUY_DATA_DIR
        super().__init__(BUY_DATA_FILE_NAME)

    def supply(self, item_id, quantity):
        pass


class AddSupplier(AddStakeHolder):
    """Add new suppliers to database"""

    def __init__(
        self, name, address, mobile_no, group="Other", **acc_kwargs
    ):
        print(f"Adding new Supplier {name}....")
        self.name = name
        self.data_dir = BUY_DATA_DIR
        self.details = deepcopy(SUPPLIER_DATA)
        self.details.update(
            {
                "NAME": name,
                "ADDRESS": address,
                "MOBILE_NO": mobile_no,
                "GROUP": group,
            }
        )
        super().__init__(stakeholder_type="SUPPLIER")
        self.add_entry(BUY_DATA_FILE_PATH)
        self.open_account(**acc_kwargs)
