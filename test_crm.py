from emanager.imports import *

cstmr_name = "Customer 2"
cstmr1 = Customer(cstmr_name)

if not cstmr1.have_id:
    address = "address2"
    mobile_no = "784551852"
    group = CUSTOMER_GROUP["I"]
    AddCustomer(
        cstmr_name,
        address,
        mobile_no,
        group=group,
        first_deposit=150,
     #   force_create=True,
    )
    cstmr1 = Customer(cstmr_name)

cstmr1.update_details(
    GROUP=CUSTOMER_GROUP["A"], MOBILE_NO="756454831", ADDRESS="new address2"
)

