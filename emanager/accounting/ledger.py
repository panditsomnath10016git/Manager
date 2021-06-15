import os
import pandas as pd
from emanager.constants import TIMESTAMP
from transaction import transaction_id

treasury_acc='0000000001'#make consistent
acc_data_path = os.path.dirname(os.path.realpath(__file__))+"/acc_data"

def new_ledger(acc_no):
    """creates a new ledger for the given account"""
    try:
        open(f"{acc_data_path}/{acc_no}.csv")
        print(f"Ledger already exists with account no {acc_no}.")
    except:
        trans_entry = pd.DataFrame.from_dict({
            "DATE": TIMESTAMP,
            "TRANSACTION_ID": transaction_id(),
            "REMARKS": "account opened",
            "DEBITED": 0.00,
            "CREDITED": 0.00,
            "CR_BALANCE": 0.00,
        })
        trans_entry.to_csv(f"{acc_data_path}/{acc_no}.csv", index=False)


def write_ledger(acc_no,trans_details):
    """write a ledger entry to the account with transaction details"""
    
    cr_balance = pd.read_csv(f"{acc_data_path}/{acc_no}.csv").tail(1)['CR_BALANCE']
    trans_details.update({'CR_BALANCE':cr_balance})
    trans_entry = pd.DataFrame.from_dict(trans_details).drop(['PAYER','PAYEE'], axis=1)
    trans_entry.to_csv(f"{acc_data_path}/{acc_no}.csv", mode="a", header=False, index=False)


def write_transaction(trans_details):
    """writes the ledger of both payer and payee"""
    
    trans_data = {
        'PAYER':treasury_acc,
        'PAYEE':treasury_acc
        'DATE': TIMESTAMP,
        'DEBITED': 0.00,
        'CREDITED': 0.00,
    }
    trans_data.update(trans_details)
    for acc in ['PAYER','PAYEE']:
        write_ledger(trans_data[acc],trans_data)
        
    print(trans_data)
    

