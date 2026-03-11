from list_24060124140138 import *

# DEFINISI TYPE
# Type PohonBiner: <A: integer, L: PohonBiner, R: PohonBiner>
# Pohon Biner terdiri dari akar yang berupa elemen, 
# L dan R adalah Pohon Biner yang merupakan sub pohon kiri dan sub pohon kanan

# DEFINISI DAN SPESIFIKASI KONSTRUKTOR
# MakePB: integer, 2 PohonBiner --> PohonBiner
# MakePB(A, L, R) membuat Pohon Biner yang terdiri dari akar yang berupa elemen, 
# L dan R adalah Pohon Biner yang merupakan sub pohon kiri dan sub pohon kanan
# REALISASI
#PREFIX
def MakePB (A,L,R):
    return [A,L,R]

# Akar: PohonBiner tidak kosong→ Elemen
# { Akar(P) adalah Akar dari P. Jika P adalah //L A R\\ = Akar(P) adalah A}
def Akar (P):
    return P[0]

# Left: PohonBiner tidak kosong PohonBiner
# {Left(P) adalah sub pohon kiri dari P. Jika P adalah //LA R\\, Left (P) adalah L}

def Left(P):
    return P[1]

# Right: PohonBiner tidak kosong → PohonBiner
# (Right(P) adalah sub pohon kanan dari P. Jika P adalah //LA R\\, Right (P) adalah R)
def Right(P):
    return P[2]

# isTreeEmpty: PohonBiner → boolean
# {isTreeEmpty(P) true jika P kosong: (//\\)}
def isTreeEmpty(P):
    return P == []

# IsOneElmt : PohonBiner → boolean
# {IsOneElement(P) true jika P hanya mempunyai satu elemen, yaitu akar (// A \\\)}
def IsOneElementPB(P):
    return not isTreeEmpty(P) and not IsExistLeftPB(P) and not IsExistRightPB(P)
  

# IsUnerLeft: PohonBiner → boolean
# {IsUnerLeft(P) true jika P hanya mengandung sub pohon kiri tidak kosong: (//L A \\)}
def IsUnerLeftPB(P):
    return not isTreeEmpty(P) and not isTreeEmpty(Left(P)) and isTreeEmpty(Right(P))

# IsUnerRight: PohonBiner → boolean
# {IsUnerRight (P) true jika P hanya mengandung sub pohon kanan tidak kosong: (//A R\\)}
def IsUnerRIghtPB(P):
    return not isTreeEmpty(P) and isTreeEmpty(Left(P)) and not isTreeEmpty(Right(P))


# IsBiner: PohonBiner tidak kosong → boolean
# {IsBiner(P) true jika P mengandung sub pohon kiri dan sub pohon kanan :
def IsBinerPB(P):
    return not isTreeEmpty(P) and IsExistLeftPB(P) and IsExistRightPB(P)


# IsExistLeft: PohonBiner tidak kosong → boolean
# {IsExistLeft (P) true jika P mengandung sub pohon kiri }
def IsExistLeftPB(P):
    return not isTreeEmpty(P) and not isTreeEmpty(Left(P)) and Akar(Left(P)) != []

# IsExistRight: PohonBiner tidak kosong → boolean
# {ExistRight(P) true jika P mengandung sub pohon kanan }
def IsExistRightPB(P):
    return not isTreeEmpty(P) and not isTreeEmpty(Right(P)) 

# NbElmt: PohonBiner → integer ≥ 0
# {NbElmt(P) memberikan Banyaknya elemen dari pohon P:
# Basis:
# NbElmt (//A\\) = 1
# Rekurens: NbElmt (//L,A,R\\) = NbElmt(L) +1 + NbELmt(R)
# NbElmt (//L,A,\) = NbElmt(L) + 1
# NbElmt (//A,R\\) = 1 + NbELmt(R) }
def NBElement(P):
    if IsOneElementPB(P):
        return 1
    else:
        if IsBinerPB(P):
            return NBElement(Left(P)) + 1 + NBElement(Right(P))
        elif IsUnerLeftPB(P):
            return NBElement(Left(P)) + 1
        elif IsUnerRIghtPB(P):
            return 1 + NBElement(Right(P))

# NbDaunPB: PohonBiner → integer ≥ 1
# {Prekondisi: Pohon P tidak kosong}
# {NbDaun (P) memberikan Banyaknya daun dari pohon P:
# Basis: NbDaun1 (//A\\) = 1
# Rekurens: NbDaun1 (//L,A,R\\) = NbDaunl (L) + NbDaunl(R)
# NbDaun 1 (//L,A,\\) NbDauni (L)
# NbDaunl (//A,R\\) = NbDaunl (R)
def NbDaunPB(P):
    if isTreeEmpty(P):
        return 0
    else:
        if IsOneElementPB(P):
            return 1
        elif IsBinerPB(P):
            return NbDaunPB(Left(P)) + NbDaunPB(Right(P))
        elif IsUnerLeftPB(P):
            return NbDaunPB(Left(P))
        elif IsUnerRIghtPB(P):
            return NbDaunPB(Right(P))

