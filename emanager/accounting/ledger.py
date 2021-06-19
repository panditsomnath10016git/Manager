import os
from typing import OrderedDict
import pandas as pd
from emanager.constants import TIMESTAMP, TREASURY_ACC_NO

acc_data_path = os.path.dirname(os.path.realpath(__file__)) + "/acc_data"


class Ledger:
    def write_transaction(self, acc_no, trans_details, new_acc=False):
        """updates ledgers with transaction details"""

        print("writing transaction..")
        __trans_data = OrderedDict(
            {
                "DATE": TIMESTAMP,
                "TRANSACTION_ID": " ",
                "REMARKS": " ",
                "DEBITED": 0.0,
                "CREDITED": 0.0,
                "CR_BALANCE": 0.0,
            }
        )
        __trans_data.update(trans_details)
        self.write_ledger(acc_no, __trans_data, new_acc=new_acc)
        if not new_acc:
            self.write_ledger(TREASURY_ACC_NO, __trans_data)
        print("account updated.\n")

    def write_ledger(self, acc_no, trans_details, new_acc=False):
        """write a ledger entry to the account
        with transaction details"""

        print(f"writing {acc_no} ledger...")
        if not new_acc:
            cr_balance = self.__get_cr_balance(acc_no, trans_details)
            trans_details.update({"CR_BALANCE": cr_balance})
        trans_entry = pd.DataFrame.from_dict([trans_details])
        trans_entry.to_csv(
            f"{acc_data_path}/{acc_no}.csv",
            mode="a",
            header=new_acc,
            index=False,
        )
        self.update_chart_of_accounts(acc_no)

    def update_chart_of_accounts(self, *args):

        pass

    def __get_cr_balance(self, acc_no, trans_details):
        return (
            pd.read_csv(
                f"{acc_data_path}/{acc_no}.csv", usecols=["CR_BALANCE"]
            )
            .tail(1)
            .iloc[0, 0]
            + trans_details["CREDITED"]
            - trans_details["DEBITED"]
        )
