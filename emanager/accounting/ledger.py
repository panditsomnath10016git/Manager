import os
import pandas as pd
from emanager.constants import TIMESTAMP

treasury_acc='0000000001'#make consistent
acc_data_path = os.path.dirname(os.path.realpath(__file__))+"/acc_data"

def new_ledger(acc_no, trans_details):
    # it may be included into the other modules
    """creates a new ledger for the given account"""
    
    print(f'creating new ledger for acc {acc_no}')
    trans_data = {
        "DATE": TIMESTAMP,
        "TRANSACTION_ID": ' ',
        "REMARKS": ' ',
        "DEBITED": 0.0,
        "CREDITED": 0.0,
        "CR_BALANCE": 0.0,
    }
    trans_data.update(trans_details)
    trans_entry = pd.DataFrame.from_dict([trans_data])
    trans_entry.to_csv(f"{acc_data_path}/{acc_no}.csv", index=False)
    print('account updated.\n', trans_entry)


def write_ledger(acc_no,trans_details, new_acc=False):
    """write a ledger entry to the account 
            with transaction details"""
            
    print(f'writing ledger..')
    if not new_acc:
        cr_balance = pd.read_csv(f"{acc_data_path}/{acc_no}.csv").tail(1).loc[0]['CR_BALANCE']+trans_details['CREDITED']-trans_details['DEBITED']
        trans_details.update({'CR_BALANCE':cr_balance})
        trans_entry = pd.DataFrame.from_dict(trans_details)
        trans_entry.to_csv(f"{acc_data_path}/{acc_no}.csv", mode="a", header=False, index=False)
        trans_entry.to_csv(f"{acc_data_path}/treasury.csv", mode="a", header=False, index=False)
        print('account updated.\n', trans_entry)
    else:
        new_ledger(acc_no, trans_details)

def write_transaction(trans_details, kwargs):
    """updates ledgers with transaction details"""
    
    print(f'writing transaction..')
    trans_data = {
        'DATE': TIMESTAMP,
        'DEBITED': 0.00,
        'CREDITED': 0.00,
    }
    trans_data.update(trans_details)
    write_ledger(trans_data.pop('ACCOUNT'),trans_data, new_acc = kwargs.get('new_acc'))
    
    

