import os
from emanager.constants import *

acc_data_path = os.path.dirname(os.path.realpath(__file__))+"/acc_data"

    
def write_ledger(acc_no,trans_details):
    pd.read_csv(f"{acc_data_path}/{acc_no}.csv")
    trans_details.to_csv(f"{acc_path}/{acc_no}.csv", mode="a", header=False, index=False)
    
    
def write_transaction(trans_details):
    trans_data = {
        'PAYER'=treasury_acc,
        'PAYEE':treasury_acc
        "DATE": TIMESTAMP,
        "DEBITED": 0.00,
        "CREDITED": 0.00,,
    }
    trans_data.update(trans_details)
    for acc in ['PAYER','PAYEE']:
        write_ledger(trans_data[acc],
        
    trans_data = pd.DataFrame.from_dict(trans_data)
        print(trans_data)
        trans_data.to_csv(f"{acc_path}/treasury.csv", mode="a", header=False, index=False)
    write_ledger(trans_details['payer'])
    

