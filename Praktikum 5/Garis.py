# Nama File   = Garis.py
# Nama        = Aqiatillah Rezi Zhafran
# NIM         = 24060124140124
# Tanggal     = 30 September 2024 
# Deskripsi   = menjawab soal tipe bentukan garis

# DEFINISI TYPE
# type Point: <x:integer, y:integer>
#   {<x,y> adalah sebuah point dengan x adalah Absis dan y adalah Ordinat}

# DEFINISI DAN SPESIFIKASI KONSTRUKTOR
# Make-point: 2real --> point
#   {Make_point(X,Y) membentuk point dari x dan y dengan x sebagai Absis dan y sebagai Ordinat}
# REALISASI
def Make_point(X,Y):
    return [X,Y]

# DEFINISI DAN SPESIFIKASI SELECTOR
# Absis: point --> integer
#   {Absis(P) memberikan Absis dari point P}
# Ordinat: point --> integer
#   {Ordinat(P) memberikan Ordinat dari point P}
# REALISASI
def Absis(P):
    return P[0]

def Ordinat(P):
    return P[1]

# =================================================================================================================================================================
# DEFINISI TYPE
# type Garis: <P1:point, P2:point>
#   {<P1,P2> adalah sebuah garis dengan P1 adalah Point1 dan P2 adalah Point2}

# DEFINISI DAN SPESIFIKASI KONSTRUKTOR
# Make-Garis: 2point --> Garis
#   {Make_Garis(P1,P2) membentuk Garis dari P1 dan P2 dengan P1 sebagai point-1 dan P2 sebagai point-2}

# REALISASI
def Make_Garis(P1,P2):
    return [P1,P2]

# DEFINISI DAN SPESIFIKASI SELECTOR
# Point1: Garis --> Point
#   {Point1(G) memberikan Point-1 dari Garis G}
# 
# Point2: Garis --> Point
#   {Point2(G) memberikan Point-2 dari Garis G}

# REALISASI
def Point1(G):
    return G[0]

def Point2(G):
    return G[1]

# DEFINISI DAN SPESIFIKASI OPERATOR/FUNGSI LAIN TERHADAP GARIS
# panjang_garis: Garis --> real
#   {panjang_garis(G) menghitung panjang garis dari point-1 ke point-2}

# REALISASI
def panjang_garis(G):
    panjang_x = Absis(Point2(G)) - Absis(Point1(G))
    panjang_y = Ordinat(Point2(G)) - Ordinat(Point1(G))
    return ((panjang_x ** 2) + (panjang_y ** 2))**0.5

# DEFINISI DAN SPESIFIKASI FUNGSI TAMBAHAN
# Gradien : point, point → real
#  { Gradien(P1, P2) menghitung gradien (kemiringan) dari garis yang dibentuk oleh dua titik P1 dan P2 }
# Jarak : point, point → real
#  { Jarak(P1, P2) menghitung jarak antara dua titik P1 dan P2 menggunakan rumus jarak Euclidean }

# REALISASI
def Gradien(P1, P2):
    return (Ordinat(P2) - Ordinat(P1)) / (Absis(P2) - Absis(P1))

# DEFINISI DAN SPESIFIKASI PREDIKAT
# Issejajar: Garis --> Boolean
#   {IsSejajar(G1,G2) benar jika G1 sama dengan G2}

# REALISASI
def IsSejajar(G1,G2):
    return Gradien(Point1(G1), Point2(G1)) == Gradien(
        Point1(G2),Point2(G2))

# APLIKASI
print(IsSejajar(Make_Garis(Make_point(2, 4), Make_point(4, 4)), Make_Garis(Make_point(4, 4), Make_point(5, 4))))
print(IsSejajar(Make_Garis(Make_point(2, 5), Make_point(4, 4)), Make_Garis(Make_point(4, 5), Make_point(5, 4))))
print(panjang_garis(Make_Garis(Make_point(5,4), Make_point(6,5)))) 