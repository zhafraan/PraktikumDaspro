from BinaryTree_24060124140138 import *

# DEFINISI DAN SPESIFIKASI PREDIKAT
# BSearchX: BinSearchTree, elemen -> boolean
# BSearchX(P,X) mengerimkan true jika ada node dari Pohon Binary Search Tree P yang bernilai x, dan false jika tidak ada.
# REALISASI
def BSearchX(P, X):
    if isTreeEmpty(P):
        return False
    else:
        if X == Akar(P):
            return True
        else:
            return BSearchX(Left(P), X) or BSearchX(Right(P), X)

# AddX: BinSearchTree, elemen -> PohonBiner
# AddX(P,X) menghasilkan sebuah pohon Binary Search Tree P dengan tambahan simpul X. Belum ada simpul P yang bernilai X.
# REALISASI
def AddX(P, X):
    if not BSearchX(P, X):
        if isTreeEmpty(P):
            return MakePB(X, [], [])
        else:
            if X >= Akar(P):
                return MakePB(Akar(P), Left(P), AddX(Right(P), X))
            else:
                return MakePB(Akar(P), AddX(Left(P), X), Right(P))
        
# MakeBinSearchTree: list of elemen -> PohonBiner
# MakeBinSearchTree(L) menghasilkan sebuah pohon Binary Search Tree P yang elemennya berasal dari elemen list L yang dijamin unik.
# REALISASI
def MakeBST(L):
    if isTreeEmpty(L):
        return L
    else:
        return AddX(MakeBST(Head(L)), LastElmt(L))

# DelBtree: BinSearchTree tidak kosong, elemen -> PohonBiner
# DelBtree(P,X) menghasilkan sebuah pohon Binary Search P tanpa node yang bernilai X. X pasti ada sebagai salah satu node Binary Seach Tree.
#   Menghasilkan Binary SearchTree yang "kosong" jika P hanya terdiri dari x
def Delete(P, X):
    if isTreeEmpty(P):
        return []
    else:
        if Akar(P) == X:
            if isTreeEmpty(Left(P)) and isTreeEmpty(Right(P)):
                return []
            else:
                if isTreeEmpty(Left(P)):
                    return MakePB(Akar(Right(P)), Left(P), Right(Right(P)))
                else:
                    return MakePB(Akar(Left(P)), Left(Left(P)), Right(P))

        elif X > Akar(P):
            return MakePB(Akar(P), Left(P), Delete(Right(P), X))
        else:
            return MakePB(Akar(P), Delete(Left(P), X), Right(P)) 


# APLIKASI
print(BSearchX(MakePB(10, [5, [], []], [20, [], []]), 20))
print(BSearchX(MakePB(10, [5, [], []], [20, [], []]), 30))
print(BSearchX(AddX(MakePB(10, [5, [], []], [20, [], []]), 15), 15))
print(BSearchX(MakeBST([10, 5, 20, 15, 25]), 15))
print(BSearchX(MakeBST([10, 5, 20, 15, 25]), 100))
print(BSearchX(Delete(MakePB(10, [5, [], []], [20, [], []]), 15), 15)) 