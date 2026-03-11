# Nama File : Lol_24060124140124.py
# Deskripsi : Operasi List of list
# Pembuat   : Aqiatillah Rezi Zhafran
# NIM       : 24060124140124
# Tanggal   : 11 November 2024(dimulai di vs code)

from List_24060124140124 import*

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

# IsMemberLS: list, list of list-> boolean
# IsMemberLS(L,S) mengembalikan true jika list L ada di dalam list of list
def isMemberLS(L,S):
    if isEmpty(S):
        return False
    else :
        if (isAtom(FirstList(S))):
          return isMemberLS(L,TailList(S))
        else:
            if(isAtom(FirstList(S))):
                return True
            else:
                if(IsEqS(FirstList(S), L) ) :
                    return True
                else:
                    return isMemberLS(L,TailList(S))

# DEFINISI DAN SPESIFIKASI FUNGSI YANG MENGOPERASIKAN LIST
# IsEqS:2 list of list -> boolean
# IsEqS(S1,S2) benar jika SI memiliki elemen dengan nilai dan urutan yang sama dengan S2
def IsEqS(S1,S2):
  if(isEmpty(S1) and isEmpty(S2)):
    return True
  elif(isEmpty (S1) and not isEmpty (S2)):
    return False
  elif(not isEmpty (S1) and isEmpty (S2)):
    return False
  else:
    if(isAtom(FirstList(S1)) and isAtom (FirstList(S2))):
      if(FirstList(S1) == FirstList(S2)):
        return IsEqS(TailList(S1), TailList(S2))
      else:
        return False
    elif(isList(FirstList(S1)) and isList(FirstList(S2))):
      return IsEqS(FirstList(S1), FirstList(S2)) and IsEqS (TailList(S1),TailList(S2))
    else:
      return False
        
# APLIKASI
print(f"KonsLo: {KonsLo([2],[3])}")
print(f"KonsLi: {KonsLi([3,4,5],[6])}")
print(f"FirstList: {FirstList([[3],4,5,6,7])}")
print(f"TailList: {TailList([3,[4,5,6,7]])}")
print(f"Lastlist: {Lastlist([3,4,5,6,[7]])}")
print(f"HeadList: {HeadList([[3,4,5,6],7])}")
print(f"isEmpty: {isEmpty([])}")
print(f"isEmpty: {isEmpty([[]])}")
print(f"isAtom: {isAtom(FirstList([[3],4,5,6,7]))}")
print(f"isList: {isList(FirstList([[3],4,5,6,7]))}")
print(f"NbElmt: {NbElmt([3,4,[5,6],7])}")
print(f"IsEqS: {IsEqS([3,[4,5],6,7],[3,[4,5],6,7])}")
print(f"IsEqS: {IsEqS([3,4,5,6,7],[3,[4,5],6,7])}")
print(f"IsEqS: {IsEqS([3,[4,5],[6],7],[3,[4,5],6,7])}")
print(f"isMemberLS: {isMemberLS([6],[3,[4,5],6,[6],7])}")
print(f"isMemberLS: {isMemberLS([4,5],[3,[4,5],6,[6],7])}")


# IsMemberS: elemen, list of list-> boolean
# IsMemberS(x,S) mengembalikan true jika elemen x ada di dalam list of list S
def IsMemberS(x, S):
    if isEmpty(S):
        return False
    else:
        if isAtom(FirstList(S)):
            if x == FirstList(S):
                return True
            else:
                return IsMemberS(x, TailList(S))
        else:
            if IsMemberS(x, FirstList(S)):
                return True
            else:
                return IsMemberS(x, TailList(S))
         
# Rember: elemen, list of list -> list of list
# Rember(x,S) menghapus semua elemen x yang ada di list of list S
def Rember(x,S):
   if isEmpty(S):
      return S
   else:
      if isList(FirstList(S)):
         return KonsLo(Rember(x,FirstList(S)),Rember(x,TailList(S)))
      else:
         if FirstList(S)== x:
            return Rember(x,TailList(S))
         else:
            return KonsLo(FirstList(S),Rember(x,TailList(S)))
  
# Max: list of list -> elemen
# Max(S) mengembalikan elemen maksimum di dalam list of list
def Max2(a,b):
    if a >= b:
        return a
    else:
        return b
def Max(S):
    if IsOneEmlt(S):
        if isAtom(FirstList(S)):
            return FirstList(S)
        else:
            return Max(FirstList(S))
    else:
        if isAtom(FirstList(S)):
            return Max2(FirstList(S),Max(TailList(S)))
        else:
            return Max2(Max(FirstList(S)),Max(TailList(S)))

