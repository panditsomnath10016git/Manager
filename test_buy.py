from emanager.buy.supplier import *

supplier_name = "Supplier 1"
id_ = check_stakeholder_existance(BUY_DATA_FILE_PATH, supplier_name)

if id_ is None:
    address = "address1"
    mobile_no = "898512752"
    group = SUPPLIER_GROUP["W"]
    supplier = AddSupplier(
        supplier_name,
        address,
        mobile_no,
        group=group,
        #first_deposit=1500,
    )
    id_ = supplier.id_

supplier = Supplier(id_)

supplier.update_details(
    MOBILE_NO="956414569", ADDRESS="new address1"
)
