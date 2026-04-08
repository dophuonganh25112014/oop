from abc import ABC , abstractmethod
class GiaKhongHopLe(Exception):
    def __init__(self,gia):
        self.gia=gia
        super().__init__(f"Giá {gia} không hợp lệ")
        
class HangHoa(ABC):
    def __init__(self,ma ,ten ,nsx , gia):
        self.__ma , self.__ten , self.__nsx = ma , ten ,nsx
        self.gia = gia        
    @property
    def ma_hang(self): return self.__ma
    @property
    def ten_hang(self):
        return self.__ten
    @property
    def gia(self):
        return self.__gia
    @gia.setter 
    def gia(self, v):
        if v < 0 : raise GiaKhongHopLe(v)
        self.__gia =v
    @abstractmethod
    def loai_hang(self): pass
    def inTTin(self):
        return (f"[{self.loai_hang()}] {self.__ma} "
                f" | {self.__ten} | {self.__gia: ,.0f}đ")
    def __str__(self):return self.inTTin()
    def __eq__(self,o):return self.__ma==o.__ma 
    def __lt__(self,o): return self.__gia<o.__gia 
    def __hash__(self,o): return hash(self.__ma)
    def __repr__(self):
        return (f"{self.__class__.__name__}("
            f"ma='{self.__ma}',"
            f"ten='{self.__ten}',"
            f"gia={self.__gia})") 
class HangSanhSu(HangHoa):
    def __init__(self, ma, ten, nsx, gia, loai_nguyenlieu):
        self.loai_nguyenlieu = loai_nguyenlieu 
        super().__init__(ma,ten,nsx,gia)
    def loai_hang(self): return "Gốm Sứ Bát Tràng"
    def inTTin(self):
        return (f"{super().inTTin()}"
                f" | NL:{self.loai_nguyenlieu}")
class HangThucPham(HangHoa):
    def __init__(self, ma ,ten ,nsx,gia,ngay_sx, ngay_hethan):
        super().__init__(ma , ten ,nsx,gia)
        self.__ngay_sx , self.__ngay_hethan = ngay_sx , ngay_hethan 
    def loai_hang(self): return "Hàng thực phẩm"
    def ngay_sx(self): return "Hôm nay"
    def ngay_hethan(self): return "3 tháng sau khi mua"
    def inTTin(self):
        return (f"{super().inTTin()}"
                f" | NSX :{self.ngay_sx()}"
                f" | NHH :{self.ngay_hethan ()}")



class HangDienMay(HangHoa):
    def __init__(self,ma,ten,nsx,gia,bhanh,dap,cs):
        super().__init__(ma,ten,nsx,gia)
        self.__bhanh , self.__dap , self.__cs = bhanh , dap ,cs 
    def loai_hang(self):return "Điện Máy"
    def inTTin(self):
        return (f"{super().inTTin()}"
                f" | BH:{self.__bhanh} th"
                f" | {self.__dap}V | {self.__cs}W")
        
    #test
ds = [HangDienMay ("111", "Máy Lạnh " , "Panasonic", 12000000 ,24,222,150) , HangSanhSu (112, " Chén Ăn Cơm Cute " , 11, 12 , "Gôm bát tràng ")]

for sp in sorted (ds):
    print(sp)
    
with open("kho.txt" , "w", encoding ="utf -8") as f:
    for sp in ds:
        f.write(repr(sp)+ "\n")
        
    
