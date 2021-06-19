import json
import datetime as dt
from pathlib import Path
import os

time_zone = dt.datetime.now()  # Get thời gian thực


def fname():  # Hàm tạo tên file là file_recored_<current_Time>
    current_time = (time_zone.strftime("%X")).replace(":", ".")
    time_file = time_zone.strftime("_%d-" + "%m-" + "%y_" + current_time)
    f_name = "file_recorded" + time_file
    ext = ".txt"
    path_file = f_name + ext

    return path_file


def write_file(write=True):
    if write:  # Trường hợp user muốn tạo file mới, update time trước khi tạo file mới
        time_zone = dt.datetime.now()
        return "w+"  # Dùng lệnh w+ để có thể read nếu cần
    return "w"


def append_file():
    return "a"


def read_file():
    return "r"


def return_back():
    return False


def sel_opt_save(mode):
    switch_save_file = {
        1: write_file(write=True),
        2: append_file(),
        3: write_file(write=False),
    }
    return switch_save_file.get(mode, "Your input is wrong")


def remove_last_line(file_path):
    rd_file = open(file_path, "r", encoding='utf-8')
    lines = rd_file.readlines()
    rd_file.close()
    wr_file = open(file_path, "w", encoding="utf-8")
    wr_file.writelines([item for item in lines[:-1]])
    wr_file.close()


def common_input_exit(file_save, file_path):
    my_path = Path().absolute()
    i = 0

    while True:
        if i == 0:
            print("\n\tNhập ở đây, nhấn q để thoát")

        usr_in = input("\tInput: ")

        if usr_in == "q":
            usr_save = input("\n\tBạn có chắc chắn muốn lưu file vừa tạo, nhấn Y?\n"
                             "\tNhấn phím Y hoặc N để thoát\n"
                             "\tNhấn phím bất kỳ để tiếp tục\n"
                             "\tLựa chọn của bạn là: "
                             )
            if usr_save in ["N", "Y"]:
                file_path = my_path / file_path
                file_save.close()
                # remove_last_line(file_path)
                if os.path.exists(file_path) and usr_save == "N":
                    os.remove(file_path)
                    file_path = None
                break
            continue
        else:
            file_save.writelines(usr_in)

        file_save.writelines("\n")
        i += 1

    return file_path


def answer_question(file_save, value=None, data=None):
    if value is None or data is None:
        return
    result  = 0
    if value == 1:  # 1. Có bao nhiều đội bóng tham dự World Cup 2022?
        file_save.write('\n1. Có bao nhiều đội bóng tham dự World Cup 2022?')
        for key in data['teams']:
            result += 1
    elif value == 2:  # 2. Có bao nhiêu chương trình tv trực tiếp ở Việt Nam và Singapore
        file_save.write('\n2. Có bao nhiêu chương trình tv trực tiếp ở Việt Nam và Singapore')
        for key in data['tvchannels']:
            if key['country'] == 'VietNam' or key['country'] == 'Singapore':
                result += 1
    elif value == 3:  # 3. Liệt kê sân vận động nào có sức chứa trên 20000 người?
        file_save.write('\n3. Liệt kê sân vận động nào có sức chứa trên 20000 người?')
        result = []
        for key in data['stadiums']:
            if key['capacity'] > 20000:
                result.append(key['name'])
    else:
        result = None

    return result


def common_qanda_exit(file_save, file_path, value=None, data=None):
    my_path = Path().absolute()
    if value is None or data is None:
        return

    result = answer_question(file_save, value, data)
    if result is not None:
        print('Đã trả lời xong')
        if isinstance(result, list):
            usr_in = "\nKết quả của câu hỏi là: " + str(result)[1:-1]
        else:
            usr_in = "\nKết quả của câu hỏi là: " + str(result)
        file_save.writelines(usr_in)
    else:
        return

    usr_in = input("\n\tNhấn q để thoát, anykey để tiếp tục: ")
    usr_save = ""
    if usr_in == "q":
        usr_save = input("\n\tBạn có chắc chắn muốn lưu file vừa tạo, nhấn Y?\n"
                         "\tNhấn phím Y hoặc N để thoát\n"
                         "\tNhấn phím bất kỳ để tiếp tục\n"
                         "\tLựa chọn của bạn là: "
                         )
        if usr_save in ["N", "Y"]:  # Nếu chọn Yes hoặc No, đều quay ngược lại Menu trước đó
            file_path = my_path / file_path  #  Tạo đường dẫn file
            file_save.close()  # Đóng file
            # remove_last_line(file_path)
            if os.path.exists(file_path) and usr_save == "N":  # Nếu chọn No thì không lưu file
                                                               # và remove đường dẫn file đã khởi tạo
                os.remove(file_path)
                file_path = None
            return file_path

    else:
        file_save.writelines("\n")

    return file_path


