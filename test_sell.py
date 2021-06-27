from emanager.sell.customer import *

cstmr_name = "Customer 1"
id_ = check_stakeholder_existance(SELL_DATA_FILE_PATH, cstmr_name)

if id_ is None:
    address = "address2"
    mobile_no = "894512752"
    group = CUSTOMER_GROUP["I"]
    cstmr = AddCustomer(
        cstmr_name,
        address,
        mobile_no,
        group=group,
        first_deposit=1500,
    )
    id_ = cstmr.id_

cstmr = Customer(id_)

cstmr.update_details(
    GROUP=CUSTOMER_GROUP["I"], MOBILE_NO="956414831", ADDRESS="address1"
)
