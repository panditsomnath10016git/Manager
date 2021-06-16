import os
import uuid
from emanager.constants import TIMESTAMP
from emanager.accounting import ledger
import pandas as pd

acc_data_path = os.path.dirname(os.path.realpath(__file__)) + "/acc_data"


class Transaction:
    """supplies withdrawl and deposit mechanism"""

    def __init__(self):
        pass

    #  print(super())#testing

    def deposit(self, amount, payer, remarks="Self Deposit", **kwargs):
        print(f"depositing {amount} rupees in acc {payer}...")
        trans_details = {
            "ACCOUNT": payer,
            "TRANSACTION_ID": self.transaction_id(),
            "REMARKS": remarks,
            "CREDITED": amount,
        }
        ledger.write_transaction(trans_details, kwargs)

    def withdrawl(self, amount, benifactor, remarks="Self Withdrawl", **kwargs):
        print(f"withdrawing {amount} rupees from acc {benifactor}...")
        trans_details = {
            "ACCOUNT": benifactor,
            "TRANSACTION_ID": self.transaction_id(),
            "REMARKS": remarks,
            "DEBITED": amount,
        }
        ledger.write_transaction(trans_details, kwargs)

    def transaction_id(self):
        print(f"generating transaction id...")
        return uuid.uuid4().hex
