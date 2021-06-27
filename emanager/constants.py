"""Want to assign all constants here such that it is available package wide"""

import os
from datetime import datetime as dt

BASE_DIR = os.path.dirname(os.path.realpath(__file__))

TIMESTAMP = dt.strptime(
    dt.now().strftime("%y-%m-%d %H:%M:%S"), "%y-%m-%d %H:%M:%S"
)

TREASURY_ACC_NO = int(1000000001)
