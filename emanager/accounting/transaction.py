import os
import uuid
from emanager.accounting import ledger

acc_data_path = os.path.dirname(os.path.realpath(__file__)) + "/acc_data"


class Transaction:
    """supplies withdrawl and deposit mechanism"""

    def __init__(self):
        pass

    def deposit(self, amount, payer, remarks="Self Deposit", new_acc=False):
        print(f"depositing {amount} rupees in acc {payer}...")
        trans_details = {
            "TRANSACTION_ID": self.__transaction_id(),
            "REMARKS": remarks,
            "CREDITED": amount,
        }
        ledger.write_transaction(payer, trans_details, new_acc=new_acc)

    def withdrawl(
        self, amount, benifactor, remarks="Self Withdrawl", new_acc=False
    ):
        print(f"withdrawing {amount} rupees from acc {benifactor}...")
        trans_details = {
            "TRANSACTION_ID": self.__transaction_id(),
            "REMARKS": remarks,
            "DEBITED": amount,
        }
        ledger.write_transaction(benifactor, trans_details, new_acc=new_acc)

    def __transaction_id(self):
        print("generating transaction id...")
        return uuid.uuid4().hex
