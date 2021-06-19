"""Want to assign all constants here such that it is available package wide"""

import datetime as dt


TIMESTAMP = dt.datetime.now()
TREASURY_ACC_NO = int(1000000001)

DATA_TYPES = {
    "ACC_CHART": {
        "ACCOUNT_NO": int,
        "NAME": str,
        "ADDRESS": str,
        "MOBILE_NO": str,
        "CR_BALANCE": float,
    }
}


def initialize_directories():
    pass
