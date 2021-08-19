# methods for adding files during initial setup &

# from emanager.utils.directories import MAPFILE_DIRS


# def init_all_acc_mapfile():
#    for path in MAPFILE_DIRS:
#       init_acc_mapfile(path)

# Account mapfile


def init_acc_mapfile(path_to_file):
    with open(path_to_file, "w") as mapfile:
        mapfile.write("ID,ACCOUNT_NO\n")


# Worker attendance sheet & salary


def init_attendance_sheet(attendance_sheetfile, worker_ids: list):
    with open(attendance_sheetfile, "w") as sheet:
        sheet.write("DATE")
        for id in worker_ids:
            sheet.write(f",{id}")
        sheet.write("\n")


def init_salary_log(salary_logfile):
    with open(salary_logfile, "w") as log:
        log.write("ID,FROM_DATE,TO_DATE,CALCULATED_SALARY\n")


# stock


def init_stock_ledger(filepath):
    with open(filepath, "w") as file:
        file.write("DATE,ITEM,MODE,REMARKS\n")


def init_stock_data(filepath):
    with open(filepath, "w") as file:
        file.write("ITEM,QUANTITY,LAST_UPDATED\n")
