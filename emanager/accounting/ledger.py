import os
import pandas as pd
from emanager.constants import TIMESTAMP

acc_data_path = os.path.dirname(os.path.realpath(__file__)) + "/acc_data"
treasury_acc = "1000000001"


def update_chart_of_accounts(*args):
    pass


def get_cr_balance(acc_no, trans_details):
    return (
        pd.read_csv(f"{acc_data_path}/{acc_no}.csv")
        .tail(1)
        .iloc[0]["CR_BALANCE"]
        + trans_details["CREDITED"]
        - trans_details["DEBITED"]
    )


def write_ledger(acc_no, trans_details, new_acc=False):
    """write a ledger entry to the account
    with transaction details"""

    print(f"writing {acc_no} ledger...")
    if not new_acc:
        cr_balance = get_cr_balance(acc_no, trans_details)
        trans_details.update({"CR_BALANCE": cr_balance})
    trans_entry = pd.DataFrame.from_dict([trans_details])
    trans_entry.to_csv(
        f"{acc_data_path}/{acc_no}.csv",
        mode="a",
        header=new_acc,
        index=False,
    )
    update_chart_of_accounts(acc_no)


def write_transaction(acc_no, trans_details, new_acc=False):
    """updates ledgers with transaction details"""

    print("writing transaction..")
    trans_data = {
        "DATE": TIMESTAMP,
        "TRANSACTION_ID": " ",
        "REMARKS": " ",
        "DEBITED": 0.0,
        "CREDITED": 0.0,
        "CR_BALANCE": 0.0,
    }
    trans_data.update(trans_details)
    write_ledger(acc_no, trans_data, new_acc=new_acc)
    if not new_acc:
        write_ledger(treasury_acc, trans_data)
    print("account updated.\n")
