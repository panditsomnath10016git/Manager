import pandas as pd
from emanager.constants import TIMESTAMP
from emanager.utils.data_types import WORKER_DATA, CUSTOMER_DATA, SELLER_DATA
from emanager.accounting.accounts import CreateAccount

STAKEHOLDER_TYPE = {
    "WORKER": "W",
    "CUSTOMER": "C",
    "SUPPLIER": "S",
}


class StakeHolder:
    """Supplies common methods for initiating customer, worker, supplier"""

    def __init__(self, path_to_data_file) -> None:
        """self.name, self.data_format must be declared in child class"""
        
        self.data_path = path_to_data_file
        self.check_database()

    def check_database(self):
        """Check the database to find the stakeholder details and
        update the status of stakerholder object"""

        print("checking database...")
        s_data = pd.read_csv(
            self.data_path,
            dtype=self.data_format,
            index_col="NAME",
            sep=",",
        )
        try:
            self._id = s_data.loc[self.name, "ID"]
            print(f"{self.name} exists...")
            self.have_id = True
            self.details = s_data.loc[self.name, :]
            print(self.details)
        except KeyError:
            print(f"{self.name} is not in database.")
            self.have_id = False

    def update_details(self, **kwargs):
        """Update details of a stakeholder"""

        # TODO check validity of kwargs
        print(f"updating {self._id} detalils...")
        s_data = pd.read_csv(
            self.data_path, index_col="ID", sep=",", dtype=self.data_format
        )
        self.details = s_data.loc[self._id, :]
        s_details = self.details.to_dict()
        s_details.update(kwargs)
        s_details.update(LAST_MODIFIED=TIMESTAMP)

        values = list(s_details.values())
        s_data.at[self._id] = values
        # ?any way to insert only the changed data rather than readding all
        s_data.to_csv(self.data_path)
        print(f"{self._id} details updated.")
        self.check_database()
        #TODO update the account details also


class AddStakeHolder:
    """Supplies common methods for adding customer, worker, supplier"""

    # TODO replace loose words like type and group
    def __init__(self, stakeholder_type):
        """self.name, self.details from the child class"""

        self.mobile_no = self.details["MOBILE_NO"]
        self.address = self.details["ADDRESS"]
        self.__type = STAKEHOLDER_TYPE[str(stakeholder_type)]
        # TODO self.check_existance_in_db()

        self.details.update(ID=self.__generate_id(), LAST_MODIFIED=TIMESTAMP)
        self.details_data = pd.DataFrame([self.details])
        print(self.details_data)

    def check_existance_in_db(self):
        pass

    def __generate_id(self):
        ts = TIMESTAMP.strftime("%y%m%d%M%S")
        self.id_no = self.__type + self.details["GROUP"][0] + ts
        return self.id_no

    def add_entry(self, path_to_data_file):
        self.details_data.to_csv(
            path_to_data_file, mode="a", header=False, index=False
        )

    def open_account(self, **kwargs):
        "Open new account. Returns:acc_no"
        self.acc = CreateAccount(
            self.name, self.address, self.mobile_no, **kwargs
        )
        return self.acc.acc_no

    def __map_id_with_acc_no(self):
        pass
