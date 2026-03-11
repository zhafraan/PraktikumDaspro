# Nama File : PetualangandiDuniaLumerion.py
# Deskripsi : SC Hackerrank PetualangandiDuniaLumerion
# Pembuat   : Aqiatillah Rezi Zhafran
# NIM       : 24060124140124
# Tanggal   : 1 Desember 2024

# DEFINISI DAN SPESIFIKASI SELEKTOR
# operasi: List -> elemen
# operasi(P) mengembalikan elemen pertama dari list P.
def operasi(P):
    return P[0]

# angka1: List -> elemen
# angka1(P) mengembalikan elemen kedua dari list P.
def angka1(P):
    return P[1]

# angka2: List -> elemen
# angka2(P) mengembalikan elemen ketiga dari list P.
def angka2(P):
    return P[2]

# DEFINISI DAN SPESIFIKASI PREDIKAT
# isEmpty: List -> boolean
# isEmpty(P) benar jika list kosong
def isEmpty(P):
    return P == []

# DEFINISI DAN SPESIFIKASI OPERASI
# EvaluateExpression: List -> integer
# EvaluateExpression(S) mengembalikan hasil evaluasi dari ekspresi yang diberikan.
def EvaluateExpression(S):
    if isEmpty(S):
        return []
    else:
        if operasi(S) == '+':
            return angka1(S) + angka2(S)
        elif operasi(S) == '-':
            return angka1(S) - angka2(S)
        elif operasi(S) == '*':
            return angka1(S) * angka2(S)
        elif operasi(S) == '/':
            return angka1(S) / angka2(S)
        
# APLIKASI
print(EvaluateExpression(['+', 3, 5]))
print(EvaluateExpression(['-', 10, 4]))
