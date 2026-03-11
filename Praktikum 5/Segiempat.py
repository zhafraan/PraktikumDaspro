# Nama File   = Segiempat.py
# Nama        = Aqiatillah Rezi Zhafran
# NIM         = 24060124140124
# Tanggal     = 30 September 2024 
# Deskripsi   = menjawab soal tipe segiempat

# DEFINISI TYPE
# type Point: <x:integer, y:integer>
#   {<x,y> adalah sebuah point dengan x sebagai absis dan y sebagai ordinat}
# type Segiempat: <P1:Point, P2:Point, P3:Point, P4:Point>
#   {Segiempat dibentuk oleh 4 point (P1, P2, P3, P4)}

# DEFINISI DAN SPESIFIKASI KONSTRUKTOR
# MakePoint: 2real --> Point
#   {MakePoint(X, Y) membentuk point dari x dan y dengan x sebagai absis dan y sebagai ordinat}
# MakeSegiempat: 4Point --> Segiempat
#   {MakeSegiempat(P1, P2, P3, P4) membentuk Segiempat dari 4 point (P1, P2, P3, P4)}

# DEFINISI DAN SPESIFIKASI SELEKTOR
# absis: Point --> real
# {absis(P) memberikan nilai absis (X) dari point P}
# ordinat: Point --> real
# {ordinat(P) memberikan nilai ordinat (Y) dari point P}
# Point1: Segiempat --> Point
# {Point1(S) memberikan point P1 dari Segiempat S}
# Point2: Segiempat --> Point
# {Point2(S) memberikan point P2 dari Segiempat S}
# Point3: Segiempat --> Point
# {Point3(S) memberikan point P3 dari Segiempat S}
# Point4: Segiempat --> Point
# {Point4(S) memberikan point P4 dari Segiempat S}

# DEFINISI DAN SPESIFIKASI OPERATOR
# Jarak: Point, Point --> real
# {Jarak(P1, P2) menghitung jarak Euclidean antara dua point P1 dan P2}
# Gradien: Point, Point --> real
# {Gradien(P1, P2) menghitung gradien garis yang dibentuk oleh P1 dan P2}

# DEFINISI DAN SPESIFIKASI PREDIKAT
# IsBujurSangkar: 4Point --> Boolean
# {IsBujurSangkar(P1, P2, P3, P4) mengecek apakah keempat point membentuk bujur sangkar}
# IsJajargenjang: 4Point --> Boolean
# {IsJajargenjang(P1, P2, P3, P4) mengecek apakah keempat point membentuk jajar genjang}

# DEFINISI DAN SPESIFIKASI DENGAN OPERATOR LAIN
# AreaBujurSangkar: 4Point --> real
# {AreaBujurSangkar(P1, P2, P3, P4) menghitung luas bujur sangkar jika keempat point membentuk bujur sangkar}


# REALISASI
def MakePoint(X,Y):
    return [X,Y]

def MakeSegiempat(P1,P2,P3,P4):
    return [P1,P2,P3,P4]

def absis(P):
    return P[0]

def ordinat(P):
    return P[1]

def Point1(S):
    return S[0]

def Point2(S):
    return S[1]

def Point3(S):
    return S[2]

def Point4(S):
    return S[3]

def Jarak(P1,P2):
    return (((absis(P1) - absis(P2))** 2) + ((ordinat(P1) - ordinat(P2))** 2))**0.5

def Gradien(P1,P2):
    return (ordinat(P2) - ordinat(P1)) / (absis(P2) - absis(P1))

def AreaBujurSangkar(S):
    return Jarak(Point1(S), Point2(S)) * Jarak(Point3(S), Point4(S))

def IsBujurSangkar(S):
    return Jarak(Point1(S), Point2(S)) == Jarak(Point3(S), Point4(S)) and Jarak(Point1(S), Point3(S)) == Jarak(Point2(S), Point4(S))

def IsJarjargenjang(S):
    P1 = Point1(S)
    P2 = Point2(S)
    P3 = Point3(S)
    P4 = Point4(S)
    return Gradien(P1, P2) == Gradien(P3, P4) and Gradien(P1, P4) == Gradien(P2, P3) and Jarak(P1, P2) == Jarak(P3, P4) and Jarak(P1, P4) == Jarak(P2, P3)

#APLIKASI
print(AreaBujurSangkar(MakeSegiempat( MakePoint(2, 3), MakePoint(4, 3), MakePoint(2, 2), MakePoint(4, 2))))
print(IsBujurSangkar(MakeSegiempat(MakePoint(2, 5), MakePoint(6, 5), MakePoint(2, 2), MakePoint(6, 2))))
print(IsJarjargenjang(MakeSegiempat(MakePoint(1, 1), MakePoint(4, 1), MakePoint(6, 4), MakePoint(3, 4))))