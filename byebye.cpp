#include <iostream>
#include <list>
#include <string>
using namespace std;
class ChuyenBay {
public:
    string ma;
    string khoiHanh;
    string den;
    int giaVe;

    ChuyenBay() {}

    ChuyenBay(string m, string kh, string d, int g) {
        ma = m;
        khoiHanh = kh;
        den = d;
        giaVe = g;
    }

    void nhap() {
        cout << "Nhap ma chuyen bay: ";
        cin >> ma;
        cin.ignore();

        cout << "Nhap noi khoi hanh: ";
        getline(cin, khoiHanh);

        cout << "Nhap noi den: ";
        getline(cin, den);

        cout << "Nhap gia ve: ";
        cin >> giaVe;
    }

    void hienThi() {
        cout << ma << " | "
             << khoiHanh << " -> "
             << den << " | "
             << giaVe << " VND\n";
    }
};

int main() {
    
    list<ChuyenBay> ds = {
        ChuyenBay("VN101", "Ha Noi", "TP.HCM", 1500000),
        ChuyenBay("VN202", "Da Nang", "Ha Noi", 1200000),
        ChuyenBay("VN303", "TP.HCM", "Phu Quoc", 1700000),
        ChuyenBay("VN404", "Can Tho", "Da Lat", 1100000),
        ChuyenBay("VN505", "Hai Phong", "Nha Trang", 1600000)
    };

    int chon; 

    do {
        cout << "\n===== MENU =====\n";
        cout << "1. Nhap du lieu (them chuyen bay)\n";
        cout << "2. Hien thi tat ca chuyen bay\n";
        cout << "3. Tim chuyen bay theo ma\n";
        cout << "4. Chuyen bay co gia ve cao nhat\n";
        cout << "5. Chuyen bay co gia ve thap nhat\n";
        cout << "0. Thoat\n";
        cout << "Chon: ";
        cin >> chon;

       
        if (chon == 1) {
            ChuyenBay cb;
            cb.nhap();
            ds.push_back(cb);
            cout << "Da them chuyen bay!\n";
        }

    
        else if (chon == 2) {
            for (ChuyenBay cb : ds)
                cb.hienThi();
        }

        else if (chon == 3) {
            string ma;
            cout << "Nhap ma can tim: ";
            cin >> ma;

            bool found = false; 
            for (ChuyenBay cb : ds) {
                if (cb.ma == ma) {
                    cb.hienThi();
                    found = true;
                }
            }

            if (!found)
                cout << "Khong tim thay chuyen bay!\n";
        }
        else if (chon == 4) {
            ChuyenBay max = *ds.begin();
            for (ChuyenBay cb : ds)
                if (cb.giaVe > max.giaVe)
                    max = cb;

            cout << "Chuyen bay co gia ve cao nhat:\n";
            max.hienThi();
        }

        else if (chon == 5) {
            ChuyenBay min = *ds.begin();
            for (ChuyenBay cb : ds)
                if (cb.giaVe < min.giaVe)
                    min = cb;

            cout << "Chuyen bay co gia ve thap nhat:\n";
            min.hienThi();
        }

    } while (chon != 0);

    return 0;
}