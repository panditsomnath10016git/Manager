from emanager.imports import *

# test transacition.py
new_acc = CreateAccount("Test Account1", "address1", "1234567891")

acc1 = Account(new_acc.acc_no)
print("cr_balance ", acc1.cr_balance())
acc1.update_details(ADDRESS="new address")
acc1.deposit(100, remarks="testing account deposit")
acc1.withdrawl(20, remarks="testing account withdrawl")

acc1.view_statement()
# print(acc1.details)
print(Treasury().balance)