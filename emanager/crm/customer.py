from copy import deepcopy
from emanager.utils.stakeholder import *
from emanager.utils.data_types import CUSTOMER_DATA
from emanager.utils.directories import CRM_DATA_DIR

CRM_DATA_FILE = CRM_DATA_DIR + "/customer_data.csv"
CUSTOMER_GROUP = {
    "I": "Individual",
    "A": "Association",
    "B": "Business",
    "G": "Government",
}

# TODO initating customer with name need to be change with id
# and for checking customer existance a different module to be created
class Customer(StakeHolder):
    def __init__(self, id_):
        print(f"Customer {id_}  initiated...")
        self.id_ = id_
        self.data_format = CUSTOMER_DATA
        self.data_dir = CRM_DATA_DIR
        super().__init__("customer_data.csv")

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
        self.add_entry(f"{self.data_dir}/customer_data.csv")
        self.open_account(**acc_kwargs)
