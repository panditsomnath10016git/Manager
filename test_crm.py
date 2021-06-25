from emanager.imports import *

cstmr_name = "Customer 1"
id_ = check_existance_in_db(CRM_DATA_FILE, cstmr_name)

if id_ is None:
    address = "address1"
    mobile_no = "784512752"
    group = CUSTOMER_GROUP["I"]
    cstmr = AddCustomer(
        cstmr_name,
        address,
        mobile_no,
        group=group,
        first_deposit=1500,
        #   force_create=True,
    )
    id_ = cstmr.id_

cstmr = Customer(id_)

cstmr.update_details(
    GROUP=CUSTOMER_GROUP["A"], MOBILE_NO="956456831", ADDRESS="new address1"
)
