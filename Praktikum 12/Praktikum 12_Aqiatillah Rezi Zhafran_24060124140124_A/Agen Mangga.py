# Nama File : Agen Mangga.py
# Deskripsi : SC Hackerrank Agen Mangga
# Pembuat   : Aqiatillah Rezi Zhafran
# NIM       : 24060124140124
# Tanggal   : 1 Desember 2024

#DEFINISI DAN SPESIFIKASI KONSTRUKTOR
# Buah: List tidak kosong -> elemen
# Buah(P) Menghasilkan elemen pertama list P
def Buah(P):
    return P[0]

# Agen: List tidak kosong -> elemen
# Agen(P) Menghasilkan elemen kedua list P
def Agen(P):
    return P[1]

#DEFINISI DAN SPESIFIKASI SELEKTOR
# Tail : List tidak kosong -> List
# Tail (P) : Menghasilkan list tanpa elemen pertama list P, mungkin kosong
def Tail(P):
    return P[1:]

# First : List tidak kosong -> elemen
# First(P) Menghasilkan elemen pertama list P
def First(P):
    return P[0]

# Last: List tidak kosong ->elemen
# Last(P): mengembalikan elemen terakhir terakhir list P
def Last(P):
    return P[-1]

# DEFINISI DAN SPESIFIKASI PREDIKAT
# IsEmpty : List -> boolean
# IsEmpty(P) benar jika list kosong
def Isempty(P):
    return P == []

# DEFINISI DAN SPESIFIKASI OPERASI
# BeratMangga:List,character -> integer
# BeratMangga(mangga, agen) menghitung total berat mangga dalam list mangga berdasarkan agen yang diberikan.
def BeratMangga(mangga, agen):
    if Isempty(mangga):
        return 0
    elif agen == 'A':
        if mangga[0]%2 != 0:
            return mangga[0] + BeratMangga(Tail(mangga),agen)
        else :
            return BeratMangga(Tail(mangga),agen)
    elif agen == 'B':
        if mangga[0]%2 == 0:
            return mangga[0] + BeratMangga(Tail(mangga),agen)
        else :
            return BeratMangga(Tail(mangga),agen)
        
# APLIKASI
print(BeratMangga([1, 2, 4, 5, 7], 'A'))     
print(BeratMangga([1, 2, 4, 5, 7], 'B'))     