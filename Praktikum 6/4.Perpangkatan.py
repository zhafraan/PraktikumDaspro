# Nama File   = 4.Perpangkatan.py
# Nama        = Aqiatillah Rezi Zhafran
# NIM         = 24060124140124
# Tanggal     = 4 Oktober 2024
# Deskripsi   = membuat ekspresi rekursif operasi perpangkatan 

#DEFINISI DAN SPESIFIKASI
# Perpangkatan: 2 integer >= 0 --> integer >0
#   {Perpangkatan(x,y) adalah  untuk menghitung perpangakatan dengan mengalikan input x dikali sebanyak y dengan menggunakan ekspresi rekursif}

# REALISASI
def Perpangkatan(x,y):
    if y == 0:
        return 1
    else:
        return x * Perpangkatan(x,y-1)
    
# APLIKASI 
print(Perpangkatan(2,0))
print(Perpangkatan(5,5))
print(Perpangkatan(5,3))