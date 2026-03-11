# Nama File   = 1.Pengurangan.py
# Nama        = Aqiatillah Rezi Zhafran
# NIM         = 24060124140124
# Tanggal     = 4 Oktober 2024
# Deskripsi   = Membuat fungsi rekursif operasi pengurangan

#DEFINISI DAN SPESIFIKASI
#Pengurangan : integer > 0,Integer > 0 --> integer 
#   {Pengurangan(x,y)adalah untuk menghitung pengurangan antara input x dan y  dengan menggunakan ekspresi rekursif}

# REALISASI
def Pengurangan(x, y):
    if y == 0:    
        return x
    else: 
        return Pengurangan(x, y-1) - 1
    
# APLIKASI 
print(Pengurangan(4,4))
print(Pengurangan(18,9))
print(Pengurangan(9,2))