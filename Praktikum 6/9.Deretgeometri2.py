# Nama File   = 9.Deretgeometri2.py
# Nama        = Aqiatillah Rezi Zhafran
# NIM         = 24060124140124
# Tanggal     = 5 Oktober 2024
# Deskripsi   = menghitung deret geometri menggunakan ekspresi rekursif

# DEFINISI DAN SPESIFIKASI
# geometric2 : integer > 0 -> integer
#   {geometric2(n) mengitung perjumlahan deret geometri dimulai dari 1 dan selanjutnya dengan masing masing deret ditambah pangkat 2 dari n menggunakan ekspresi rekursif}

# REALISASI
def geometric2(n):
    if n == 1:
        return 1
    else:
        return (n)**2+ geometric2(n-1)
    
# APLIKASI
print(geometric2(1))  
print(geometric2(2))  
print(geometric2(3))  
    