import os
from copy import deepcopy
from emanager.utils.stakeholder import *
from emanager.utils.data_types import CUSTOMER_DATA

# import sqlite3

crm_data_path = os.path.dirname(os.path.realpath(__file__)) + "/crm_data"
# TIMESTAMP = dt.now()
CUSTOMER_GROUP = {"I": "Individual", "B": "Business", "G": "Government"}


class Customer(StakeHolder):
    def __init__(self, name):
        print(f"Customer {name}  initiated...")
        self.name = name
        self._type = "CUSTOMER"
        self.data_format = CUSTOMER_DATA
        super().__init__(f"{crm_data_path}/customer_data.csv")

    def check_balance(self):
        pass


class AddCustomer(AddStakeHolder):
    """Add new customers to database
    group : Individual/ Association/ Business/ Government"""

    def __init__(
        self, name, address, mobile_no, group=CUSTOMER_GROUP["I"], **acc_kwargs
    ):
        print(f"Adding new Customer {name}....")
        self.name = name

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
        self.add_entry(f"{crm_data_path}/customer_data.csv")
        self.open_account(**acc_kwargs)
