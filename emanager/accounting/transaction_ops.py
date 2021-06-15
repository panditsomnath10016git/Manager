import os
import uuid
from emanager.constants import *
import emanager.accounting import ledger
import pandas as pd

acc_path = os.path.dirname(os.path.realpath(__file__))+"/acc_data"

class Transaction:
    #TODO
    """acts as a mediator between two parties and returns them transaction details so that they can update their accounts"""
    
    def __init__(self):
        print(super().__name__)
        
    def deposit(self, amount, payer, remarks="Self Deposit"):
        trans_details = {
            'PAYER'=payer,
            'TRANSACTION_ID'=self.transaction_id(),
            'REMARKS': remarks,
            'CREDITED': amount, 
        }
        ledger.write_transaction(trans_details)
        
        self.check_vault_status()

    def withdrawl(self, amount, benifactor, remarks="Self Withdrawl"):
        trans_details = {
            "DATE": TIMESTAMP,
            "TRANSACTION_ID": self.transaction_id(),
            "REMARKS": remarks,
            "DEBITED": amount,
            "CREDITED": 0.00,
            "CR_BALANCE": self.treasure_money - amount,
        }
        trans_data = pd.DataFrame.from_dict(trans_details)
        print(trans_data)
        trans_data.to_csv(f"{acc_path}/treasury.csv", mode="a", header=False, index=False)
        self.check_vault_status()

    def transaction_id(self):
        self.transaction_id = uuid.uuid4().hex
