# Nama File   = 3.Pembagian.py
# Nama        = Aqiatillah Rezi Zhafran 
# NIM         = 24060124140124
# Tanggal     = 4 Oktober 2024
# Deskripsi   = membuat ekspresi rekursif operasi pembagian

# DEFINISI DAN SPESIFIKASI
# Pembagian : integer > 0,integer > 0 --> real >0
#   {Pembagian(x,y)adalah untuk menghitung pembagian antara input x dibagi y  dengan menggunakan ekspresi rekursif}

# REALISASI
def Div(x,y):
    if y == 1:
        return x
    else:
        return (Div(x,y-1)) / y
 
# APLIKASI
print(Div(5,3))
print(Div(2,1))
print(Div(6,2))



