# Nama File   = 5.Perkalian 3.py
# Nama        = Aqiatillah Rezi Zhafran
# NIM         = 24060124140124
# Tanggal     = 5 Oktober 2024
# Deskripsi   = menghitung perkalian dengan 3 menggunakan ekspresi rekursif

#DEFINISI DAN SPESIFIKASI
# kalitiga: integer >= 0 --> integer >=0
#   {kalitiga(n)mengitung perkalian dari input n dengan 3 dengan menggunakan ekspresi rekursif}

# REALISASI
def kalitiga(n):
    # print("Trace",n)
    if n == 0:
        return 0
    else:
        return 3 +  kalitiga(n-1)

# APLIKASI
print(kalitiga(0))
print(kalitiga(1))
print(kalitiga(2))
print(kalitiga(3))