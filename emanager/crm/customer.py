from copy import deepcopy

import emanager.accounting.accounts as acc
from emanager.utils.data_types import CUSTOMER_DATA
from emanager.utils.directories import CRM_DATA_DIR
from emanager.utils.stakeholder import *

CRM_DATA_FILE_NAME = "customer_data.csv"
CRM_DATA_FILE_PATH = f"{CRM_DATA_DIR}/{CRM_DATA_FILE_NAME}"
CUSTOMER_GROUP = {
    "I": "Individual",
    "A": "Association",
    "B": "Business",
    "G": "Government",
}


class Customer(StakeHolder):
    def __init__(self, id_):
        print(f"Customer {id_}  initiated...")
        self.id_ = id_
        self.data_format = CUSTOMER_DATA
        self.data_dir = CRM_DATA_DIR
        super().__init__(CRM_DATA_FILE_NAME)

    def check_balance(self):
        pass


class AddCustomer(AddStakeHolder):
    """Add new customers to database"""

    def __init__(
        self, name, address, mobile_no, group=CUSTOMER_GROUP["I"], **acc_kwargs
    ):
        print(f"Adding new Customer {name}....")
        self.name = name
        self.data_dir = CRM_DATA_DIR
        self.details = deepcopy(CUSTOMER_DATA)
        self.details.update(
            {
                "NAME": name,
                "ADDRESS": address,
                "MOBILE_NO": mobile_no,
                "GROUP": group,
            }
        )
        super().__init__(stakeholder_type="CUSTOMER")
        self.add_entry(CRM_DATA_FILE_PATH)

        acc_no = acc.check_account_existance(self.name, self.mobile_no)
        if acc_no is None:
            self.open_account(**acc_kwargs)
