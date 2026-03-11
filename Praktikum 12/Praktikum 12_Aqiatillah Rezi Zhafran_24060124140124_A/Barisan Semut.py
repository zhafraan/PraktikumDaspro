# Nama File : Agen Mangga.py
# Deskripsi : SC Hackerrank Barisan Semut
# Pembuat   : Aqiatillah Rezi Zhafran
# NIM       : 24060124140124
# Tanggal   : 1 Desember 2024

# DEFINISI DAN SPESIFIKASI SELEKTOR
# FirstElmt: List -> elemen
# FirstElmt(L) mengembalikan elemen pertama dari list L.
def FirstElmt(L):
    return L[0]

# Tail: List -> List
# Tail(L) mengembalikan list tanpa elemen pertama dari list L.
def Tail(L):
    return L[1:]

# DEFINISI DAN SPESIFIKASI PREDIKAT
# IsEmpty: List -> boolean
# IsEmpty(L) benar jika list kosong.
def IsEmpty(L):
    return L == []

# DEFINISI DAN SPESIFIKASI OPERASI
# Angka: int, int, int, int -> List
# Angka(x, y, n, z) mengembalikan list yang berisi n angka yang dimulai dari z,
# dengan penambahan x, dan mengabaikan angka yang merupakan kelipatan dari y.
def Angka(x, y, n, z):
    if n == 0:
        return []
    elif z % y == 0:
        return Angka(x, y, n, z + x)
    else:
        return [z] + Angka(x, y, n - 1, z + x)

# BarisanSemut: int, int, int -> List
# BarisanSemut(x, y, n) mengembalikan list yang dihasilkan dari fungsi Angka
# dengan parameter x, y, n, dan z diinisialisasi dengan x.
def BarisanSemut(x, y, n):
    return Angka(x, y, n, x)

#APLIKASI
print(BarisanSemut(2, 3, 5))
print(BarisanSemut(1, 2, 10))