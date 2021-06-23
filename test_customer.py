from emanager.imports import*

cstmr_name = "Customer 2"
cstmr1 = Customer(cstmr_name)
if not cstmr1.have_id:
    address = "address2"  # str(input("Enter Address.. : "))
    mobile_no = "782261852"  # str(input("Mobile No. : "))
    group = "Individual"  # str(input("Customer Group :"))
    AddCustomer(cstmr_name, address, mobile_no, group=group)
    cstmr1 = Customer(worker_name)


cstmr1.update_details(MOBILE_NO="756454831", ADDRESS="new address2")