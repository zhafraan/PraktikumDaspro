# Nama File : treeNaire _24060124140124.py
# Deskripsi : berisi type dan operasi pohon N-ner
# Pembuat   : Aqiatillah Rezi Zhafran
# NIM       : 24060124140124
# Tanggal   : 18 November 2024(dimulai di vs code)


from List_24060124140124 import*
#DEFINISI DAN SPESIFIKASI KONSTRUKTOR
def makePN(A,PN):
    return[A,PN]

#DEFINISI DAN SPESIFIKASI SELEKTOR
#Akar :PohonN-ner tidak kosong -> Elemen
# { Akar(P) adalah Akar dari P. Jika P adalah (A, PN)Akar(P) adalah A }
def Akar(PN):
    return PN[0]
#Anak : PohonN-ner t idak kosong -> List of PohonN-ner
#{ Anak(P) adalah List of Pohon N-ner yang merupakan anak-anak (sub phon)
# dari P. Jika P adalah (A, PN) = Anak (P) adalah PN }
def Anak(PN):
    return PN[1]

#DEFINISI DAN SPESIFIKASI PREDIKAT
# IsTreeNEmpty : PohonN-ner -> boolean
# {IsTreeNEmpty(PN) true jika PN kosong: ()}
def IsTreeNEmpty(PN):
    return PN == []
#IsOneElmt : PohonN-ner -> boolean
#{IsOneElmt(PN) true jika PN hanya mterdiri dari Akar }
def IsOneElmt(PN):
    return (IsTreeNEmpty(PN) == False) and (IsTreeNEmpty(Anak(PN)) == True)

#NbNElmt : PohonN-ner -> Integer >= 0
# {NbNELmt(P) memberikan banyaknya node dari pohon P :
# Basis 1: NbNELmt ((A)\) = 1
#Rekurens : NbNElmt((A,PN)) = 1 + NbElmat(PN)}
def NbNElmt(PN):
    # Basis:Jika pohon kosong
    if IsTreeNEmpty(PN):
        return 0
    # Jika hanya ada satu elemet(akar saja)
    if IsOneElmt(PN):
        return 1
    # Hitung 1 untuk akar,dan rekursif pada setiap anak pohon
    # Tanpa menggunakan loop,kita memanggil fungsi untuk setiap anak secara rekursif
    # Pertama Pada anak pertama
    return 1 + NbNElmt(Anak(PN)[0]) + NbNElmtChild(Anak(PN)[1:])


#Fungsi tambahan untuk menghitung jumlah elemen pada sisa anak anak
def NbNElmtChild(PN):
    #Basis: Jika tidak ada anak
    if IsTreeNEmpty(PN):
        return 0
   # Jika ada anak, rekursif pada anak pertama dan sisa anak-anak
    return NbNElmt(PN[0]) + NbNElmtChild(PN[1:])


# Fungsi tambahan untuk menghitung jumlah elemen pada sisa anak-anak
def NbNDaun(PN):
    # Basis: Jika pohon kosong
    if IsTreeNEmpty(PN):
        return 0
    # Jika pohon adalah daun (anak kosong)
    if IsOneElmt(PN) and IsTreeNEmpty(Anak(PN)):
        return 1
    # Rekursi pada akar dan anak-anak
    return NbNDaunChild(Anak(PN))

# Fungsi tambahan untuk menghitung jumlah daun pada sisa anak-anak

def NbNDaunChild(PN):
    # Basis: Jika tidak ada anak
    if IsTreeNEmpty(PN):
        return 0
    # Jika ada anak, rekursif pada anak pertama dan sisa anak-anak
    else:
        return NbNDaun(PN[0]) + NbNDaunChild(PN[1:])

#APLIKASI
T = makePN(2,[])
print(makePN(2,[]))
print(IsTreeNEmpty(T))
print(IsOneElmt(T))
T2 = makePN('A',[makePN('B',[makePN('D',[]),makePN('E',[]),makePN('F',[])]),makePN('C',[makePN('G',[]),makePN('H',[makePN('I',[])])])])
print(T2)
print(NbNElmt(T2))
print(NbNDaun(T2))


    
    

