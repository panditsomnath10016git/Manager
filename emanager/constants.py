"""Want to assign all constants here such that it is available package wide"""

import os
from datetime import datetime as dt

BASE_DIR = os.path.dirname(os.path.realpath(__file__))

TIMESTAMP = dt.strptime(
    dt.now().strftime("%Y-%m-%d %H:%M:%S"), "%Y-%m-%d %H:%M:%S"
)
TODAY = TIMESTAMP.date()

TREASURY_ACC_NO = int(1000000001)
