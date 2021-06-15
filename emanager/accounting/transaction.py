import os
import uuid
from emanager.constants import TIMESTAMP
from emanager.accounting import ledger
import pandas as pd

acc_path = os.path.dirname(os.path.realpath(__file__))+"/acc_data"

class Transaction:
    """supplies withdrawl and deposit mechanism"""
    
    def __init__(self):
        print(super().__name__)#test method
        
    def deposit(self, amount, payer, remarks="Self Deposit"):
        trans_details = {
            'PAYER':payer,
            'TRANSACTION_ID':self.transaction_id(),
            'REMARKS': remarks,
            'CREDITED': amount, 
        }
        ledger.write_transaction(trans_details)
        

    def withdrawl(self, amount, benifactor, remarks="Self Withdrawl"):
        trans_details = {
            'PAYER':benifactor,
            'TRANSACTION_ID':self.transaction_id(),
            'REMARKS': remarks,
            'DEBITED': amount, 
        }
        ledger.write_transaction(trans_details)
        
    def transaction_id(self):
        self.transaction_id = uuid.uuid4().hex
