import os
from emanager.constants import *
import pandas as pd

hr_path = os.path.dirname(os.path.realpath(__file__))


class Worker:
    def __init__(self, name):
        self.name = name

        self.check_database()
        self.check_attendance()
        self.check_balance()

    def check_database(self):
        """Check the database to find the Worker details and
        update the status of Worker object"""

        w_data = pd.read_csv(f"{hr_path}/worker_data.csv", index_col="NAME")
        try:
            self.id = w_data.loc[self.name, "ID"]
            self.have_id = True
            self.details = w_data.loc[self.name, :]
            print(self.details)
        except:
            self.have_id = False

    def refresh_data(self):
        self.check_database()
        self.check_attendance()
        self.check_balance()

    def update_details(self, detail, new_value):
        """Update details of a Worker"

        Parameters
        ------------
        detail: str, list of str
            NAME, AGE, ADDRESS, MOBILE_NO, PAY_RATE, GROUP
        new_value: str, list of str
            new value of the detail
        """

        if type(detail) != list:
            detail = [detail]
            new_value = [new_value]
            print("Details Updated :\n", detail)

        w_data = pd.read_csv(f"{hr_path}/worker_data.csv", index_col="ID")
        w_data.at[self.id, detail + ["LAST_MODIFIED"]] = new_value + [TIMESTAMP]
        w_data.to_csv(f"{hr_path}/worker_data.csv")
        self.check_database()

    def update_pay_rate(self, new_rate):
        w_data = pd.read_csv(f"{hr_path}/worker_data.csv", index_col="ID")
        w_data.at[self.id, ["PAY_RATE", "LAST_MODIFIED"]] = [new_rate, TIMESTAMP]
        w_data.to_csv(f"{hr_path}/worker_data.csv")
        self.check_database()

    def check_attendance(self):
        pass

    def check_balance(self):
        pass

    def update_attendance(self):
        pass

    # with open("attendance_sheet.csv") as a_data:


class AddWorker:
    """Add new workers to database
    group : Permanent/ Temporary"""

    def __init__(
        self, name, age, address, mobile_no, join_date, pay_r, group="Temporary"
    ):
        print("Adding new Worker....")
        self.name = name

        self.id = self.generate_id(name, group, id_type="W")
        self.add_entry(name, age, address, mobile_no, join_date, pay_r, group)

    def generate_id(self, name, group, id_type="X"):
        initials = name.split()
        ts = TIMESTAMP.strftime("%y%m%S")
        id_no = id_type + group[0] + initials[0][0] + initials[1][0] + ts
        return id_no

    def add_entry(self, name, age, address, mobile_no, join_date, pay_r, group):
        with open(f"{hr_path}/worker_data.csv", "a") as c_data:
            c_data.write(
                f"\n{self.id},{name},{age},{address},{mobile_no},{join_date},{pay_r},{group},{TIMESTAMP}"
            )
