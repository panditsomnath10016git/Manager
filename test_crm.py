from emanager.imports import *

cstmr_name = "Customer 1"
cstmr1 = Customer(cstmr_name)

if not cstmr1.have_id:
    address = "address2"
    mobile_no = "782261852"
    group = CUSTOMER_GROUP["I"]
    AddCustomer(cstmr_name, address, mobile_no, group=group)
    cstmr1 = Customer(cstmr_name)


cstmr1.update_details(GROUP=CUSTOMER_GROUP["B"], MOBILE_NO="756454831", ADDRESS="address1")
