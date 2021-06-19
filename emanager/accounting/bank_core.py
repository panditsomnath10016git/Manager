import os
from emanager.constants import TIMESTAMP, TREASURY_ACC_NO
import pandas as pd

# need to change  this method
acc_data_path = os.path.dirname(os.path.realpath(__file__)) + "/acc_data"


class Bank:
    def __init__(self):
        pass

    # def chart_of_accounts(self):
    # accounts = pd.read_csv("chart_of_accounts.csv")
    def refresh_database(self):
        pass
        self.update_chart_of_accounts()
        self.update_treasury()

    def update_treasury(self):
        pass

    def map_account_with_ID(self):
        pass


class Treasury:
    def __init__(self):
        self.acc_no = TREASURY_ACC_NO
        self.balance = self.get_balance()

    def get_balance(self):
        return (
            pd.read_csv(
                f"{acc_data_path}/{self.acc_no}.csv", usecols=["CR_BALANCE"]
            )
            .tail(1)
            .iloc[0, 0]
        )

    def archive_ledger(self):
        pass
