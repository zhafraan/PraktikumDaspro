# DEFINISI TYPE
#  type point: <x: real, y: real>
#   {<x,y>membuat point dari x dan y}
# type garis: <P1: point, P2: point>
#   {<P1,P2>membuat garis dari point 1 dan point 2}

# DEFINISI DAN SPESIFIKASI SELEKTOR
# GetX: point → real
#   {Memberikan koordinat x dari sebuah point.}
# GetY: point → real
#   {Memberikan koordinat y dari sebuah point.}
# GetP1: garis → point
#   {Memberikan point P1 dari sebuah garis.}
# GetP2: garis → point
#   {Memberikan point P2 dari sebuah garis.}

# DEFINISI DAN SPESIFIKASI KONSTRUKTOR
# MakePoint: 2 real → point
#   {Membentuk point dari koordinat x dan y.}
# MakeGaris: 2 point → garis
#   {Membentuk garis dari dua buah point P1 dan P2.}

# DEFINISI DAN SPESIFIKASI OPERATOR 
# Gradien: garis → real
#   {Menghitung gradien dari garis G. Jika garis vertikal, mengembalikan None}
# PanjangGaris: garis → real
#   {Menghitung panjang garis G menggunakan rumus Pythagoras.}
# IsSejajar: 2 garis → boolean
#   {Mengecek apakah dua garis sejajar, berdasarkan gradiennya.}
# IsTegakLurus: 2 garis → boolean
#   {Mengecek apakah dua garis tegak lurus, gradien G1 * gradien G2 == -1}

# REALISASI
def MakePoint(x, y):
    return [x, y]  

def GetX(P):
    return P[0]  

def GetY(P):
    return P[1] 

def MakeGaris(P1, P2):
    return [P1, P2] 

def GetP1(G):
    return G[0]  

def GetP2(G):
    return G[1] 

def Gradien(G):
    if GetX(GetP1(G)) == GetX(GetP2(G)):
        return None  
    else :
        return (GetY(GetP2(G)) - GetY(GetP1(G))) / (GetX(GetP2(G)) - GetX(GetP1(G)))

def PanjangGaris(G):
    return (((GetX(GetP2(G)) - GetX(GetP1(G))) ** 2) + ((GetY(GetP2(G)) - GetY(GetP1(G))) ** 2))

def IsSejajar(G1, G2):
    return Gradien(G1) == Gradien(G2)

def IsTegakLurus(G1, G2):
    if Gradien(G1) == None :
        return Gradien(G2) == 0
    elif Gradien(G2) == None :
        return Gradien(G1) == 0 
    else :
        return Gradien(G1) * Gradien(G2)== -1
    
print(IsSejajar(MakeGaris(MakePoint(5,10),MakePoint(4,6)),(MakeGaris(MakePoint(10,20),MakePoint(8,12)))))
print(IsTegakLurus(MakeGaris(MakePoint(5,10),MakePoint(4,6)),(MakeGaris(MakePoint(10,20),MakePoint(8,12)))))
print(PanjangGaris(MakeGaris(MakePoint(5,10),MakePoint(4,6))))
print(Gradien(MakeGaris(MakePoint(5,10),MakePoint(4,6))))