from emanager.imports import *

## test Worker.py
worker_name = "Gurupada Pandit"
worker1 = Worker(worker_name)

if not worker1.have_id:
    address = "kamarpukur"  # str(input("Enter Address.. : "))
    age = 46
    mobile_no = "7908795631"  # str(input("Mobile No. : "))
    join_date = "20/03/2012"
    pay_r = 350.0
    group = "Owner"  # str(input("Worker Group :"))
    AddWorker(worker_name, age, address, mobile_no, join_date, pay_r, group=group)
    worker1 = Worker(worker_name)


worker1.update_details(["MOBILE_NO", "ADDRESS"], ["756024831", "Kamarpukur"])

worker1.update_pay_rate(400)


## test Custotmer.py
cstmr_name = "Somnath Pandit"
cstmr1 = Customer(cstmr_name)
if not cstmr1.have_id:
    address = "kamarpukur"  # str(input("Enter Address.. : "))
    mobile_no = "782264852"  # str(input("Mobile No. : "))
    group = "Individual"  # str(input("Customer Group :"))
    AddCustomer(cstmr_name, address, mobile_no, group=group)
    cstmr1 = Customer(worker_name)


cstmr1.update_details(["MOBILE_NO", "ADDRESS"], ["7264589260", "Kamarpukur"])
