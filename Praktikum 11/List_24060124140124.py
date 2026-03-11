#Nama File  : List_24060124140124.py
#Deskripsi  : berisi type dan operasi list
#Pembuat    : Aqiatillah Rezi Zhafran
#Tangga1    : 30 Oktober 2024

#DEFINISI DAN SPESIFIKASI TYPE
#Konstruktor menambahkan elemen di awal, notasi prefix

#type List: [] atau [e o List]
#Konstruktor menambahkan elemen di akhir, notasi postfis
# type List: [] atau [List o e]

#DEFINISI DAN SPESIFIKASI KONSTRUKTOR
# Konso: elemen, List -> List
# Konso(e,L) menghasilkan sebuah list dari e dan L dengan e sebagai elemen pertama
# Realisasi
def Konso(e,L):
    return[e]+ L
# Konsi: List, elemen -> List
# Konsi(L,e) - > menghasilkan sebah list dari L dan e dengan e sebagai elemen terakhir
# Realisasi
def Konsi(L,e):
    return L + [e]

#DEFINISI DAN SPESIFIKASI SELEKTOR
# FirstElmt: List tidak kosong -> elemen
# FirstEImt(L) Menghasilkan elemen pertama list L
# Realisasi
def FirstElmt(L):
    return L[0]

# LastE1mt: List tidak kosong ->elemen
# LastElmt(L): mengembalikan elemen terakhir terakhir list L
# Realisasi
def LastElmt(L):
    return L[-1]  

# Tail : List tidak kosong -> List
# Tail (L) : Menghasilkan list tanpa elemen pertama list L, mungkin kosong
# Realisasi
def Tail(L):
    return L[1:]

# Head : List tidak kosong-> List
# Head(L) : Menghasilkan list tanpa elemen terakhir list L,mungkin kosong
# Realisasi
def Head(L):
    return L[:-1]

# DEFINISI DAN SPESIFIKASI PREDIKAT
# IsEmpty : List -> boolean
# IsEmpty(L) benar jika list kosong
# Realisasi
def IsEmpty(L):
    return L == []

# IsOneE1mt: List -> boolean
# IsOneE1mt (X, L) adalah benar j ika list L hanya mempunyai satu elemen
# Realisasi
def IsOneEmlt(L):
    if IsEmpty(L):
        return False
    else:
        return Tail (L)==[] and Head(L) == []
    
# DEFINISI DAN SPESIFIKASI FUNGSI YANG MENGOPERASIKAN LIST
# NbElmt : List -> integer
# NbElmt(L) : Menghasilkan banyaknya elemen list, nol jika kosong
# Realisasi
def NbElmt(L):
    if IsEmpty(L):
        return 0
    else:
        return 1 + NbElmt(Tail(L))
    
#APLIKASI
# print(Konso(2,[3]))
# print(Konsi([3,4,5],6))
# print(FirstElmt([3,4,5,6,7]))
# print(LastElmt([3,4,5,6,7]))
# print(Tail([3,4,5,6,7]))
# print(Head([3,4,5,6,7]))
# print(IsEmpty([]))
# print(IsEmpty([3,4,5,6,7]))
# print(IsOneEmlt( [] ) )
# print(IsOneEmlt( [3] ) )
# print(IsOneEmlt([3,4,5,6,7]))
# print(NbElmt([3,4,5,6,7]))

# print("==================================================================================================================================================================")
 
# ElmtkeN :integer >= 0,List -> elemen
# ElmtkeN (N,L) : Mengirimkan elemen list yang ke N, N <= NbELmt(L) dan N>= 0
# Realisasi
def  ElmtkeN(N,L):
    if N == 1 :
        return FirstElmt(L)
    else :
        return ElmtkeN(N-1,Tail(L))

# print(ElmtkeN(3,[3,4,5,6,7]))

# IsMember : elemen, List -> boolean
# IsMember (X,L) adalah benar jika X adalah elemen list L
# Realisasi
def IsMember(X,L):
    if IsEmpty(L):
        return False
    else:
        if FirstElmt(L) == X :
            return True
        else:
            return IsMember(X,Tail(L))

# print(IsMember(3,[3,4,5,6,7]))

