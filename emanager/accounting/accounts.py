import os
from copy import deepcopy
from emanager.constants import TIMESTAMP
from emanager.utils.data_types import ACC_CHART_DATA
from emanager.accounting.transaction import Transaction
import pandas as pd

acc_data_path = os.path.dirname(os.path.realpath(__file__)) + "/acc_data"


class Account:
    def __init__(self, acc_no):
        print(f"account {acc_no} initiated.")
        self.acc_no = str(acc_no)
        self.details = pd.read_csv(
            f"{acc_data_path}/chart_of_accounts.csv",
            dtype=ACC_CHART_DATA,
            index_col="ACCOUNT_NO",
        ).loc[int(acc_no)]

    def cr_balance(self):
        self.cr_balance = (
            pd.read_csv(f"{acc_data_path}/{self.acc_no}.csv")
            .tail(1)
            .iloc[0]["CR_BALANCE"]
        )
        return self.cr_balance

    def deposit(self, amount, **remarks):
        Transaction().deposit(amount, self.acc_no, **remarks)

    def withdrawl(self, amount, **remarks):
        Transaction().withdrawl(amount, self.acc_no, **remarks)

    def view_statement(self, upto=10):
        print(
            f"Last {upto} transactions.\n",
            30 * "-",
            "\n",
            pd.read_csv(f"{acc_data_path}/{self.acc_no}.csv").tail(upto),
        )

    def generate_passbook(self):
        # create pdf and send to a output folder
        pass

    def update_details(self, **kwargs):
        """Update details of account"""

        print("updating account details...")
        acc_details = self.details.to_dict()
        acc_details.update(kwargs)
        acc_chart = pd.read_csv(
            f"{acc_data_path}/chart_of_accounts.csv",
            dtype=ACC_CHART_DATA,
            index_col="ACCOUNT_NO",
        )
        values = list(acc_details.values())
        acc_chart.at[int(self.acc_no)] = values
        acc_chart.to_csv(f"{acc_data_path}/chart_of_accounts.csv")


class CreateAccount:
    """create account , add it to chart_of_accounts, start new ledger"""

    def __init__(
        self,
        name,
        address,
        mobile_no,
        first_deposit=0.0,
        force_create=False,
    ):
        acc_chart = pd.read_csv(
            f"{acc_data_path}/chart_of_accounts.csv",
            dtype=ACC_CHART_DATA,
        )
        if (not acc_chart.isin([name, mobile_no]).any().any()) or force_create:
            print("creating new account...")
            acc_details = deepcopy(ACC_CHART_DATA)
            acc_details.update(
                {
                    "ACCOUNT_NO": self.__generate_acc_no(),
                    "NAME": name,
                    "ADDRESS": address,
                    "MOBILE_NO": mobile_no,
                    "CR_BALANCE": 0.0,
                    "LAST_UPDATED": TIMESTAMP,
                    "OPENING_DATE": TIMESTAMP,
                }
            )
            acc_data = pd.DataFrame.from_dict([acc_details])
            acc_data.to_csv(
                f"{acc_data_path}/chart_of_accounts.csv",
                mode="a",
                header=False,
                index=False,
            )
            print("account created.\n", acc_data)
            # initiate the ledger
            Transaction().deposit(first_deposit, self.acc_no, new_acc=True)
        else:
            print("Account already exist", end=" ")
            # show account details
            if any(acc_chart["NAME"] == name):
                acc_details = acc_chart[acc_chart["NAME"] == name]
                print("with Name : ", name)
            elif any(acc_chart["MOBILE_NO"] == mobile_no):
                acc_details = acc_chart[acc_chart["MOBILE_NO"] == mobile_no]
                print("with Mobile_no : ", mobile_no)

            self.acc_no = acc_details.iloc[0]["ACCOUNT_NO"]
            # FOR more accounts with same name or mobile_no
            if acc_details.shape[0] != 1:
                print("more than one account with same name or mobile_no.")

            print(acc_details)

    def __generate_acc_no(self):
        # TODO map acc_no with ID no
        print("generating account number...")
        last_acc_no = (
            pd.read_csv(
                f"{acc_data_path}/chart_of_accounts.csv",
                usecols=["ACCOUNT_NO"],
                dtype=int,
            )
            .iloc[:, 0]
            .max()
        )
        self.acc_no = last_acc_no + 1
        return self.acc_no
