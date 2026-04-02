class HangHoa:
    def __init__(self, ma_hang, ten_hang, nha_sx ,gia):
        self.ma_hang = ma_hang
        self.ten_hang = ten_hang
        self.nha_sx =nha_sx
        self.gia = gia
    def __str__(self):
        return f"{self.ma_hang} - {self.ten_hang} - {self.nha_sx} - {self.gia}"
        
class HangDienMay(HangHoa):
    def __init__(self, ma_hang, ten_hang, nha_sx, gia, tg_baohanh, dien_ap, cong_suat):
        super().__init__(ma_hang, ten_hang, nha_sx, gia)  # 🔥 THÊM DÒNG NÀY
        self.tg_baohanh = tg_baohanh
        self.dien_ap = dien_ap
        self.cong_suat = cong_suat

    def __str__(self):
        return f"{self.ma_hang} - {self.ten_hang} - {self.nha_sx} - {self.gia} - {self.tg_baohanh} - {self.dien_ap} - {self.cong_suat}"
        
class HangSanhSu(HangHoa):
    def __init__(self, ma_hang, ten_hang, nha_sx, gia, loai_nguyenlieu):
        super().__init__(ma_hang, ten_hang, nha_sx, gia)
        self.loai_nguyenlieu = loai_nguyenlieu

    def __str__(self):
        return f"{self.ma_hang} - {self.ten_hang} - {self.nha_sx} - {self.gia} - {self.loai_nguyenlieu}"    
    
class HangThucPham(HangHoa):
    def __init__(self, ma_hang, ten_hang, nha_sx, gia, ngay_sx, ngay_hethan):
        super().__init__(ma_hang, ten_hang, nha_sx, gia)
        self.ngay_sx = ngay_sx
        self.ngay_hethan = ngay_hethan

    def __str__(self):
        return f"{self.ma_hang} - {self.ten_hang} - {self.nha_sx} - {self.gia} - {self.ngay_sx} - {self.ngay_hethan}"
    
    
a= HangHoa ("111", "Banh" , "Orino", 190 )
b= HangDienMay ("122", "Keo", "baby", 200 , "12ngay" , 200 , 120)
c= HangSanhSu ("119", "Chen" ,"Bat Trang" ,3000, "Su")
d=HangThucPham ("117" , "Banh" , "koko" , 10 , "12/1" , "22/4")
print (a)
print (b)
print(c)
print (d)