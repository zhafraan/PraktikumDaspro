# Nama File   = 8.Deretgeometri.py
# Nama        = Aqiatillah Rezi Zhafran
# NIM         = 24060124140124
# Tanggal     = 5 Oktober 2024
# Deskripsi   = menghitung deret geometri menggunakan ekspresi rekursif

#DEFINISI DAN SPESIFIKASI
# geometric : integer > 0 -> integer
#   {geometric(n) adalah menghitung nilai dari deret geometri dengan rasio 3 pada suku ke-n munggunakan ekspresi rekursif}

# REALISASI
def geometric(n):
    if n == 1:
        return 1
    else:
        return 3**(n-1) + geometric(n-1)

# APLIKASI 
print(geometric(1))
print(geometric(2))
print(geometric(3))