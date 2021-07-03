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


def init_attendance_sheet(sheet_dir, worker_ids: list):
    with open(f"{sheet_dir}/attendance_sheet.csv", "w") as sheet:
        sheet.write("DATE")
        for id in worker_ids:
            sheet.write(f",{id}")
        sheet.write("\n")


def init_salary_log(file_dir):
    with open(f"{file_dir}/salary_deposit_log.csv", "w") as log:
        log.write("ID,FROM_TIME,TO_TIME,CALCULATED_SALARY\n")
