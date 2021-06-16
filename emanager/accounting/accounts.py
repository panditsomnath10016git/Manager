import os
from emanager.constants import TIMESTAMP
from emanager.accounting.transaction import Transaction
from emanager.accounting.ledger import new_ledger
import pandas as pd

acc_data_path = os.path.dirname(os.path.realpath(__file__)) + "/acc_data"


class Account(Transaction):
    def __init__(self, acc_no):
        print(f"account {acc_no} initiated.")
        self.acc_no = acc_no
        self.acc_details = pd.read_csv(
            f"{acc_data_path}/chart_of_accounts.csv", index_col="ACCOUNT_NO"
        ).loc[acc_no]

    def deposit(self, amount, **kwargs):
        Transaction.deposit(self, amount, self.acc_no, **kwargs)

    def withdrawl(self, amount, **kwargs):
        Transaction.withdrawl(self, amount, self.acc_no, **kwargs)

    def cr_balance():
        pass

    def view_statement(upto=10):
        pass

    def generate_passbook():
        pass


class Treasury(Account):
    def __init__(self):
        acc_no = "0000000001"
        Account.__init__(acc_no)
        self.check_vault_status()

    def check_vault_status(self):
        vault = pd.read_csv(f"{acc_data_path}/treasury.csv")
        self.treasure_money = vault.tail(1)["CR_BALANCE"]
        print(self.treasure_money)
        self.last_10_transaction = vault.tail(10)


class CreateAccount:
    """create account , add it to chart_of_accounts, start new ledger"""

    def __init__(self, name, address, mobile_no, first_deposit=0.0):
        acc_chart = pd.read_csv(f"{acc_data_path}/chart_of_accounts.csv")
        if not acc_chart.isin([name, mobile_no]).any().any():
            print("creating new acccount...")
            self.generate_acc_no()
            acc_details = {
                "ACCOUNT_NO": self.acc_no,
                "NAME": name,
                "ADDRESS": address,
                "MOBILE_NO": mobile_no,
                "CR_BALANCE": first_deposit,
                "LAST_UPDATED": TIMESTAMP,
                "OPENING_DATE": TIMESTAMP,
            }
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
            print("Account already exist.")
            # show account details
            if any(acc_chart["NAME"] == name):
                acc_details = acc_chart[acc_chart["NAME"] == name]
            elif any(acc_chart["MOBILE_NO"] == mobile_no):
                acc_details = acc_chart[acc_chart["MOBILE_NO"] == mobile_no]

            self.acc_no = acc_details.iloc[0]["ACCOUNT_NO"]
            print(acc_details)

    def generate_acc_no(self):
        # TODO map acc_no with ID no
        print("generating account number...")
        last_acc_no = pd.read_csv(f"{acc_data_path}/chart_of_accounts.csv")[
            "ACCOUNT_NO"
        ].max()
        self.acc_no = last_acc_no + 1
