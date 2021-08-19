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

    def __init__(self, id, data_dir, stakeholder_data_filename, data_format):
        self._id = id
        self.data_dir = data_dir
        self.data_format = data_format
        self.data_path = f"{self.data_dir}/{stakeholder_data_filename}"
        self.check_details()

    def check_details(self):
        """Check the database to find the stakeholder details and
        update the status of stakerholder object"""

        print("checking database...")
        self.acc_no = self.get_acc_no()
        s_data = pd.read_csv(
            self.data_path,
            dtype=self.data_format,
            index_col="ID",
            sep=",",
        )
        self.name = s_data.loc[self._id, "NAME"]
        self.details = s_data.loc[self._id, :]
        print(self.details)
        print("Account no : ", self.acc_no)

    def account_balance(self):
        return acc.Account(self.acc_no).get_cr_balance()

    def deposit_balance(self, amount, **kw):
        acc.Account(self.acc_no).deposit(amount, **kw)

    def withdraw_balance(self, amount, **kw):
        acc.Account(self.acc_no).withdrawl(amount, **kw)

    def update_details(self, update_acc=True, **kwargs):
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
        # ?any way to insert only the changed data rather than reading all
        s_data.to_csv(self.data_path)
        print(f"{self._id} details updated.")
        if update_acc:
            self._update_acc_details(**s_details)

        self.check_details()

    def _update_acc_details(self, **new_details):
        """Upadate the account details of the StakeHolder"""

        acc.Account(self.acc_no).update_details(**new_details)

    def get_acc_no(self):
        acc_no = pd.read_csv(
            f"{self.data_dir}/acc_map.csv", index_col="ID"
        ).loc[self._id, "ACCOUNT_NO"]
        return acc_no


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

        self.details.update(ID=self._generate_id(), LAST_MODIFIED=TIMESTAMP)
        self.details_data = pd.DataFrame([self.details])
        print(self.details_data)

    def _generate_id(self):
        ts = TIMESTAMP.strftime("%y%m%d%M%S")
        self._id = self._type + self.details["GROUP"][0] + ts
        return self._id

    def add_entry(self, path_to_data_file):
        """Appends the details of worker(self.details) to the file"""

        try:
            open(path_to_data_file, "r")
            self.details_data.to_csv(
                path_to_data_file, mode="a", header=False, index=False
            )
        except FileNotFoundError:
            self.details_data.to_csv(path_to_data_file, index=False)

    def open_account(self, **kwargs):
        """Open new account. Returns: acc_no"""

        self.acc_no = acc.CreateAccount(
            self.name, self.address, self.mobile_no, **kwargs
        ).acc_no
        self._map_acc()
        return self.acc_no

    def _map_acc(self):
        file_path = f"{self.data_dir}/acc_map.csv"
        try:
            open(file_path, "r")
        except FileNotFoundError:
            fop.init_acc_mapfile(file_path)

        with open(file_path, "a") as mapfile:
            mapfile.write(f"{self._id},{self.acc_no}\n")


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
        _id = data.loc[name, "ID"]
        print(f"{name} exists...")
        details = data.loc[name, :]
        print(details)
    except KeyError:
        print(f"{name} is not in database.")
        _id = None

    return _id
