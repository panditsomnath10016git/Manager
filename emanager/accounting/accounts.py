from copy import deepcopy

import pandas as pd
from emanager.accounting.transaction import Transaction
from emanager.constants import TIMESTAMP
from emanager.utils.data_types import ACC_CHART_DATA
from emanager.utils.directories import ACCOUNTING_DATA_DIR

ACC_CHART_DATA_PATH = ACCOUNTING_DATA_DIR + "/chart_of_accounts.csv"


class Account:
    def __init__(self, acc_no):
        print(f"account {acc_no} initiated.")
        self.acc_no = int(acc_no)
        self.details = self.get_details()

    def get_details(self):
        details = pd.read_csv(
            ACC_CHART_DATA_PATH,
            dtype=ACC_CHART_DATA,
            index_col="ACCOUNT_NO",
        ).loc[self.acc_no]
        return details

    def get_cr_balance(self):
        # account ledger and acc chart must have same cr_balance
        # as the chart updates with while writing ledger
        cr_balance = (
            pd.read_csv(f"{ACCOUNTING_DATA_DIR}/{self.acc_no}.csv")
            .tail(1)
            .iloc[0]["CR_BALANCE"]
        )
        return cr_balance

    def deposit(self, amount, **kw):
        Transaction().deposit(amount, self.acc_no, **kw)

    def withdrawl(self, amount, **kw):
        Transaction().withdrawl(amount, self.acc_no, **kw)

    def view_statement(self, upto=10):
        print(
            f"Last {upto} transactions.\n",
            30 * "-",
            "\n",
            pd.read_csv(f"{ACCOUNTING_DATA_DIR}/{self.acc_no}.csv").tail(upto),
        )

    def generate_passbook(self):
        # create pdf and send to a output folder
        pass

    def update_details(self, **new_details):
        """Upadate the account details"""

        acc_chart = pd.read_csv(
            ACC_CHART_DATA_PATH,
            index_col="ACCOUNT_NO",
            sep=",",
            dtype=ACC_CHART_DATA,
        )
        # Update only the sensible details
        updateable = dict(NAME="", ADDRESS="", MOBILE_NO="")
        a_details = dict(
            (k, new_details[k]) for k in updateable.keys() & new_details.keys()
        )
        acc_chart.at[
            self.acc_no, list(a_details.keys()) + ["LAST_UPDATED"]
        ] = list(a_details.values()) + [TIMESTAMP]
        acc_chart.to_csv(ACC_CHART_DATA_PATH)
        print(f"{self.acc_no} account details updated.")


class CreateAccount:
    """create account , add it to chart_of_accounts, start new ledger.
    does NOT check for existing account with same name or mobile no,
    check with 'check_account_existance' method"""

    def __init__(
        self,
        name,
        address,
        mobile_no,
        first_deposit=0.0,
    ):
        print("creating new account...")
        acc_details = deepcopy(ACC_CHART_DATA)
        acc_details.update(
            {
                "ACCOUNT_NO": self._generate_acc_no(),
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
            ACC_CHART_DATA_PATH,
            mode="a",
            header=False,
            index=False,
        )
        print("account created.\n", acc_data)
        # initiate the ledger
        Transaction().deposit(
            first_deposit,
            self.acc_no,
            remarks="new account created",
            new_acc=True,
        )

    def _generate_acc_no(self):
        # TODO map acc_no with ID no
        print("generating account number...")
        last_acc_no = (
            pd.read_csv(
                ACC_CHART_DATA_PATH,
                usecols=["ACCOUNT_NO"],
                dtype=int,
            )
            .iloc[:, 0]
            .max()
        )
        self.acc_no = last_acc_no + 1
        return self.acc_no


def check_account_existance(name, mobile_no):
    """If found only one account returns 'acc_no', else 'None'"""
    # TODO a dynamic method which returns details with
    # each keystroke in entrybox of the UI.
    acc_chart = pd.read_csv(
        ACC_CHART_DATA_PATH,
        dtype=ACC_CHART_DATA,
    )
    if acc_chart.isin([name, mobile_no]).any().any():
        try:
            acc_details = acc_chart.loc[acc_chart["NAME"] == name]
            print("Account already exist with Name : ", name)
            acc_no = acc_details.iloc[0]["ACCOUNT_NO"]
        except IndexError:
            acc_details = acc_chart.loc[acc_chart["MOBILE_NO"] == mobile_no]
            print("Account already exist with Mobile_no : ", mobile_no)
            acc_no = acc_details.iloc[0]["ACCOUNT_NO"]
        print(acc_details)
        if acc_details.shape[0] != 1:
            print("more than one account with same name or mobile_no.")
            acc_no = None
    else:
        print(f"No account with name '{name}' or mobile_no '{mobile_no}'.")
        acc_no = None

    return acc_no
