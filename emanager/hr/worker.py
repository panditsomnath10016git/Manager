from copy import deepcopy

import pandas as pd
from emanager.accounting.accounts import Account
from emanager.constants import TODAY
from emanager.utils.data_types import WORKER_DATA
from emanager.utils.directories import HR_DATA_DIR
from emanager.utils.file_ops import init_salary_log
from emanager.utils.stakeholder import *

WORKER_DATA_FILE_NAME = "worker_data.csv"
WORKER_DATA_FILE = f"{HR_DATA_DIR}/{WORKER_DATA_FILE_NAME}"
ATTENDANCE_SHEET = f"{HR_DATA_DIR}/attendance_sheet.csv"
SALARY_LOGFILE = f"{HR_DATA_DIR}/salary_deposit_log.csv"
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
        self.account_balance()

    def check_attendance(self, from_date, to_date):
        attendance = pd.read_csv(
            ATTENDANCE_SHEET,
            # index_col="DATE",
            sep=",",
            parse_dates=["DATE"],
            usecols=["DATE", self.id_],
            infer_datetime_format=True,
        )
        return attendance[
            (attendance["DATE"] >= pd.to_datetime(from_date))
            & (attendance["DATE"] < pd.to_datetime(to_date))
        ][self.id_].sum(axis=0)

    def calc_salary(self):
        """calculate salary from last pay date to yesterday
        returns salary, last_calculated"""

        print(f"calculating salary of {self.id_}...")
        salary_log = pd.read_csv(
            SALARY_LOGFILE,
            sep=",",
            parse_dates=True,
            infer_datetime_format=True,
        ).sort_values(by="TO_DATE")
        salary_log = salary_log[salary_log["ID"] == self.id_]
        last_calculated = salary_log.iloc[-1]["TO_DATE"]
        salary = (
            self.check_attendance(last_calculated, TODAY)
            * self.details["PAY_RATE"]
        )
        return salary, last_calculated

    def credit_salary(self):
        salary, last_calculated = self.calc_salary()
        if str(last_calculated) != str(TODAY):
            with open(SALARY_LOGFILE, "a") as log:
                log.write(f"{self.id_},{last_calculated},{TODAY},{salary}\n")
            if salary > 0:
                Account(self.acc_no).deposit(
                    salary, remarks="Salary", pay_worker=True
                )
                print(f"salary {salary} credited in {self.id_}'s account.")
        else:
            print("Salary already up-to-date.")


def update_attendance(attendance_data):
    """attendance data : dict,
    ID and attendance number as key value pairs.
    i.e. dict(WO2106242355=1, WO2106244555=0.5, WO2106242655=0)
    """

    sheet = pd.read_csv(
        ATTENDANCE_SHEET,
        index_col="DATE",
        sep=",",
        parse_dates=["DATE"],
        infer_datetime_format=True,
    )
    sheet.loc[pd.to_datetime(TODAY), list(attendance_data.keys())] = list(
        attendance_data.values()
    )
    sheet.to_csv(ATTENDANCE_SHEET)
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
        self.add_entry(WORKER_DATA_FILE)
        if group == "Permanent":
            self.join_attendance_sheet()
        self.open_account(**acc_kwargs)
        self.join_attendance_sheet()
        self._ping_salary_log()

    def join_attendance_sheet(self):
        sheet = pd.read_csv(ATTENDANCE_SHEET)
        sheet[self.id_] = 0.0
        sheet.to_csv(ATTENDANCE_SHEET, index=False)
        print(f"{self.id_} joined attendance sheet.")

    def _ping_salary_log(self):
        try:
            open(SALARY_LOGFILE, "r")
        except FileNotFoundError:
            init_salary_log(SALARY_LOGFILE)
        with open(SALARY_LOGFILE, "a") as log:
            log.write(f"{self.id_},{TODAY},{TODAY},0.0\n")
        print("pinged salary log.")
