import emanager.utils.file_ops as fop
from emanager.stock.stock import *

# fop.init_stock_ledger(STOCK_LEDGER_FILE)
# fop.init_stock_data(STOCK_DATA_FILE)

#Stock().add_item_group("Sofa")
stk = Stock()
item_id = stk.add_new_item(
    "Sofa", "Hard Foam", "hard foam seat sofa", 11050, "CO", "imgfilepath2"
)
item = Item(item_id)
#item.update_price(1850)
#item.add_quantity(5)
#item.remove_quantity(1)
print("Stock Value=", stk.stock_value())
print(item.details())
