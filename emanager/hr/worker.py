import os
from copy import deepcopy
from emanager.utils.stakeholder import *
from emanager.utils.data_types import WORKER_DATA

hr_data_path = os.path.dirname(os.path.realpath(__file__)) + "/hr_data"

WORKER_GROUP = {"P": "Permanent", "T": "Temporary"}


class Worker(StakeHolder):
    def __init__(self, name):
        print(f"Worker {name}  initiated...")
        self.name = name
        self._type = "WORKER"
        self.data_format = WORKER_DATA
        super().__init__(f"{hr_data_path}/worker_data.csv")

    def _get_data(self):
        self.check_database()
        self.check_attendance()
        self.check_balance()

    def update_pay_rate(self, new_rate):
        self.update_details(PAY_RATE=new_rate)
        print("Pay Rate Updated.")

    def check_attendance(self):
        pass

    def check_balance(self):
        pass

    def update_attendance(self):
        pass

    # with open("attendance_sheet.csv") as a_data:


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
        **kwargs,
    ):
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
        self.add_entry(f"{hr_data_path}/worker_data.csv")
        self.open_account(**kwargs)
