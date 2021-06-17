import os
from emanager.constants import *
import pandas as pd

# need to change  this method
acc_path = os.path.dirname(os.path.realpath(__file__)) + "/acc_data"


class Bank:
    def __init__(self):
        pass

    # def chart_of_accounts(self):
    #    accounts = pd.read_csv("chart_of_accounts.csv")
    def refresh_database(self):
        pass
        self.update_chart_of_accounts()
        self.update_treasury()
        

    def update_chart_of_accounts(self):
        pass

    def update_treasury(self):
        pass

    def map_account_with_ID(self):
        pass
