class NhanVien:
    LUONG_MAX = 20000000   # lương tối đa ( tự điều chỉnh)
    #lương max là thuộc tính chung vì nhân viên nào cx có lương max như nhau

    def __init__(self, tenNhanVien, luongCoBan, heSoLuong): #def __init__ là hàm khởi tạo , dùng để tạo object,
        #gắn giá trị ban đầu cho thuộc tính 
        self.tenNhanVien = tenNhanVien # gán tạo thuộc tính cho object , object trog bài là : NhanVien
        self.luongCoBan = luongCoBan  # self là tham chiếu đối tượng , self = với object trong bài
        self.heSoLuong = heSoLuong

    # tính lương
    def tinhLuong(self): # hàm tính lương 
        return self.luongCoBan * self.heSoLuong # hàm chạy return trả kết quả và gán vào biến luong

    # tăng lương 
    def tangLuong(self, x): # hàm tăng lương thêm x nhưng k đc vượt mức max
        heSoMoi = self.heSoLuong + x
        luongMoi = self.luongCoBan * heSoMoi

        if luongMoi > NhanVien.LUONG_MAX: # lương mới lớn hơn object.thuộc tính
            print("Luong vuot qua muc cho phep!") 
            return False # trả về giá trị false
        else: # nếu ko vượt mức
            self.heSoLuong = heSoMoi # trả về hệ số mới
            return True # trả về true

    # in thông tin
    def inTTin(self):
        print("Ten:", self.tenNhanVien)
        print("Luong co ban:", self.luongCoBan)
        print("He so luong:", self.heSoLuong)
        print("Luong:", self.tinhLuong()) 

    # getter & setter
    def getTen(self): #lấy tenNhanVien của object trả ra ngoài bằng return 
        return self.tenNhanVien

    def setTen(self, ten): # hàm dùng đổi tên nhân viên
        self.tenNhanVien = ten 

    def getLuongCoBan(self): 
        return self.luongCoBan

    def setLuongCoBan(self, lcb): # thay đổi lg cơ bản 
        self.luongCoBan = lcb

    def getHeSoLuong(self):
        return self.heSoLuong

    def setHeSoLuong(self, hsl): # thay đổi hệ số lg
        self.heSoLuong = hsl


# test 
an = NhanVien("An", 2000000, 3) # ( tên , lg cơ bản , hệ số lương)
an.inTTin()

print("\nTang luong:")
print(an.tangLuong(2))   # thử tăng hệ số lương của an ban đầu là 3 tăng thêm 2 thì tổng là tăng gấp 5

an.inTTin() 

print ("===========")
may = NhanVien("May",2000000,4)
may.tangLuong(1)
may.inTTin()

