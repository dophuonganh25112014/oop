from math import gcd
class MauSoBangKhong (Exception):
    pass
class PhanSo:
    def __init__(self, mau_so,tu_so):
        if mau_so ==0:
            raise MauSoBangKhong("Mẫu số không được bằng 0")
        self.tu_so = tu_so
        self.mau_so = mau_so
    def toi_gian(self):
        g = gcd(  self.tu_so ,self.mau_so )
        return PhanSo( self.tu_so // g , self.mau_so // g)
    def is_toi_gian(self):
        return gcd(self.tu_so , self.mau_so) ==1
    def __add__(self, other):
        tu=self.tu_so * other.mau_so + other.tu_so *self.mau_so
        mau= self.mau_so*other.mau_so
        return PhanSo(tu, mau).toi_gian()
    def __sub__(self, other):
        tu= self.tu_so * other.mau_so - other.tu_so*self.mau_so
        mau= self.mau_so*other.mau_so
        return PhanSo(tu, mau).toi_gian()
    def __mul__(self, other):
        return PhanSo( self.tu_so * other.tu_so , self.mau_so*other.mau_so).toi_gian()
    def __trudiv__(self, other):
        return PhanSo(self.tu_so*other.mau_so , self.mau_so * other.tu_so).toi_gian()
    def __eq__(self , other):
        return self.tu_so* other.mau_so == other.tu_so* self.mau_so
    def __lt__(self, other):
        return self.tu_so*other.mau_so < other.tu_so*self.mau_so
    def __gt__(self,other):
        return self.tu_so* other.mau_so > other.tu_so * self.mau_so
    def __str__(self):
        if self.mau_so ==1:
            return str(self.tu_so)
        return f"{self.tu_so}/ {self.mau_so}"
ds =[]
n=int(input("Nhập số lương phân số vào danh sách :"))
for i in range(n):
    tu = int(input("Tử: "))
    mau=int(input("Mẫu: "))
    ps=PhanSo (tu,mau)
    ds.append(ps)
print("\n Dạng tối giản:")
for ps in ds:
    print(ps.toi_gian())
ds_sorted= sorted(ds)
print("\n Sau khi sắp xếp:")
for ps in ds_sorted:
    print(ps.toi_gian())