class CanBo:
    def __init__(self , ho_vaten, tuoi,gioi_tinh,dia_chi):
        self.ho_vaten= ho_vaten
        self.tuoi = tuoi
        self.gioi_tinh= gioi_tinh
        self.dia_chi = dia_chi
    def __str__(self):
        return f"{self.ho_vaten}-{self.tuoi}-{self.gioi_tinh}-{self.dia_chi}"
    
class CongNhan (CanBo):
    def __init__(self,ho_vaten, tuoi,gioi_tinh,dia_chi, bac):
        self.bac = bac
        super().__init__(ho_vaten, tuoi,gioi_tinh,dia_chi)
    def __str__(self):
        return f"{self.ho_vaten}-{self.tuoi}-{self.gioi_tinh}-{self.dia_chi}-{self.bac}"

class KySu (CanBo):
    def __init__(self , ho_vaten, tuoi,gioi_tinh,dia_chi, nganh_dao_tao):
        super().__init__(ho_vaten, tuoi,gioi_tinh,dia_chi)
        self.nganh_dao_tao = nganh_dao_tao
        
    
    def __str__(self):
        return f"{self.ho_vaten}-{self.tuoi}-{self.gioi_tinh}-{self.dia_chi}-{self.nganh_dao_tao}"
    
class NhanVien (CanBo):
    def __init__(self , ho_vaten, tuoi,gioi_tinh,dia_chi, cong_viec):
        super().__init__(ho_vaten, tuoi,gioi_tinh,dia_chi)
        self.cong_viec = cong_viec
        
    def __str__(self):
        return  f"{self.ho_vaten}-{self.tuoi}-{self.gioi_tinh}-{self.dia_chi} -{self.cong_viec}"
    
class QLCB:
    def __init__(self):
        self.danh_sach =[]
        
    def them_can_bo (self ,cb):
        self.danh_sach.append(cb)
        
    def tim_kiem (self ,ten):
        for cb in self.danh_sach:
            if ten.lower() in cb.ho_vaten.lower():
                print(cb)
            
    def hien_thi_nv (self):
        for cb in self.danh_sach:
            print(cb)
            

ql = QLCB()

while True:
    print("1.Thêm")
    print("2.Tìm")
    print("3.Hiển thị")
    print("4.Thoát")

    chon = input("Chọn: ")

    if chon == "1":
        loai = input("1.Công nhân 2.Kỹ sư 3.Nhân viên: ")
        ho_vaten = input("Họ tên: ")
        tuoi = int(input("Tuổi: "))
        gioi_tinh = input("Giới tính: ")
        dia_chi = input("Địa chỉ: ")

        if loai == "1":
            bac = int(input("Bậc: "))
            cb = CongNhan(ho_vaten, tuoi, gioi_tinh, dia_chi, bac)

        elif loai == "2":
            nganh = input("Ngành: ")
            cb = KySu(ho_vaten, tuoi, gioi_tinh, dia_chi, nganh)

        elif loai == "3":
            cv = input("Công việc: ")
            cb = NhanVien(ho_vaten, tuoi, gioi_tinh, dia_chi, cv)

        else:
            print("Loại không hợp lệ!")
            continue

        ql.them_can_bo(cb)

    elif chon == "2":
        ten = input("Nhập tên: ")
        ql.tim_kiem(ten)

    elif chon == "3":
        ql.hien_thi_nv()

    elif chon == "4":
        break

    else:
        print("Chọn sai!")