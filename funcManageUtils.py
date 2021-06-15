import json


def append_file():
    return "a"


def overwrite_file():
    return "w"


def return_back():
    return "back"


def sel_opt_save(obj):
    if obj not in range(1, 3):
        print("Your input is wrong, please select again")
        return return_back()

    switch_save_file = {
        1: append_file(),
        2: overwrite_file(),
        3: return_back()
    }
    return switch_save_file.get(obj, "Your input is wrong")


def input_option(filename, filesave):
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
            print("\nkey cua key la: %s " % idx)
            print(idx)
            file_save.write(str(idx) + "\n")


def question_answer(obj):

    return