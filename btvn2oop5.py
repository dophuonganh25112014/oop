class NhanVien:
    def __init__(self , ma_nv , ho_vaten, nam_sinh, gioi_tinh, dia_chi , he_so_luong , luong_toi_da):
        self.ma_nv = ma_nv
        self.ho_vaten = ho_vaten
        self.nam_sinh = nam_sinh
        self.gioi_tinh =gioi_tinh
        self.dia_chi= dia_chi
        self.he_so_luong = he_so_luong 
        self.luong_toi_da= luong_toi_da
    def tinh_luong(self):
        return self.he_so_luong * self.luong_toi_da
    
    def __str__(self):
        return f"{self.ma_nv} - {self.ho_vaten} - {self.tinh_luong()}"
    
class CongTacVien (NhanVien):
    def __init__(self , ma_nv , ho_vaten, nam_sinh, gioi_tinh, dia_chi , he_so_luong , luong_toi_da,thoi_han_hop_dong, phu_cap ):
        super().__init__(ma_nv, ho_vaten, nam_sinh, gioi_tinh, dia_chi, he_so_luong, luong_toi_da)
        self.thoi_han_hop_dong = thoi_han_hop_dong
        self.phu_cap = phu_cap
    def tinh_luong(self):
        return super().tinh_luong() + self.phuc_cap
    def __str__(self):
        return f"{self.ma_nv}- {self.ho_vaten} -{self.nam_sinh} -{self.gioi_tinh} -{self.dia_chi}-{self.he_so_luong} -{self.luong_toi_da} -{self.thoi_han_hop_dong} -{self.phu_cap}"
    
class NhanVienChinhThuc (NhanVien):
    def __init__(self , ma_nv , ho_vaten, nam_sinh, gioi_tinh, dia_chi , he_so_luong , luong_toi_da, thong_tin_cong_viec):
        super().__init__(ma_nv, ho_vaten, nam_sinh, gioi_tinh, dia_chi, he_so_luong, luong_toi_da)
        self.thong_tin_cong_viec = thong_tin_cong_viec
    def tinh_luong (self):
        return super().tinh_luong()
    def __str__(self):
        return f"{self.ma_nv}- {self.ho_vaten} -{self.nam_sinh} -{self.gioi_tinh} -{self.dia_chi}-{self.he_so_luong} -{self.luong_toi_da} -{self.thong_tin_cong_viec}"
    
class TruongPhong (NhanVien):
    def __init__(self , ma_nv , ho_vaten, nam_sinh, gioi_tinh, dia_chi , he_so_luong , luong_toi_da, tro_cap_quan_ly):
        super().__init__(ma_nv, ho_vaten, nam_sinh, gioi_tinh, dia_chi, he_so_luong, luong_toi_da)
        self.tro_cap_quan_ly = tro_cap_quan_ly
    def tinh_luong(self):
        return super().tinh_luong() + self.tro_cap_quan_ly
    def __str__(self):
          return f"{self.ma_nv} - {self.ho_vaten} - {self.tro_cap_quan_ly}-{self.tinh_luong()}"
        
        
a= NhanVien ("011", "Nguyễn Văn A" , "2000" ,"Nam" ,"Hà Nội " , 3 , 21000000)
b= CongTacVien ("003", "Nguyễn Thị B" , 2002 ,"Nữ" ,"Hải Phòng" ,4,21000000 , "3 tháng", 300000)   
c= NhanVienChinhThuc ("005", "Alex Cunning Ham" , "1990","Nam" ,"NewYork" ,5 ,30000000, "Coder")
d= TruongPhong ("112" ,"Nguyễn Ánh Sáng " , 1998, "Nữ", "Hà Nội " ,4 , 30000000 , 500000)
print (a)
print(b)
print(c)
print(d)