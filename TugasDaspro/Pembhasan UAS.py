# UAS 2023
# Nomor 1
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
    
# DEFINISI DAN SPESIFIKASI
# FilterGenap: List   List
# {FilterGenap(L)menghasilkan sebuah list dengan memfilter elemen dari list L yang merupakan bilangan genap}

# REALISASI
def FilterGenap(L):
    if IsEmpty(L):
        return []
    else:
        if FirstElmt(L) % 2 == 0:
            return Konso(FirstElmt(L) ,FilterGenap(Tail(L)))
        else:
            return FilterGenap(Tail(L))
        
print(FilterGenap([6, 3, 1, 28, 12, 9, 41]))

# APLIKASI
# FilterGenap([6, 3, 1, 28, 12, 9, 41) -> [6, 28, 12] FilterGenap(L)

# Nomor 2
#DEFINISI DAN SPESIFIKASI PREDIKAT KHUSUS LIST
# IsEmpty: list of list - > boolean
# IsEmpty(S) benar jika S adalah list of list kosong.
def isEmpty(S):
    return S == []
# IsAtom: list of list -> boolean
# IsAtom(S) benar jika S adalah sebuah atom.
def isAtom(S):
    return type(S) != list
# IsList: list of list -> boolean
# IsList(S) benar jika S adalah sebuah list.
def isList(S):
    return type(S) == list

#DEFINISI DAN SPESIFIKASI KONSTRUKTOR
# KonsLo: list, list of list -> list of list
# KonsLo(L,S) membentuk list baru dengan list (L) yang diberikan sebagai elemen
#   pertama list of list (S).
def KonsLo(L,S):
    return[L] + S
# KonsLi: list of list, list - > list of list
# KonsLi(S,L) membentuk list baru dengan list (L) yang diberikan sebagai elemen
# terakhir list of list (S).
def KonsLi(S,L):
    return S +[L]

#DEFINISI DAN SPESIFIKASI SELEKTOR
# FirstList: list of list tidak kosong -> list
# FirstList(S) menghasilkan elemen pertama list (mungkin sebuah list atau atom)
def FirstList(S):
    return S[0]
# LasttList: list of list tidak kosong -> list
# LastList(S) menghasilkan elemen terakir list (mungkin sebuah list atau atom)
def Lastlist(S):
    return S[-1]
# TailList: list of list tidak kosong - > list of list
# TailList(S) menghasilkan sisa list of list S tanpa elemen pertamanya.
def TailList(S):
    return S[1:]
# HeadList: list of list tidak kosong - > list of list
# HeadList(S) menghasilkan sisa list of list S tanpa elemen terakhirnya.
def HeadList(S):
    return S[:-1]

# DEFINISI DAN SPESIFIKASI
# IsContainList: List of List → boolean
# IsContainList(S) mengembalikan true jika salah satu anggota dari list of list S berupa list
# REALISASI



# REALISASI DALAM PYTHON
def IsContainList(S):
    if isEmpty(S):
        return False
    elif isAtom(FirstList(S)):
          return IsContainList(TailList(S))
    elif isAtom(FirstList(S)):
                return True
    else:
        if isList(FirstList(S)) :
            return True
        else:
            return IsContainList(TailList(S))

    
print(IsContainList([6, [3, 1], [28, 12, 9], 4]))
print(IsContainList([6, 3, 1, 28, 12, 9, 4]))
# APLIKASI
# IsContainList([6, [3, 1], [28, 12, 9], 4]) → true
# IsContainList([6, 3, 1, 28, 12, 9, 4]) → false




