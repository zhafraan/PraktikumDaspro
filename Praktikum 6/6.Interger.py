# Nama File   = 6.Integer.py
# Nama        = Aqiatillah Rezi Zhafran
# NIM         = 24060124140124
# Tanggal     = 5 Oktober 2024
# Deskripsi   = membuat perhitungan deret bilangan integer menggunakan ekspresi rekursif

# DEFINISI DAN SPESIFIKASI
# Bil_Integer : integer > 0 -> integer
#   {Bil_Integer(x) adalah menghitung penjumlah deret aritmatika bilangan integer bilangan dari 1 hingga x menggunakan ekspresi rekursif}

# REALISASI
def Bil_Integer(x):
    if x == 1:
        return 1
    else:
        return x + Bil_Integer(x-1)

# APLIKASI    
print(Bil_Integer(1))
print(Bil_Integer(2))
print(Bil_Integer(3))