# NBElmtAtom: list of list -> integer
# NBElmtAtom(S) mengembalikan banyaknya elemen list of list S yang berupa atom
def NBElmtAtom(S):
    if isEmpty(S):
        return 0
    elif isAtom(FirstList(S)):
        return 1 + NBElmtAtom(TailList(S))
    else:
        return NBElmtAtom(TailList(S))

# NBElmtList: list of list -> integer
# NBElmtList(S) mengembalikan banyaknya elemen list of list S yang berupa list
def NBElmtList(S):
    if isEmpty(S):
        return 0
    elif isList(FirstList(S)):
        return 1 + NBElmtList(TailList(S))
    else:
        return NBElmtList(TailList(S))

# SumLoL: list of list -> integer
# SumLoL(S) mengembalikan jumlah semua elemen dalam list of list S
def SumLoL(S):
    if isEmpty(S):
        return 0
    elif isAtom(FirstList(S)):
        return FirstList(S) + SumLoL(TailList(S))
    else:
        return SumLoL(FirstList(S)) + SumLoL(TailList(S))

# MaxNBElmtList: list of list -> integer
# MaxNBElmtList(S) mengembalikan banyaknya elemen list maksimum yang ada pada list of list S 
def MaxNBElmtList(S):
    if isEmpty(S):
        return 0  
    elif isList(FirstList(S)):
        if NBElmtAtom(FirstList(S)) > MaxNBElmtList(TailList(S)):
            return NBElmtAtom(FirstList(S))
        else:
            return MaxNBElmtList(TailList(S))
    else:
        return MaxNBElmtList(TailList(S))

# MaxSumElmt: list of list -> integer
# MaxSumElmt(S) mengembalikan elemen maksimum pada list of list S
# jika elemen berupa list, maka dihitung jumlahan elemen dalam list tersebut
# jika elemen atom, maka nilainya adalah elemen tersebut 
def MaxSumElmt(S) :
    if IsEmpty(S) :
        return 0
    elif isAtom(FirstList(S)) :
            if FirstList(S) > MaxSumElmt(TailList(S)) :
                return FirstList(S)
            else :
                return MaxSumElmt(TailList(S)) 
    else :
         if SumLoL(FirstList(S)) > MaxSumElmt(TailList(S)) :
            return SumLoL(FirstList(S))
         else :
            return MaxSumElmt(TailList(S))


# APLIKASI
print(f"IsMembers:{IsMemberS(3, [])}")
print(f"IsMembers:{IsMemberS(3, [2, 4, 3, [1], [4,5]])}")
print(f"IsMembers:{IsMemberS(3, [2, 4, 7, [1], [3,5]])}")
print(f"Rember: {Rember(3, [])}")
print(f"Rember: {Rember(3, [4, 3, [2,4], 3])}")
print(f"Rember: {Rember(3, [2, 4, [3,6,9], 5, 3])}")
print(f"Max: {Max([4, 5, 6, [8,9,10], [12,0], 8])}")
print(f"Max: {Max([4, 15, 6, [8,9,10], [12,0], 8])}")
print(f"NBElmtAtom: {NBElmtAtom([4, 5, 6, [8,9,10], [12,0], 8])}")
print(f"NBElmtAtom: {NBElmtAtom([4, 15, 6, [8,9], 10, [12], 8])}")
print(f"NBElmtAtom: {NBElmtAtom([[8,9,10]])}")
print(f"NBElmtList: {NBElmtList([4, 5, 6, [8,9,10], [12,0], 8])}")   
print(f"NBElmtList: {NBElmtList([[4, 15], 6, [8,9], 10, [12], 8])}")   
print(f"NBElmtList: {NBElmtList([[8,9,10]])}")
print(f"SumLoL: {SumLoL([[]])}")
print(f"SumLoL: {SumLoL([4, 5, 6, [2,3,1]])}")
print(f"SumLoL: {SumLoL([[2,3,4]])}")
print(f"MaxNBElmtList: {MaxNBElmtList([[4,5,6,7], [8,9,10], [12,0], 8])}")
print(f"MaxNBElmtList: {MaxNBElmtList([[4,15], 6, [8,9], 10, [12], 8])}")
print(f"MaxNBElmtList: {MaxNBElmtList([8,9,10])}") 
print(f"MaxSumElmt: {MaxSumElmt([[1,2], 9, [4,5,6], 8])}") 
print(f"MaxSumElmt: {MaxSumElmt([[1,2], 90, [4,5,6], 8])}")  
print(f"MaxSumElmt: {MaxSumElmt([8,9,10])}") 
print(f"MaxSumElmt: {MaxSumElmt([[8,9,10]])}")














        

