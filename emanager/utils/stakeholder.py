import pandas as pd
from emanager.constants import TIMESTAMP
from emanager.accounting.accounts import CreateAccount

STAKEHOLDER_TYPE = {
    "Worker": "W",
    "Customer": "C",
    "Supplier": "S",
}

STAKEHOLDER_SPFC_DETAILS = {
    "W": {
        "JOIN_DATE": "",
        "PAY_R": "",
    },
    "C": {},
    "S": {},
}


class StakeHolder:
    """Supplies common methods for initiating customer, worker, supplier"""

    def __init__(self, path_to_data_file) -> None:
        self.data_path = path_to_data_file
        self.check_database()

    def check_database(self):
        """Check the database to find the stakeholder details and
        update the status of stakerholder object"""

        print("checking database...")
        s_data = pd.read_csv(self.data_path, index_col="NAME")
        try:
            self.id = s_data.loc[self.name, "ID"]
            self.have_id = True
            self.details = s_data.loc[self.name, :]
            print(self.details)
        except AssertionError:
            self.have_id = False

    def update_details(self, **kwargs):
        """Update details of a stakeholder"""

        # TODO check validity of kwargs
        print("updating worker detalils...")
        s_details = self.details.to_dict()
        s_details.update(kwargs)
        s_data = pd.read_csv(self.path, index_col="ID")
        values = list(s_details.values())
        s_data.at[self.id] = values
        s_data.to_csv(self.data_path)
        self.check_database()


class AddStakeHolder:
    """Supplies common method for adding customer, worker, supplier"""

    # TODO replace loose words like type and group
    def __init__(
        self, name, address, mobile_no, stakeholder_type, group, **more_details
    ):
        """
        more_details: kwargs
            choose from STAKEHOLDER_SPFC_DETAILS
        stakeholder_type: str
            choose from STAKEHOLDER_TYPE i.e. 'Worker'
        group: str
            choose from the groups in types i.e. 'Permanent' in Worker type
        """

        self.name = name
        self.address = address
        self.mobile_no = mobile_no
        self.type_ = stakeholder_type[0]
        self.group = group[0]
        self.details = {
            "ID": self._generate_id(),
            "NAME": self.name,
            "ADDRESS": self.address,
            "MOBILE_NO": self.mobile_no,
            "GROUP": group,
        }
        more_details = STAKEHOLDER_SPFC_DETAILS[self.type_].update(
            more_details
        )
        # adding more details should be more explicit
        self.details.update(more_details)
        self.details = pd.DataFrame(self.details)
        print(self.details)

    def check_existance_in_db(self):
        pass

    def _generate_id(self):
        initials = self.name.split()
        ts = TIMESTAMP.strftime("%y%m%d%M%S")
        self.id_no = (
            self.type_ + self.group + initials[0][0] + initials[1][0] + ts
        )
        return self.id_no

    def add_entry(self, path_to_data_file):
        self.details.to_csv(
            path_to_data_file, mode="a", header=False, index=False
        )

    def open_account(self, **kwargs):
        "Open new account. Returns:acc_no"
        self.acc = CreateAccount(
            self.name, self.address, self.mobile_no, **kwargs
        )
        return self.acc.acc_no

    def map_id_with_acc_no(self):
        pass
