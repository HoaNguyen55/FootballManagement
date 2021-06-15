# Chuong trinh ghi, doc file voi du lieu List va sap xep List
# Date: June 12,2021
# Author: Hoa Nguyen

# ghi file vào tệp tin đã tạo
def ghifile():
    filenamewrite = "venv/WorldCup2022.json"
    filewrite     = open(filenamewrite, "w", encoding="utf-8")
    StudentList=["Anh","Sơn","Phúc","Kha","Linh"]
    for ten in StudentList:
        filewrite.write(ten+"\n") ## dau xuong dong
    filewrite.close()

# Xóa dấu xuống dòng
def remove_new_line():
    filenameread = "data/DanhSachLop.txt"
    StudentListNew = []
    with open(filenameread, encoding="utf-8") as f:
        for line in f:
            line = line.replace("\n", "")
            StudentListNew.append(line)

def read_file_sort():
    print("Hien thi danh sach da doc tu file va sap xep lai")
    StudentListNewSort = sorted(StudentListNew, reverse=False)
    Stt = 1
    for ten in StudentListNewSort:
        print(Stt, ":", ten)
        Stt += 1