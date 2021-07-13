import pandas as pd
from emanager.constants import TIMESTAMP, TREASURY_ACC_NO
from emanager.utils.directories import ACCOUNTING_DATA_DIR


class Ledger:
    def write_transaction(self, acc_no, trans_details, pay_worker=False, **kw):
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
        self.__write_ledger(acc_no, trans_data, **kw)
        if not pay_worker:
            self.__write_ledger(TREASURY_ACC_NO, trans_data)
        print("account updated.\n")

    def __write_ledger(self, acc_no, trans_details, new_acc=False):
        """write a ledger entry to the account
        with transaction details"""

        print(f"writing {acc_no} ledger...")
        if not new_acc:
            cr_balance = self._get_cr_balance(acc_no)
            write_mode = "a"
        else:
            cr_balance = 0.0
            write_mode = "w"
        new_cr_balance = (
            cr_balance + trans_details["CREDITED"] - trans_details["DEBITED"]
        )
        trans_details.update(CR_BALANCE=new_cr_balance)
        trans_entry = pd.DataFrame.from_dict([trans_details])
        trans_entry.to_csv(
            f"{ACCOUNTING_DATA_DIR}/{acc_no}.csv",
            mode=write_mode,
            header=new_acc,
            index=False,
        )
        self._update_cr_balance_in_chart(acc_no, new_cr_balance)

    # maybe move to bank_core
    def _update_cr_balance_in_chart(self, acc_no, new_cr_balance):
        acc_chart = pd.read_csv(
            f"{ACCOUNTING_DATA_DIR}/chart_of_accounts.csv",
            index_col="ACCOUNT_NO",
        )
        acc_chart.loc[acc_no, ["CR_BALANCE", "LAST_UPDATED"]] = [
            new_cr_balance,
            TIMESTAMP,
        ]
        acc_chart.to_csv(f"{ACCOUNTING_DATA_DIR}/chart_of_accounts.csv")
        # print(acc_chart.loc[acc_no, :])

    def _get_cr_balance(self, acc_no):
        return (
            pd.read_csv(
                f"{ACCOUNTING_DATA_DIR}/{acc_no}.csv", usecols=["CR_BALANCE"]
            )
            .tail(1)
            .iloc[0, 0]
        )
