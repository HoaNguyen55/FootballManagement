# Program Name: MenuDrivenProgram
# Author: Hoa Nguyen
# Data: June 12,2021
# Note: Chuong trinh nay co nhieu chuc nang de quan ly bong da

# Chia se mot file chung

import json
import funcManageUtils as fmUtils
import matplotlib.pyplot as plt

# Chuc nang 1: Nhap
filename = 'venv/WorldCup2022.json'
filesave = 'venv/data_after_processing'


def NhapVaGhi():
    print("<><><> Chào mừng bạn đến với chức năng Nhập yêu cầu và ghi file <><><>")
    fmUtils.inputandwr(filename, filesave)
    return

# Chuc nang 2: Hoi dap


def HoiVaDap():
    print("<><><> Chào mừng bạn đến với chức năng Hỏi và Đáp <><><>")
    fmUtils.qanda(filename)
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
    print("")
    selOpt = int(input("Vui lòng chọn các yêu cầu sau: \n"
                       "\t1. Nhập dữ liệu  \n"
                       "\t2. Hỏi và đáp    \n"
                       "\t3. Phân tích dữ liệu theo yêu cầu: \n"
                       "\t4. Thoát chương trình \n"
                       "\t   Lựa chọn của bạn là: "))
    if selOpt <= 0 or selOpt > 3:
        print("Chào tạm biệt")
        break
    Menu(selOpt)
