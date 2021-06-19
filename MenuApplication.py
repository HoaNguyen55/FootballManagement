# Program Name: MenuDrivenProgram
# Author: Hoa Nguyen
# Data: June 12,2021
# Note: Chuong trinh nay co nhieu chuc nang de quan ly bong da

# Chia se mot file chung

import json
import funcManageUtils as fmUtils
import matplotlib.pyplot as plt

# Chuc nang 1: Nhap
database_name = 'venv/WorldCup2022.json'
# filesave = 'venv/data_after_processing'


def NhapVaGhi():
    print("\n<><><> Chào mừng bạn đến với chức năng Nhập yêu cầu và ghi file <><><>")
    fmUtils.input_data(database_name)
    return

# Chuc nang 2: Hoi dap


def HoiVaDap():
    print("\n<><><> Chào mừng bạn đến với chức năng Hỏi và Đáp <><><>")
    fmUtils.input_qanda(database_name)
    return

# Chuc nang 3: Phan tich


def PhanTichDuLieu():
    print("<><><> Chuc nang phan tich, doc file abc.txt de tra loi <><><>")

    return


def Menu(select_opt):
    switcher = {
        1: NhapVaGhi,
        2: HoiVaDap,
        3: PhanTichDuLieu
    }
    func = switcher.get(select_opt, lambda: "Du lieu sai")

    func()


while True:
    print("\n \t\t\t <><><> Welcome to Football Management Application <><><>")
    selOpt = int(input("\nVui lòng chọn các yêu cầu sau: \n"
                       "\t1. Nhập dữ liệu  \n"
                       "\t2. Hỏi và đáp    \n"
                       "\t3. Phân tích dữ liệu theo yêu cầu: \n"
                       "\t4. Thoát chương trình \n"
                       "\t   Lựa chọn của bạn là: "))
    if selOpt == 4:
        print("Chào tạm biệt")
        break
    elif selOpt != 4 and (selOpt > 4 or selOpt < 1):
        print("\nNOTE: Vui lòng nhập lại yêu cầu hoặc nhấn 4 để thoát chương trình !!!")
    else:
        Menu(selOpt)
