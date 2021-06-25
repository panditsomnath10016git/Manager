"""Want to assign all constants here such that it is available package wide"""

import os
import datetime as dt

BASE_DIR = os.path.dirname(os.path.realpath(__file__))

TIMESTAMP = dt.datetime.now()

TREASURY_ACC_NO = int(1000000001)
