from emanager.accounting.accounts import *

# test transacition.py
acc_no = check_account_existance("Test Account1", "1234567891")
if acc_no is None:
    new_acc = CreateAccount("Test Account1", "address1", "1234567891")

acc1 = Account(acc_no)
print(acc1.details["NAME"])
print("cr_balance ", acc1.get_cr_balance())
acc1.update_details(ADDRESS="new address1")
acc1.deposit(100, remarks="testing account deposit")
acc1.withdrawl(100, remarks="testing account withdrawl")

acc1.view_statement()
