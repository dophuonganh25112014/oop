from abc import ABC, abstractmethod
class TuoiKhongHopLe(Exception):
    pass
class BacKhongHopLe(Exception):
    pass

class CanBo(ABC):
    def __init__(self , ho_vaten, tuoi,gioi_tinh,dia_chi):
        self.ho_vaten= ho_vaten
        self.tuoi = tuoi
        self.gioi_tinh= gioi_tinh
        self.dia_chi = dia_chi
    @property
    def tuoi(self):
        return self.__tuoi
    @tuoi.setter 
    def tuoi(self, value):
        if value <18 or value >65:
            raise TuoiKhongHopLe("Tuổi phải từ 18-65")
        self.__tuoi = value
    @abstractmethod
    def mo_ta(self):
        pass
    def __str__(self):
        return self.__str__()
    def __repr__(self):
        return f"{self.__class__.__name__ }('{self.ho_vaten}', {self.tuoi},'{self.gioi_tinh}','{self.dia_chi}')"
    def __eq__(self,other):
        return self.ho_vaten == other.ho_vaten and self.tuoi == other.tuoi
    def __lt__(self, other):
        return self.ho_vaten < other.ho_vaten
    
    
    
class CongNhan (CanBo):
    def __init__(self,ho_vaten, tuoi,gioi_tinh,dia_chi, bac):
        self.bac = bac
        super().__init__(ho_vaten, tuoi,gioi_tinh,dia_chi)
    @property
    def bac(self):
        return self.__bac 
    @bac.setter 
    def bac (self,value):
        if value <1 or value >10:
            raise BacKhongHopLe("Bậc phải từ 1-10")
        self.__bac = value 
    def mo_ta(self):
        return f"Công nhân - bậc {self.bac}"
    def __repr__(self):
        return f"CongNhan('{self.ho_vaten}' , {self.tuoi},'{self.gioi_tinh}' , '{self.dia_chi}', {self.bac})" 
      

class KySu (CanBo):
    def __init__(self , ho_vaten, tuoi,gioi_tinh,dia_chi, nganh_dao_tao):
        super().__init__(ho_vaten, tuoi,gioi_tinh,dia_chi)
        self.nganh_dao_tao = nganh_dao_tao
    def mo_ta(self):
        return f"Kỹ sư - ngành {self.nganh_dao_tao}"
      
    
    def __repr__(self):
        return f"KySu ('{self.ho_vaten}',{self.tuoi},'{self.gioi_tinh}','{self.dia_chi}','{self.nganh_dao_tao}')"
    
class NhanVien (CanBo):
    def __init__(self , ho_vaten, tuoi,gioi_tinh,dia_chi, cong_viec):
        super().__init__(ho_vaten, tuoi,gioi_tinh,dia_chi)
        self.cong_viec = cong_viec
    def mo_ta(self):
        return f"Nhân viên - {self.cong_viec}"
        
    def __repr__(self):
        return  f"NhanVien('{self.ho_vaten}',{self.tuoi},'{self.gioi_tinh}','{self.dia_chi}','{self.cong_viec}')"
    
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

    def luu_file(self):
        with open("canbo.txt","w", encoding="utf-8") as f:
            for cb in self.danh_sach:
                f.write(repr(cb)+ "\n")
    def doc_file(self):
        
        try:
            with open("canbo.txt", "r", encoding="utf-8") as f:
                for line in f:
                    cb = eval(line.strip())
                    self.them_can_bo(cb)
        except FileNotFoundError:
           print("Chưa có file!")
                            

ql = QLCB()
ql.doc_file()

while True:
    print("\n1.Thêm")
    print("2.Tìm")
    print("3.Hiển thị")
    print("4.Lưu File")
    print("5.Thoát")

    chon = input("Chọn: ")
    try:
        if chon == "1":
            loai = input("1.Công nhân 2.Kỹ sư 3.Nhân viên: ")
            ten = input("Họ tên: ")
            tuoi = int(input("Tuổi: "))
            gt = input("Giới tính: ")
            dc = input("Địa chỉ: ")

            if loai == "1":
                bac = int(input("Bậc: "))
                cb = CongNhan(ten, tuoi, gt, dc, bac)

            elif loai == "2":
                nganh = input("Ngành: ")
                cb = KySu(ten, tuoi, gt, dc, nganh)

            elif loai == "3":
                cv = input("Công việc: ")
                cb = NhanVien(ten, tuoi, gt, dc, cv)

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
            ql.luu_file()
            print("Đã lưu!!")
        elif chon =="5":
            break

        else:
            print("Chọn sai!")
    except Exception  as e:
        print("Lỗi : ", e)