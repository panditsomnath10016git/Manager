from copy import deepcopy

import pandas as pd
from emanager.utils.stakeholder import *
from emanager.utils.data_types import WORKER_DATA
from emanager.utils.directories import HR_DATA_DIR
from emanager.constants import TIMESTAMP


WORKER_DATA_FILE_NAME = "worker_data.csv"
WORKER_DATA_FILE_PATH = f"{HR_DATA_DIR}/{WORKER_DATA_FILE_NAME}"
ATTENDANCE_SHEET_PATH = f"{HR_DATA_DIR}/attendance_sheet.csv"
WORKER_GROUP = {"P": "Permanent", "T": "Temporary"}


class Worker(StakeHolder):
    def __init__(self, id_):
        print(f"Worker {id_}  initiated...")
        self.id_ = id_
        self.data_format = WORKER_DATA
        self.data_dir = HR_DATA_DIR
        super().__init__(WORKER_DATA_FILE_NAME)

    def _get_data(self):
        self.check_database()
        self.check_attendance()
        self.check_balance()

    def update_pay_rate(self, new_rate):
        self.update_details(PAY_RATE=new_rate)
        print("Pay Rate Updated.")

    def check_balance(self):
        pass

    def check_attendance(self, from_date, to_date):
        pass

    def deposit_salary(self):
        salary, last_calculated = self._calc_salary(self.id_)
        with open(f"{self.data_dir}/salary_deposit_log.csv") as log:
            log.write(f"ID,{last_calculated},{TIMESTAMP},{salary}\n")
            ####

        print(f"salary {salary} deposited in {self.id_} account.")

    def _calc_salary(self):
        pass


def update_attendance(attendance_data):
    """attendance data : dict,
    ID and attendance number as key value pairs.
    i.e. dict(WO2106242355=1, WO2106244555=0.5, WO2106242655=0)
    """

    sheet = pd.read_csv(
        ATTENDANCE_SHEET_PATH,
        index_col="DATE",
        sep=",",
        parse_dates=["DATE"],
        infer_datetime_format=True,
    )
    sheet.loc[
        pd.to_datetime(TIMESTAMP.date()), list(attendance_data.keys())
    ] = list(attendance_data.values())
    print(sheet)
    sheet.to_csv(ATTENDANCE_SHEET_PATH)
    print("attendance sheet updated.")


class AddWorker(AddStakeHolder):
    """Add new workers to database"""

    def __init__(
        self,
        name,
        age,
        address,
        mobile_no,
        join_date,
        pay_rate,
        group=WORKER_GROUP["P"],
        **acc_kwargs,
    ):
        print(f"Adding new Worker {name}....")
        self.name = name
        self.data_dir = HR_DATA_DIR
        self.details = deepcopy(WORKER_DATA)
        self.details.update(
            {
                "NAME": name,
                "AGE": age,
                "ADDRESS": address,
                "MOBILE_NO": mobile_no,
                "JOIN_DATE": join_date,
                "PAY_RATE": pay_rate,
                "GROUP": group,
            }
        )

        super().__init__(stakeholder_type="WORKER")
        self.add_entry(WORKER_DATA_FILE_PATH)
        if group == "Permanent":
            self.join_attendance_sheet()
        self.open_account(**acc_kwargs)

    def join_attendance_sheet(self):
        sheet = pd.read_csv(ATTENDANCE_SHEET_PATH)
        sheet[self.id_] = 0
        sheet.to_csv(ATTENDANCE_SHEET_PATH, index=False)
        print(f"{self.id_} joined attendance sheet.")
