from emanager.imports import *

## test transacition.py
new_acc = CreateAccount("Somnath Pandit", "Kamarpukur", 9302112564)


print(new_acc.acc_no)
acc1 = Account(new_acc.acc_no)
acc1.deposit(120.5, remarks="testing account deposit")
acc1.withdrawl(300, remarks="testing account withdrawl")
