from emanager.imports import *

# test transacition.py
new_acc = CreateAccount("Somnath Pandit", "kamarpukur", "456821541")

acc1 = Account(new_acc.acc_no)
print("cr_balance ", acc1.cr_balance())
#acc1.update_details(ADDRESS="kamarpukur")
#acc1.deposit(100, remarks="testing account deposit")
#acc1.withdrawl(20, remarks="testing account withdrawl")

acc1.view_statement()
#print(acc1.details) 
Treasury().check_vault_status()