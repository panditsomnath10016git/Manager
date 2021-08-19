ACC_CHART_DATA = {
    "ACCOUNT_NO": int,
    "NAME": object,
    "ADDRESS": object,
    "MOBILE_NO": object,
    "CR_BALANCE": float,
    "LAST_UPDATED": object,
    "OPENING_DATE": object,
}

WORKER_DATA = {
    "ID": object,
    "NAME": object,
    "AGE": int,
    "ADDRESS": object,
    "MOBILE_NO": object,
    "JOIN_DATE": object,
    "PAY_RATE": float,
    "GROUP": object,
    "LAST_MODIFIED": object,
}

CUSTOMER_DATA = {
    "ID": object,
    "NAME": object,
    "ADDRESS": object,
    "MOBILE_NO": object,
    "GROUP": object,
    "LAST_MODIFIED": object,
}

SUPPLIER_DATA = {
    "ID": object,
    "NAME": object,
    "ADDRESS": object,
    "MOBILE_NO": object,
    "GROUP": object,
    "LAST_MODIFIED": object,
}

ITEM_DATA = {
    "ID": object,
    "GROUP": object,
    "MODEL": object,
    "VARIANT": object,
    "DESCRIPTION": object,
    "PRICE": float,
    "IMAGE": object,
    "LAST_UPDATED": object,
}

STOCK_DATA = {
    "ITEM": object,
    "QUANTITY": int,
    "LAST_UPDATED": object,
}

STOCK_LEDGER_DATA = {
    "DATE": object,
    "ITEM": object,
    "MODE": object,
    "REMARKS": object,
}