def common_sel_opt_save():
    final_opt_save  = None
    file_path       = None
    my_path         = Path().absolute()  # Lấy đường dẫn file hiện tại

    opt_save = int(input("\n\t**** Vui lòng lựa chọn chế độ dùng cho file:"
                         "\n\t1. Tạo file log mới"
                         "\n\t2. Thêm dữ liệu vào file log có sẵn"
                         "\n\t3. Ghi đè dữ liệu lên file log có sẵn"
                         "\n\t4. Quay về Menu"
                         "\n\t   Lựa chọn của bạn là: "
                         ))

    if opt_save not in range(1, 5):
        print("\tNote: Vui lòng nhập lại hoặc nhấn 4 để quay về Menu")
    else:
        if opt_save == 4:
            return final_opt_save, opt_save, file_path
        final_opt_save = sel_opt_save(opt_save)

    if final_opt_save in ["w", "w+"] and opt_save != 3:  # Điều kiện khi lưu file khi tạo file mới
        file_path = fname()
    elif final_opt_save == "a" or opt_save == 3:  # Điều kiện lưu file khi thêm hoặc ghi đè dữ liệu
        file_name = input("Vui lòng nhập tên file cần thêm hoặc ghi đè dữ liệu: ")
        if file_name is None or file_name == "" or len(file_name) <= 0:
            return final_opt_save, opt_save, file_path
        file_path = my_path / file_name  # Đường dẫn file, full path
    else:
        return final_opt_save, opt_save, file_path

    return final_opt_save, opt_save, file_path


def input_data(dbname):
    while True:
        final_opt_save, opt_save, file_path = common_sel_opt_save()  # Hàm chọn chức năng save data
        if final_opt_save is None or final_opt_save is True or file_path is None:
            return

        file_save = open(file_path, final_opt_save, encoding="utf-8")  # Mở file

        file_path = common_input_exit(file_save, file_path)  # Điều kiện nhập và thoát khi đã nhập xong

        if file_path is None:  # Trường hợp không muốn tạo file thì in ra không có file
            print("Không create file vì bạn đã chọn xóa file đã tạo")
        else:
            file_save.close()
        print(f'Đường dẫn của file: {file_path}')  # In ra đường dẫn của file


def input_qanda(dbname):
    fdb = open(dbname, "r", encoding="utf-8")
    data = json.loads(fdb.read())
    final_opt_save, opt_save, file_path = common_sel_opt_save()  # Hàm chọn chức năng save data
    if opt_save == 4:
        return

    file_save = open(file_path, final_opt_save, encoding="utf-8")  # Mở file với lựa chọn user mong muốn

    while True:
        if final_opt_save is None or final_opt_save is True:
            break
        usr_input = int(input("\n\t**** Vui lòng lựa chọn câu hỏi:"
                              "\n\t1. Có bao nhiều đội bóng tham dự World Cup 2022?"
                              "\n\t2. Có bao nhiêu chương trình TV trực tiếp đội tuyển Việt Nam và Malaysia thi đấu?"
                              "\n\t3. Có bao nhiêu sân vận động có sức chứa trên 20000 người?"
                              "\n\t4. Quay về Menu"
                              "\n\t   Lựa chọn của bạn là: "
                              ))

        if usr_input == 4:
            break

        file_path = common_qanda_exit(file_save, file_path, usr_input, data)  # Trả lời câu hỏi và kết thúc
        if file_path is None:  # Trường hợp không muốn tạo file hoặc exit ngay từ đầu thì in ra không có file
            print("Không create file")

    if file_save is not None:
        file_save.close()

    print(f'Đường dẫn của file: {file_path}')  # In ra đường dẫn của file
    fdb.close()


def read_file(fname):
    outfile = open(fname, 'r', encoding="utf-8")
    # do something
    outfile.close()
    return
