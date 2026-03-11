# Nama File : Tebak Huruf.py
# Deskripsi : SC Hackerrank Tebak Huruf
# Pembuat   : Aqiatillah Rezi Zhafran
# NIM       : 24060124140124
# Tanggal   : 1 Desember 2024

# DEFINISI DAN SPESIFIKASI SELEKTOR
# firstElmt: List -> elemen
# firstElmt(L) mengembalikan elemen pertama dari list L.
def firstElmt(L):
    return L[0]

# Tail: List -> List
# Tail(L) mengembalikan list tanpa elemen pertama dari list L, mungkin kosong.
def Tail(L):
    return L[1:]

# DEFINISI DAN SPESIFIKASI PREDIKAT
# isempty: List -> boolean
# isempty(L) benar jika list kosong.
def isempty(L):
    return L == []

# DEFINISI DAN SPESIFIKASI OPERASI
# TebakHuruf: character, List -> string
# TebakHuruf(huruf, nama) mengembalikan "YA" jika huruf sama dengan elemen pertama dari nama,
# "TIDAK" jika tidak, dan melanjutkan pemeriksaan pada elemen berikutnya.
def TebakHuruf(huruf, nama):
    if isempty(huruf) and isempty(nama):
        return "YA"
    elif isempty(huruf) and not isempty(nama):
        return "TIDAK"
    elif not isempty(huruf) and isempty(nama):
        return "TIDAK"
    elif not isempty(huruf) and not isempty(nama):
        if huruf == firstElmt(nama):
            return "YA"
        else:
            return TebakHuruf(huruf, Tail(nama))
        
#APLIKASI
print(TebakHuruf('k', ['s', 'e', 'n', 'k', 'u']))
print(TebakHuruf('a', ['b', 'o', 'r', 'u', 't', 'o']))