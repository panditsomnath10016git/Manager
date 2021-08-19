from emanager.utils.data_types import STOCK_LEDGER_DATA
from emanager.stock.stock import STOCK_LEDGER_FILE

# initate files

try:
    open(STOCK_LEDGER_FILE, "r")
except FileNotFoundError:
    with open(STOCK_LEDGER_FILE, "w") as file:
        entry = ""
        for col in STOCK_LEDGER_DATA.keys():
            entry += f"{col},"
        print(entry[0:-1])
        file.write(f"{entry[0:-1]}\n")
