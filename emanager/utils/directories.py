# generate the directories during setup

import os
from emanager.constants import BASE_DIR


HR_DATA_DIR = os.path.join(BASE_DIR, "hr/hr_data")
BUY_DATA_DIR = os.path.join(BASE_DIR, "buy/buy_data")
CRM_DATA_DIR = os.path.join(BASE_DIR, "crm/crm_data")
SELL_DATA_DIR = os.path.join(BASE_DIR, "sell/sell_data")
ACCOUNTING_DATA_DIR = os.path.join(BASE_DIR, "accounting/acc_data")

MAPFILE_DIRS = [HR_DATA_DIR, BUY_DATA_DIR, CRM_DATA_DIR, SELL_DATA_DIR]

UI_ICONS_DIR = os.path.join(BASE_DIR, "UI/icons")


def guarantee_existence(path):
    if not os.path.exists(path):
        os.makedirs(path)
    return os.path.abspath(path)


def initialize_directories():
    pass
