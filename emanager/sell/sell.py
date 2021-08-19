from emanager.sell.customer import Customer
from emanager.stock.stock import Item, Stock


class SellInvoice:
    def __init__(self) -> None:
        self.__id = 1  # generate invoice id

    def add_entry(self):
        pass

    def modify_entry(self):
        pass

    def show_invoice(self):
        pass

    def paid_amount(self, amount):
        pass

    def confirm_purchase(self):
        pass


class SellItem(Customer):
    def __init__(self, customer_id, item_id, quantity=1, amount_paid=None):
        self.item_id = item_id
        super().__init__(customer_id)
        item = Item(item_id)
        Stock().remove_item(item_id, quantity)
        self.withdraw_balance(
            item.price(),
            remarks=f"Purchased {item_id}: {item.details()['DESCRIPTION']}.",
        )
        if amount_paid is not None:
            self.deposit_balance(
                item.price(), remarks=f"Paid for {item_id} purchase."
            )
        # TODO save transaction details and generate receipt
