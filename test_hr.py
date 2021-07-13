from emanager.hr.worker import *
import emanager.utils.file_ops as fop

# fop.init_attendance_sheet(HR_DATA_DIR, ["WO2106242355"])

# test worker.py

worker_name = "Worker 1"
id_ = check_stakeholder_existance(WORKER_DATA_FILE, worker_name)

if id_ is None:
    address = "address2"
    age = 46
    mobile_no = "7908795345"
    join_date = "20/03/2017"
    pay_r = 250.0
    group = WORKER_GROUP["T"]
    worker = AddWorker(
        worker_name, age, address, mobile_no, join_date, pay_r, group=group
    )
    id_ = worker.id_
worker1 = Worker(id_)

# worker1.update_details(MOBILE_NO="756024861", ADDRESS="new address1")
# worker1.update_pay_rate(200)

update_attendance({id_: 1})
print("attendance check - ", worker1.check_attendance("2021-07-03", "2021-07-13"))
print("salary calc-",worker1.calc_salary())
worker1.credit_salary()
