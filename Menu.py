### Program Name: MenuDrivenProgram
### Author: Hoa Nguyen
### Data: June 12,2021
### Note: Chuong trinh nay co nhieu chuc nang de quan ly bong da

### Chia se mot file chung
### Chuc nang 1: Nhap



def Nhap():
    print("Chuc nang nhap, ghi file abc.txt")
    return

### Chuc nang 2: Hoi dap
def HoiDap():
    print("Chuc nang hoi dap, doc file abc.txt de tra loi")
    return

### Chuc nang 3: Phan tich
def PhanTichDuLieu():
    print("Chuc nang phan tich, doc file abc.txt de tra loi")
    return

def Menu(chon):
        switcher = {
            1: Nhap,
            2: HoiDap,
            3: PhanTichDuLieu
        }

        func = switcher.get(chon, lambda: "Du lieu sai")

        func()

while(True):
    print("")
    chon = int(input("Cho chuc nang 0, hay lon hon 3 de ket thuc"))
    if chon <= 0 or chon > 3:
        print("Chao tam biet")
        break
    Menu(chon)