# RepPrefix: PohonBiner →  list of element
# {RepPrefix (P) memberikan representasi linier (dalam bentuk list), dengan urutan elemen list sesuai dengan urutan penulisan pohon secara prefix:
# Basis: RepPrefix (//A\\) = [A]
# Rekurens: RepPrefix (//L,A,R\\) = [A] o RepPrefix(L) o RepPrefix (R)
# RepPrefix (//L,A\\) = [A] o RepPrefix(L)
# RepPrefix (//A,R\\) = [A] o RepPrefix (R)
def RefPrefix(P):
    if isTreeEmpty(P):
        return []
    else:
        if IsOneElementPB(P):
            return [Akar(P)]
        else:
            if IsBinerPB(P):
                return [Akar(P)] + RefPrefix(Left(P)) + RefPrefix(Right(P))
            elif IsUnerLeftPB(P):
                return [Akar(P)] + RefPrefix(Left(P))
            elif IsUnerRIghtPB(P):
                return [Akar(P)] + RefPrefix(Right(P))

# DEFINISI DAN SPESIFIKASI PREDIKAT LAIN
# IsMember: PohonBiner, elemen -> boolean 
# {IsMember(P,X) Mengirimkan true jika ada node dari P yg bernilai X} 
# REALISASI
def IsMember(P, X):
    if isTreeEmpty(P):
        return False
    else:
        if Akar(P) == X:
            return True
        elif IsBinerPB(P):
            return IsMember(Left(P), X) or IsMember(Right(P), X)
        elif IsUnerLeftPB(P):
            return IsMember(Left(P), X)
        elif IsUnerRIghtPB(P):
            return IsMember(Right(P), X)
        

# {fungsi lain} 
# IsSkewLeft: PohonBiner -> boolean 
# {IsSkewLeft(P) Mengirimkan true jika P adalah pohon condong kiri } 
# REALISASI
def IsSkewLeft(P):
    if isTreeEmpty(P):
        return True
    else:
        if IsBinerPB(P):
            return IsSkewLeft(Left(P)) and IsOneElementPB(Right(P))
        elif IsUnerLeftPB(P):
            return IsSkewLeft(Left(P))
        elif IsUnerRIghtPB(P):
            return False
        

# IsSkewRight: PohonBiner -> boolean 
# {IsSkewRight(P) Mengirimkan true jika P adalah pohon condong kiri } 
# REALISASI
def IsSkewRight(P):
    if isTreeEmpty(P):
        return True
    else:
        if IsBinerPB(P):
            return IsOneElementPB(Left(P)) and IsSkewRight(Right(P))
        elif IsUnerLeftPB(P):
            return False
        elif IsUnerRIghtPB(P):
            return IsSkewRight(Right(P))
        

# LevelOfX: PohonBiner, elemen -> integer 
# {LevelOfX(P,X) Mengirimkan level dari node X yang merupakan salah satu simpul dari pohon biner P}
# REALISASI
def LevelOfX(P, X):
    if isTreeEmpty(P):
        return -1
    else:
        if Akar(P) == X:
            return 0
        elif IsBinerPB(P):
            return 1 + max(LevelOfX(Left(P), X), LevelOfX(Right(P), X))
        elif IsUnerLeftPB(P):
            return 1 + LevelOfX(Left(P), X)
        elif IsUnerRIghtPB(P):
            return 1 + LevelOfX(Right(P), X)
        

# APLIKASI
print(MakePB(1, [2, [], []], [3, [], []]))
print(Akar(MakePB(1, [2, [], []], [3, [], []])))
print(Left(MakePB(1, [2, [], []], [3, [], []])))  
print(Right(MakePB(1, [2, [], []], [3, [], []])))  
print(isTreeEmpty(MakePB(1, [2, [], []], [3, [], []])))  
print(isTreeEmpty(Left(MakePB(1, [2, [], []], [3, [], []])))) 
print(isTreeEmpty(Right(MakePB(1, [2, [], []], [3, [], []])))) 
print(IsOneElementPB(MakePB(1, [], [])))
print(IsOneElementPB(MakePB(1, [2, [], []], [3, [], []])))
print(IsUnerLeftPB(MakePB(1, [2, [], []], [])))
print(IsUnerLeftPB(MakePB(1, [], [3, [], []])))
print(IsUnerRIghtPB(MakePB(1, [], [3, [], []]))) 
print(IsUnerRIghtPB(MakePB(1, [2, [], []], []))) 
print(IsBinerPB(MakePB(1, [2, [], []], [3, [], []])))
print(IsBinerPB(MakePB(1, [2, [], []], [])))  
print(IsBinerPB(MakePB(1, [], [3, [], []]))) 
print(IsExistLeftPB(MakePB(1, [2, [], []], [])))
print(IsExistLeftPB(MakePB(1, [], [3, [], []]))) 
print(IsExistRightPB(MakePB(1, [2, [], []], [3, [], []])))
print(IsExistRightPB(MakePB(1, [2, [], []], [])))  
print(NBElement(MakePB(1, [2, [], []], [3, [], []])))  
print(NBElement(MakePB(1, [2, [], []], []))) 
print(NbDaunPB(MakePB(1, [2, [], []], [])))  
print(NbDaunPB(MakePB(1, [], [3, [], []])))
print(RefPrefix(MakePB('a', [], [])))  
print(IsMember(MakePB(1, [2, [], []], [3, [], []]), 2)) 
print(IsMember(MakePB(1, [2, [], []], []), 3))
print(IsSkewLeft(MakePB(1, [2, [], []], []))) 
print(IsSkewLeft(MakePB(1, [], [3, [], []])))
print(IsSkewRight(MakePB(1, [2, [], []], []))) 
print(IsSkewRight(MakePB(1, [], [3, [], []]))) 
print(LevelOfX(MakePB(1, [], [3, [], []]), 3)) 
print(LevelOfX(MakePB(1, [], []), 1))
