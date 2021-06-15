# Program Name: MenuDrivenProgram
# Author: Hoa Nguyen
# Data: June 12,2021
# Note: Chuong trinh nay co nhieu chuc nang de quan ly bong da

# Chia se mot file chung
# Chuc nang 1: Nhap
import json

import read_write_file
from matplotlib import pyplot as plt


def sel_opt_save(obj):
    switch_save_file = {
        1: "a",
        2: "w",
        3: "back"
    }
    return switch_save_file.get(obj, "Nothing")


def Nhap():
    print("<><><> Chào mừng bạn đến với chức năng nhập, ghi file <><><>")
    filename = 'venv/WorldCup2022.json'
    filesave = 'venv/data_after_processing'
    f = open(filename, "r", encoding="utf-8")
    data = json.loads(f.read())
    opt_save = int(input("Vui lòng lựa chọn chế độ dùng cho file: \n"
                         "\t1. Thêm dữ liệu vào file có sẵn     \n"
                         "\t2. Lưu dữ liệu đè lên file hiện tại \n"
                         "\t3. Quay về Menu                     \n"
                         "\t   Lựa chọn của bạn là: "))

    final_opt_save = sel_opt_save(opt_save)
    if final_opt_save == "back":
        return
    file_save = open(filesave, final_opt_save, encoding="utf-8")
    print("Tong so key trong table la:", len(data))
    for key in data:
        print("Key cua data la: ", key)
        file_save.write(key + "\n")
        for idx in data[key]:
            print("\nkey cua key la: %s " %idx)
            print(idx)
            file_save.write(str(idx) + "\n")

    return

# Chuc nang 2: Hoi dap


def HoiDap():
    print("<><><> Chuc nang hoi dap, doc file abc.txt de tra loi <><><>")
    return

# Chuc nang 3: Phan tich


def PhanTichDuLieu():
    print("<><><> Chuc nang phan tich, doc file abc.txt de tra loi <><><>")

    return


def Menu(select_opt):
    switcher = {
        1: Nhap,
        2: HoiDap,
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
