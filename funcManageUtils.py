import json
import datetime as dt
from pathlib import Path
import os

time_zone = dt.datetime.now()


def fname():  # Tạo tên file là file_recored_<current_Time>
    current_time = (time_zone.strftime("%X")).replace(":", ".")
    time_file = time_zone.strftime("_%d-" + "%m-" + "%y_" + current_time)
    f_name = "file_recorded" + time_file
    ext = ".txt"
    path_file = f_name + ext

    return path_file


def write_file(write=True):  # Trường hợp chạy user muốn tạo file mới, update time trước khi tạo file mới
    if write:
        time_zone = dt.datetime.now()
        return "w+"
    return "w"


def append_file():
    return "a"


def read_file():
    return "r"


def return_back():
    return True


def open_file(file_path, opt_save):
    file_save = open(file_path, opt_save, encoding="utf-8")
    return file_save


def sel_opt_save(mode):
    switch_save_file = {
        1: write_file(write=True),
        2: append_file(),
        3: write_file(write=False),
        4: return_back()
    }
    return switch_save_file.get(mode, "Your input is wrong")


def remove_last_line(file_path):
    rd_file = open_file(file_path, "r")
    lines = rd_file.readlines()
    rd_file.close()
    wr_file = open(file_path, "w", encoding="utf-8")
    wr_file.writelines([item for item in lines[:-1]])
    wr_file.close()


def common_input(file_save, file_path, my_path):
    i = 0
    while True:
        if i == 0:
            print("\n\tNhập ở đây, nhấn q để thoát")
        usr_in = input("\tInput: ")
        file_save.writelines(usr_in)
        if usr_in == "q":
            usr_save = input("\n\tBạn muốn lưu file vừa tạo, nhấn Y?\n"
                             "\tNhấn phím Y hoặc N để thoát\n"
                             "\tNhấn phím bất kỳ để tiếp tục\n"
                             "\tLựa chọn của bạn là: "
                             )
            if usr_save in ["N", "Y"]:
                file_path = my_path / file_path
                file_save.close()
                remove_last_line(file_path)
                if os.path.exists(file_path) and usr_save == "N":
                    os.remove(file_path)
                    file_path = None
                break
            continue

        file_save.writelines("\n")
        i += 1


def inputandwr(databasename):
    fdatabase = open(databasename, "r", encoding="utf-8")
    data = json.loads(fdatabase.read())
    my_path = Path().absolute()
    file_name = None

    while True:
        opt_save = int(input("\n**** Vui lòng lựa chọn chế độ dùng cho file: \n"
                             "\t1. Tạo file log mới                          \n"
                             "\t2. Thêm dữ liệu vào file log có sẵn          \n"
                             "\t3. Ghi đè dữ liệu lên file log có sẵn        \n"
                             "\t4. Quay về Menu                              \n"
                             "\t   Lựa chọn của bạn là: "
                             ))

        if opt_save not in range(1, 5):
            print("\tNote: Vui lòng nhập lại hoặc nhấn 4 để quay về Menu")
        else:
            final_opt_save = sel_opt_save(opt_save)

        if final_opt_save in ["w", "w+"] and opt_save != 3:
            file_path = fname()
            file_save = open_file(file_path, final_opt_save)
            common_input(file_save, file_path, my_path)

        elif final_opt_save == "a" or opt_save == 3:
            file_name = input("Vui lòng nhập tên file cần thêm hoặc ghi đè dữ liệu: ")
            if file_name is None or file_name == "" or len(file_name) <= 0:
                return
            file_path = my_path / file_name
            file_save = open_file(file_path, final_opt_save)
            common_input(file_save, file_path, my_path)

        else:
            return

        if file_path == None:
            print("Không create file vì bạn đã chọn xóa file đã tạo")
        else:
            file_save.close()
        print(f'Đường dẫn của file: {file_path}')
        fdatabase.close()


def sel_opt_qanda(obj):
    if obj not in range(1, 5):
        print("Your input is wrong, please select again")
        return return_back()

    switch_save_file = {
        1: append_file(),
        2: overwrite_file(),
        3: return_back()
    }
    return switch_save_file.get(obj, "Your input is wrong")


def qanda(obj):
    int(input("\nVui lòng lựa chọn chế độ dùng cho file: \n"
              "\t1.Có bao nhiều đội bóng tham dự World Cup 2022? \n"
              "\t2.Có bao nhiêu chương trình TV trực tiếp khi đội tuyển Việt Nam và Malaysia thi đấu? \n"
              "\t3.Có bao nhiêu sân vận động có sức chứa trên 20000 người? \n"
              "\t4.Sân vận động nào được dùng tổ chức trận việt nam và indo, và có sức chứa bao nhiêu? \n"
              "\t5.Có bao nhiêu đội bóng ở bảng G có cầu thủ tuổi lớn hơn 23 và là tiền vệ? \n"
              ))
    # case1
    switch()
    return


def read_file(fname):
    outfile = open(fname, 'r', encoding="utf-8")
    # do something
    outfile.close()
    return
