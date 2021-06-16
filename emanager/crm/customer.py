import os
from emanager.constants import *
import pandas as pd

# import sqlite3

crm_file_path = os.path.dirname(os.path.realpath(__file__))
# TIMESTAMP = dt.now()


class Customer:
    """Check customer in database"""

    def __init__(self, name):
        self.name = name

        self.check_status()

    def check_status(self):
        c_data = pd.read_csv(f"{crm_file_path}/customer_data.csv", index_col="NAME")
        try:
            self.id = c_data.loc[self.name, "ID"]
            self.have_id = True
            self.details = c_data.loc[self.name, :]
            print("Details --\n", self.details)
        except:
            self.have_id = False

    def update_details(self, detail, new_value):
        """Update details of a Customer"

        Parameters
        ------------
        detail: str, list of str
            ADDRESS, MOBILE_NO, GROUP
        new_value: str, list of str
            new value of the detail
        """

        if type(detail) != list:
            detail = [detail]
            new_value = [new_value]

        c_data = pd.read_csv(f"{crm_file_path}/customer_data.csv", index_col="ID")
        c_data.at[self.id, detail + ["LAST_MODIFIED"]] = new_value + [TIMESTAMP]
        c_data.to_csv(f"{crm_file_path}/customer_data.csv")
        self.check_status()


class AddCustomer:
    """Add new customers to database
    group : Individual/ Association/ Business/ Government"""

    def __init__(self, name, address, mobile_no, group="Individual"):
        print("Adding new Customer....")
        self.name = name

        self.id = self.generate_id(name, group, id_type="C")
        self.add_entry(name, address, mobile_no, group)

    def generate_id(self, name, group, id_type="O"):
        initials = name.split()
        ts = TIMESTAMP.strftime("%y%m%d%H%S")
        id_no = id_type + group[0] + initials[0][0] + initials[1][0] + ts
        return id_no

    def add_entry(self, name, address, mobile_no, group):
        with open(f"{crm_file_path}/customer_data.csv", "a") as c_data:
            c_data.write(
                f"\n{self.id},{name},{address},{mobile_no},{group},{TIMESTAMP}"
            )
