import os
from emanager.constants import *
import pandas as pd

# need to change  this method
acc_path = os.path.dirname(os.path.realpath(__file__)) + "/acc_data"


class Bank:
    def __init__(self):
        pass

    # def chart_of_accounts(self):
    #    accounts = pd.read_csv("chart_of_accounts.csv")

    def update_account_details(self, acc_no, detalis):
        # TODO
        pass
        acc_details = {
            "ACCOUNT_NO": self.acc_no,
            "NAME": name,
            "ADDRESS": address,
            "MOBILE_NO": mobile_no,
            "CR_BALANCE": first_deposit,
            "LAST_UPDATED": TIMESTAMP,
            "OPENING_DATE": TIMESTAMP,
        }
        acc_data = pd.DataFrame.from_dict(acc_details)
        print(acc_data)
        acc_data.to_csv(
            f"{acc_path}/chart_of_accounts.csv", mode="a", header=False, index=False
        )
