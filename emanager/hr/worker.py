import os
from emanager.constants import TIMESTAMP
import pandas as pd

hr_path = os.path.dirname(os.path.realpath(__file__))

WORKER_GROUPS = {"P": "Permanent", "T": "Temporary"}


class Worker:
    def __init__(self, name):
        self.name = name

        self.check_database()
        self.check_attendance()
        self.check_balance()

    def check_database(self):
        """Check the database to find the Worker details and
        update the status of Worker object"""

        print("checking worker database...")
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

    def update_details(self, **kwargs):
        """Update details of a Worker"""
        print("updating worker detalils...")
        w_details = self.details.to_dict()
        w_details.update(kwargs)
        w_data = pd.read_csv(f"{hr_path}/worker_data.csv", index_col="ID")
        values = list(w_details.values())
        w_data.at[self.id] = values
        w_data.to_csv(f"{hr_path}/worker_data.csv")
        self.check_database()

    def update_pay_rate(self, new_rate):
        print("updating worker pay rate...")
        w_data = pd.read_csv(f"{hr_path}/worker_data.csv", index_col="ID")
        w_data.at[self.id, ["PAY_RATE", "LAST_MODIFIED"]] = [
            new_rate,
            TIMESTAMP,
        ]
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
        self,
        name,
        age,
        address,
        mobile_no,
        join_date,
        pay_r,
        group="Temporary",
    ):
        print("Adding new Worker....")
        self.name = name

        self.id = self.__generate_id(name, group, id_type="W")
        self.__add_entry(
            name, age, address, mobile_no, join_date, pay_r, group
        )

    def __generate_id(self, name, group, id_type="X"):
        initials = name.split()
        ts = TIMESTAMP.strftime("%y%m%D%S")
        id_no = id_type + group[0] + initials[0][0] + initials[1][0] + ts
        return id_no

    def __add_entry(
        self, name, age, address, mobile_no, join_date, pay_r, group
    ):
        with open(f"{hr_path}/worker_data.csv", "a") as c_data:
            c_data.writelines(
                f"\n{self.id},{name},{age},{address},{mobile_no},{join_date},{pay_r},{group},{TIMESTAMP}"
            )
