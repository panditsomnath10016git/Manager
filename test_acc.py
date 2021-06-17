from emanager.imports import *

## test transacition.py
new_acc = CreateAccount("Somnath Pandit", "kamarpukur", "9302112564")


print(new_acc.acc_no)
acc1 = Account(new_acc.acc_no)
print("cr_balance ", acc1.cr_balance())
acc1.update_details(ADDRESS="kamarpukur")
# acc1.deposit(870.5, remarks="testing account deposit")
# acc1.withdrawl(12, remarks="testing account withdrawl")
acc1.view_statement()
print(acc1.details)
Treasury().check_vault_status()