# Copy : List -> List
# Copy(L) : Menghasilkan list yang identik dengan list asal
# Realisasi
def Copy(L):
    if IsEmpty(L):
        return []
    else :
        return Konso(FirstElmt(L),Copy(Tail(L)))

# print(Copy([3,4,5,6,7]))

# Inverse : List -> List
# Inverse(L) : Menghasilkan list L yang dibalik, yaitu yang urutan elemennya
# adalah kebalikan dari list asal
# Realisasi
def Inverse(L):
    if IsEmpty(L):
        return []
    else:
        return Konso(LastElmt(L),Inverse(Head(L)))
    
# print(Inverse([1,2,3,4,5,6,7,8]))

# Konkat : 2 List -> List
# Konkat(L1,L2) : Menghasilkan konkatenasi 2 buah list, dengan list L2 "sesudah" list L1
# Realisasi
def Konkat(L1,L2):
    if IsEmpty(L1):
        return L2
    else :
        return Konso(FirstElmt(L1),Konkat(Tail(L1),L2))
    
# print(Konkat([2,3,4,5,6],[7,8,9,10]))

# SumElmt: List of integer -> integer
# SumElmt(L) menghasilkan jumlahan dari setiap elemen di list L
# Realisasi
def SumElmt(L):
    if IsEmpty(L):
        return 0
    else :
        return FirstElmt(L) + SumElmt(Tail(L))
# print(SumElmt([2,3,4,5,3,2,1,1]))

# AvgElmt: List of integer -> integer
# AvgEmlt(L) menghasilkan nilai rata-rata
# Realisasi
def AvgElmt(L):
    if IsEmpty(L):
        return []
    else :
        return SumElmt(L) / NbElmt(L)

# print(AvgElmt([3,4,6,7,5,8]))

# MaxElmt(L): List of integer - > integer
# MaxElmt(L) mengembalikan elemen maksimum dari list L
# Realisasi
def MaxElmt(L):
    if IsOneEmlt(L):
        return LastElmt(L)
    else :
        return max(L)

# print(MaxElmt([2,4,1,4,67,6,1,33,5]))

# MaxNB: List of integer -> <integer, integer>
# MaxNB(L) menghasilkan <max,countmax>
# dengan max adalah elemen maksimum list L
# dan countMax adalah banyaknya kemunculan max di list L
# Realisasi
def MaxNB(L):
    if IsEmpty(L):
        return []
    elif IsOneEmlt(L):
        return (FirstElmt(L),1)
    else :
        m,n  = MaxNB(Tail(L))
        if FirstElmt(L) > m :
            return(FirstElmt(L),1)
        elif FirstElmt(L) == m :
            return (m,n + 1)
        elif FirstElmt(L) < m :
            return(m,n)

# print(MaxNB([11, 3, 4, 5, 11, 6, 7, 8, 11]))

# AddList: 2 List of integer -> List of integer
# AddList(L1, L 2) menghasilkan list baru yang setiap elemennya
# adalah hasil penjumlahan setiap elemen di LI dan L 2 pada posisi yang sama
# Realisasi
def AddList(L1,L2):
    if IsEmpty(L1) and IsEmpty(L2) :
        return []
    elif IsEmpty(L1) and not IsEmpty(L2) :
        return L2
    elif not IsEmpty(L1) and IsEmpty(L2) :
        return L1
    else :
        return Konso(FirstElmt(L1) + FirstElmt(L2),AddList(Tail(L1),Tail(L2)))

# print(AddList([3, 4, 5, 6, 7],[2, 3, 4, 5, 6,]))

# IsPa1indrom(L): List of character -> boolean
# IsPaIindrom(L) benar jika L merupakan kata palindrom
# yaitu kata yang sama jika dibaca dari kiri atau kanan
# contoh: RUSAK, KASUR RUSAK, NABABAN
# Realisasi
def IsPalindrom(L):
    if IsEmpty(L) or IsOneEmlt(L):
        return True
    else:
        return FirstElmt(L) == LastElmt(L) and IsPalindrom(Tail(Head(L)))

# print(IsPalindrom(['R', 'U', 'S', 'A', 'K']))
# print(IsPalindrom(['K','A','S','U','R', 'U', 'S', 'A', 'K']))
# print(IsPalindrom(['N','A','B','A','B', 'A', 'N']))


