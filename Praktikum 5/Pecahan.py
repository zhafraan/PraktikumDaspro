# Nama File   = Pecahan.py
# Nama        = Aqiatillah Rezi Zhafran
# NIM         = 24060124140124
# Tanggal     = 30 September 2024 
# Deskripsi   = menjawab soal tipe bentukan pecahan

# DEFINISI TYPE
# type pecahan: <n:integer, d:integer>
#   {<n,d> adalah sebuah point dengan n adalah pembilang dan d adalah penyebut, penyebut bpecahan tidak boleh nol}

# DEFINISI DAN SPESIFIKASI KONSTRUKTOR
# MakePoint: 2real --> pecahan
#   {makeP (n,d) membentuk point dari n dan d dengan n sebagai pembilang dan d sebagai penyebut}
# Realisasi
def makePoint (n,d):
    return[n,d]

#DEFINISI DAN SPESIFIKASI SELECTOR
# pembilang : pecahan --> integer
#   {pembilang(n) memberikan pembilang n dari pecahan tersebut}
# 
# penyebut  : pecahan --> integer
#   {penyebut(d) memberikan penyebut d dari pecahan tersebut}

# REALISASI
def pembilang(P):
    return P[0]

def penyebut(P):
    return P[1]

# DEFINISI DAN SPESIFIKASI PECAHAN
# AddP: 2 pecahan --> pecahan
#   {AddP(P1,P2) menmbahkan 2 buah pecahan yaitu P1 dan P2}
# 
# SubP: 2 pecahan --> pecahan
#   {SubP(P1,P2) mengurangkan 2 buah pecahan yaitu P1 dan P2}
# 
# MulP: 2 pecahan --> pecahan
#   {MulP(P1,P2) mengalikan 2 buah pecahan yaitu P1 dan P2}
# 
# DivP: 2 pecahan --> pecahan
#   {DivP(P1,P2) membagikan 2 buah pecahan yaitu P1 dan P2}
# 
# RealP: pecahan --> real
#   {RealP(P1) menuliskan bilangan pecahan dalam notasi desimal}

# REALISASI 
def AddP(P1,P2):
    return makePoint((pembilang(P1) * penyebut(P2)) + (pembilang(P2) * penyebut(P1)), (penyebut(P1) * penyebut(P2)))

def SubP(P1,P2):
    return makePoint((pembilang(P1) * penyebut(P2)) - (pembilang(P2) * penyebut(P1)), (penyebut(P1) * penyebut(P2)))
    
def MulP(P1,P2):
    return makePoint((pembilang(P1) * pembilang(P2)), (penyebut(P1) * penyebut(P2)))

def DivP(P1,P2):
    return makePoint((pembilang(P1) * penyebut(P2)), (penyebut(P1) * pembilang(P2)))

def RealP(P):
    return pembilang(P) / penyebut(P)

# DEFINISI DAN SPESIFIKASI PREDIKAT
# isEqP: 2 pecahan --> boolean
#   {isEqP(P1,P2) membandingkan apakah ke-2 buah pecahan itu sama}
# 
# isLtP: 2 pecahan --> boolean
#   {isLtP(P1,P2) membandingkan 2 buah pecahan apakah P1 lebih kecil dari P2}
# 
# IsGtp: 2 pecahan --> boolean
#   {IsGtp(P1,P2) membandingkan 2 buah pecahan apakah P1 lebih besar dari P2}

# REALISASI
def isEqP(P1,P2):
    return pembilang(P1)/penyebut(P1) == pembilang(P2)/penyebut(P2)

def isLtP(P1,P2):
    return pembilang(P1)/penyebut(P1) < pembilang(P2)/penyebut(P2)

def IsGtp(P1,P2):
    return pembilang(P1)/penyebut(P1) > pembilang(P2)/penyebut(P2)


# APLIKASI
print(AddP(makePoint(4,5), makePoint(2,4)))
print(SubP(makePoint(4,5), makePoint(2,4)))
print(MulP(makePoint(4,5), makePoint(2,4)))
print(DivP(makePoint(4,5), makePoint(2,4)))
print(RealP(makePoint(4,5)))

print(isLtP(makePoint(1,3), makePoint(1,2)))
print(isEqP(makePoint(2,4), makePoint(1,2)))
print(IsGtp(makePoint(2,4), makePoint(1,2)))