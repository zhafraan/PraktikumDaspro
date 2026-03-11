# Nama File   = 2.Perkalian.py
# Nama        = Aqiatillah Rezi Zhafran
# NIM         = 24060124140124
# Tanggal     = 4 Oktober 2024
# Deskripsi   = membuat fungsi rekursif operasi perkalian

# DEFINISI DAN SPESIFIKASI
# Perkalian : integer >=0,integer >= 0 --> integer >=0
#   {Perkalian(x,y)adalah untuk menghitung perkalian antara input x dan y dengan menggunakan ekspresi rekursif}

# REALISASI
def Perkalian(x,y):
    if x == 0:
        return 0    
    else:  
        return y + Perkalian(x-1,y)
# APLIKASI
print(Perkalian(5,0))
print(Perkalian(7,3))
print(Perkalian(5,4))