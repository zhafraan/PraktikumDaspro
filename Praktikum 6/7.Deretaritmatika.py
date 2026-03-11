# Nama File   = 7.Deretaritmatika.py
# Nama        = Aqiatillah Rezi Zhafran
# NIM         = 24060124140124
# Tanggal     = 5 Oktober 2024
# Deskripsi   = membuat deret aritmatika menggunakan ekspresi rekursif

# DEFINISI DAN SPESIFIKASI
# deretaritmatika: integer > 0 --> integer
#   {deretaritmatika(n)menghitung nilai suku ke-n deret aritmatika dimulai dari 3 dan selanjutnya dengan masing masing deret dikali 3 menggunakan ekspresi rekursif}

# REALISASI
def deretaritmatika(n):
    if n == 1:
        return 3
    else:
        return 3*n + deretaritmatika(n-1)  
    
# APLIKASI   
print(deretaritmatika(1))
print(deretaritmatika(2))
print(deretaritmatika(3))