from emanager.imports import *

# test worker.py
worker_name = "Worker 1"
worker1 = Worker(worker_name)

if not worker1.have_id:
    address = "address1"  # str(input("Enter Address.. : "))
    age = 46
    mobile_no = "7908795345"  # str(input("Mobile No. : "))
    join_date = "20/03/2017"
    pay_r = 250.0
    group = "Owner"  # str(input("Worker Group :"))
    AddWorker(
        worker_name, age, address, mobile_no, join_date, pay_r, group=group
    )
worker1 = Worker(worker_name)
worker1.update_details(MOBILE_NO="756024861", ADDRESS="new address1")
worker1.update_pay_rate(200)
