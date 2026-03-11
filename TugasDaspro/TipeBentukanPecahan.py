#DEFINISI TYPE
# type PecahanCampuran : <bil:integer,n:integer>=0,d:integer>0>
    #<bil,n,d> bil sebagai bilangan integer, n sebagai numerator, d sebagai denumerator}
# type Pecahan : <n: integer>=0, d: integer>0>
    #<n:integer>=0, d:integer>0 > n adalah pembilang (numerator) dan d adalah penyebut (denumerator)

#DEFINISI DAN FUNGSI SELEKTOR
#getBil : PecahanCampuran --> integer
    #{getBil(P) memberikan nilai bil pada pecahan Campuran P}
#getN : PecahanCampuran --> integer>=0
    #{getN(p) memberikan nilai n pada pecahan Campuran P}
#getD : --> PecahanCampuran --> integer >0
    #{getD(p) memberikan nilai d pada pecahan Campuran P}

#DEFINISI DAN FUNGSI KONSTRUKTOR
#makepecahancampuran: integer,integer>=0,0>integer>n --> PecahanCampuran
#{makepecahancampuran(bil,n,d) membuat sebuah pecahan campuran dari 3 inputan dengan ketentuan nominatornya lebih kecil dari denominator
# sebuah pecahan tidak boleh nol
#makepecahan : integer >=0, integer > 0 --> PecahanCampuran
    #{makepecahan(n,d) membuat Pecahan dari 2 inputan dengan ketentuan n >= 0, d > 0}


#DEFINISI DAN SPESIFIKASI OPERATOR
#KonversiPecahan : PecahanCampuran --> pecahan
    #{KonversiPecahan(P) mengubah pecahan campuran P ke tipe pecahan biasa, jika pecahan bernilai negatif, nilai negatif dilekatkan pada pembilang}
#KonversiReal : PecahanCampuran --> real
    #{KonversiReal(P) mengubah pecahan campuran P menjadi nilai real}
#AddP : 2 PecahanCampuran--> PecahanCampuran
    #{AddP(P1,P2) menjumlahan pecahan campuran P1 dan P2}
#SubP : 2 PecahanCampuran --> PecahanCampuran
    #{SubP(P1,P2) mengurangkan pecahan campuran P1 dan P2}
#DivP : 2 PecahanCampuran --> PecahanCampuran
    #{DivP(P1,P2) membagi pecahan campuran P1 dan P2}
#MulP : 2 PecahanCampuran --> PecahanCampuran
    #{MulP(P1,P2) mengalikan pecahan campuran P1 dan P2}

#DEFINISI DAN SPESIFIKASI FUNGSI ANTARA
#cariPemb : PecahanCampuran --> integer
    #{cariPemb(P) mencari pembilang dari sebuah pecahan campuran}
#Abs : integer --> integer
    #Abs(x) mencari nilai absolut dari x}
#jadiPecahanCampuran : pecahan --> PecahanCampuran
    #jadiPecahanCampuran(pembilang,penyebut) mengubah pecahan biasa menjadi pecahan campuran}

#DEFINISI DAN SPESIFIKASI PREDIKAT
#isEqP? : 2 PecahanCampuran --> boolean
    #{isEqP?(P1,P2) membandingkan apakah P1 sama dengan P2}
#isLtP? : 2 PecahanCampuran --> boolean
    #{isLtP?(P1,P2) membandingkan apakah P1 lebih kecil dari P2}
#isGtP? : 2 PecahanCampuran --> boolean
    #{isGtP?(P1,P2) membandingkan apakah P1 lebih besar dari P2}

#REALISASI 
def getBil(P):
    return P[0]
def getN(P):
    return P[1]
def getD(P):
    return P[2]
def Abs(x):
    if x < 0:
        return -x
    else:
        return x

def makepecahancampuran(bil,n,d):
    return [bil,n,d]
def Makepecahan(n,d):
    return [n,d]

def cariPemb(P):
    if getBil(P)<0:
        return getBil(P) * getD(P) - getN(P)
    elif getBil(P)>=0:
        return getBil(P) * getD(P) + getN(P)


def KonversiPecahan(P):
    if getBil(P) < 0:
        return Makepecahan(-(getBil(P)*getD(P)+getN(P)),getD(P))
    else :
        return Makepecahan(getBil(P)*getD(P)+getN(P),getD(P))

def KonversiReal(P):
    if getBil(P)<0:
        return -(getBil(P)+getN(P)/getD(P))
    else :
        return getBil(P) + getN(P) / getD(P)

def jadiPecahanCampuran(pembilang, penyebut):
    bil = pembilang // penyebut
    n = Abs(pembilang) % penyebut
    d = penyebut
    return makepecahancampuran(bil, n, d)

def AddP(P1,P2):
    pembilang = cariPemb(P1)*getD(P2)+cariPemb(P2)*getD(P1)
    penyebut = getD(P1)*getD(P2)
    return jadiPecahanCampuran(pembilang, penyebut)
def SubP(P1,P2):
    pembilang = cariPemb(P1) * getD(P2) - cariPemb(P2) * getD(P1)
    penyebut = getD(P1) * getD(P2)
    return jadiPecahanCampuran(pembilang, penyebut)
def DivP(P1,P2):
    pembilang = cariPemb(P1) * getD(P2)
    penyebut = cariPemb(P2) * getD(P1)
    return jadiPecahanCampuran(pembilang, penyebut)
def MulP(P1,P2):
    pembilang = cariPemb(P1) * cariPemb(P2)
    penyebut = getD(P1) * getD(P2)
    return jadiPecahanCampuran(pembilang, penyebut)

def isEqP(P1,P2):
    if KonversiReal(P1) == KonversiReal(P2):
        return True
    else:
        return False

def isLtp(P1,P2):
    if KonversiReal(P1) < KonversiReal(P2):
        return True
    else :
        return False

def isGtp(P1,P2):
    if KonversiReal(P1) > KonversiReal(P2):
        return True
    else:
        return False

print(KonversiPecahan(makepecahancampuran(3, 1, 2)))
print(KonversiReal(makepecahancampuran(3, 1, 2)))
print(AddP(makepecahancampuran(3, 1, 2), makepecahancampuran(-6, 1, 2)))
print(DivP(makepecahancampuran(3, 1, 2), makepecahancampuran(-6, 1, 2)))
print(MulP(makepecahancampuran(3, 1, 2), makepecahancampuran(-6, 1, 2)))
print(SubP(makepecahancampuran(3, 1, 2), makepecahancampuran(-6, 1, 2)))
print(isEqP(makepecahancampuran(3, 1, 2), makepecahancampuran(3,1,2)))
print(isLtp(makepecahancampuran(3, 1, 2), makepecahancampuran(12,1,2)))
print(isGtp(makepecahancampuran(333, 1, 6), makepecahancampuran(99,1,2)))




