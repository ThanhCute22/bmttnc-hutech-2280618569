so_gio_lam = float(input("nhap so gio lam moi tuan: "))
muc_luong = float(input("nhap thu lao tren gio lam tieu chuan: "))
gio_tieu_chuan = 44
gio_vuot_chuan = max(0, so_gio_lam - gio_tieu_chuan)
thuc_lanh = gio_tieu_chuan * muc_luong + gio_vuot_chuan * muc_luong * 1.5
print(f'so tien thuc linh cua nhan vien: {thuc_lanh}')