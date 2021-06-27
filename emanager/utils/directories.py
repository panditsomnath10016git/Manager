# generate the directories during setup

import os
from emanager.constants import BASE_DIR


HR_DATA_DIR = os.path.join(BASE_DIR, "hr/hr_data")
BUY_DATA_DIR = os.path.join(BASE_DIR, "buy/buy_data")
CRM_DATA_DIR = os.path.join(BASE_DIR, "crm/crm_data")
SELL_DATA_DIR = os.path.join(BASE_DIR, "sell/sell_data")
ACCOUNTING_DATA_DIR = os.path.join(BASE_DIR, "accounting/acc_data")

MAPFILE_DIRS = [HR_DATA_DIR, BUY_DATA_DIR, CRM_DATA_DIR, SELL_DATA_DIR]


def initialize_directories():
    pass
