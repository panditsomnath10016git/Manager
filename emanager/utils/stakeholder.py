import pandas as pd
import emanager.utils.file_ops as fop
import emanager.accounting.accounts as acc
from emanager.constants import TIMESTAMP

STAKEHOLDER_TYPE = {
    "WORKER": "W",
    "CUSTOMER": "C",
    "SUPPLIER": "S",
}


class StakeHolder:
    """Supplies common methods for initiating customer, worker, supplier"""

    def __init__(self, stakeholder_data_filename) -> None:
        """self.id_, self.data_format, self.data_dir
        must be declared in child classes of StakeHolder"""

        self.data_path = f"{self.data_dir}/{stakeholder_data_filename}"
        self.check_details()

    def check_details(self):
        """Check the database to find the stakeholder details and
        update the status of stakerholder object"""

        print("checking database...")
        self.acc_no = fop.get_acc_no(self.data_dir, self.id_)
        s_data = pd.read_csv(
            self.data_path,
            dtype=self.data_format,
            index_col="ID",
            sep=",",
        )
        self.name = s_data.loc[self.id_, "NAME"]
        self.details = s_data.loc[self.id_, :]
        print(self.details)
        print("Account no : ", self.acc_no)

    def update_details(self, update_acc=True, **kwargs):
        """Update details of a stakeholder"""

        # TODO check validity of kwargs
        print(f"updating {self.id_} detalils...")
        s_data = pd.read_csv(
            self.data_path, index_col="ID", sep=",", dtype=self.data_format
        )
        self.details = s_data.loc[self.id_, :]
        s_details = self.details.to_dict()
        s_details.update(kwargs)
        s_details.update(LAST_MODIFIED=TIMESTAMP)

        values = list(s_details.values())
        s_data.at[self.id_] = values
        # ?any way to insert only the changed data rather than reading all
        s_data.to_csv(self.data_path)
        print(f"{self.id_} details updated.")
        if update_acc:
            self._update_acc_details(**s_details)

        self.check_details()

    def _update_acc_details(self, **new_details):
        """Upadate the account details of the StakeHolder"""

        acc.Account(self.acc_no).update_details(**new_details)


class AddStakeHolder:
    """SUPPLIES common METHODS for adding customer, worker, supplier.
    This does NOT check for existing stakeholder in database, check with
    'check_stakeholder_existance' method"""

    # TODO replace loose words like type and group
    def __init__(self, stakeholder_type):
        """self.name, self.details, self.data_dir
        has to be decleared in child classes of AddStakeHolder"""

        self.mobile_no = self.details["MOBILE_NO"]
        self.address = self.details["ADDRESS"]
        self._type = STAKEHOLDER_TYPE[stakeholder_type]

        self.details.update(ID=self.__generate_id(), LAST_MODIFIED=TIMESTAMP)
        self.details_data = pd.DataFrame([self.details])
        print(self.details_data)

    def __generate_id(self):
        ts = TIMESTAMP.strftime("%y%m%d%M%S")
        self.id_ = self._type + self.details["GROUP"][0] + ts
        return self.id_

    def add_entry(self, path_to_data_file):
        """Appends the details of worker(self.details) to the file"""

        self.details_data.to_csv(
            path_to_data_file, mode="a", header=False, index=False
        )

    def open_account(self, **kwargs):
        """Open new account. Returns: acc_no"""

        acc_no = acc.CreateAccount(
            self.name, self.address, self.mobile_no, **kwargs
        ).acc_no
        fop.map_acc(self.data_dir, self.id_, acc_no)
        return acc_no


def check_stakeholder_existance(path_to_db, name):
    "If found returns 'id', else 'None'"
    # TODO a dynamic method which returns details with
    # each keystroke in entrybox of the UI.
    data = pd.read_csv(
        path_to_db,
        index_col="NAME",
        dtype={"MOBILE_NO": str},
        sep=",",
    )
    try:
        id_ = data.loc[name, "ID"]
        print(f"{name} exists...")
        details = data.loc[name, :]
        print(details)
    except KeyError:
        print(f"{name} is not in database.")
        id_ = None

    return id_
