# Nama File : Bst _24060124140124.py
# Deskripsi : berisi type dan operasi binary search tree
# Pembuat   : Aqiatillah Rezi Zhafran
# NIM       : 24060124140124
# Tanggal   : 30 November 2024(Dimulai di vs code)

from binerTree_24060124140124 import*

# BSearchX : BinSearchTree, elemen → boolean 
# { BsearchX(P,X) Mengirimkan true jika ada node  dari Pohon Binary Search Tree P yang 
# bernilai X, mengirimkan false jika tidak ada} 
def BSearchX(P,X):
    if isTreeEmpty(P):
        return False
    else:
        if Akar(P) == X:
            return True
        elif Akar(P) < X:
            return BSearchX(Right(P),X)
        else:
            return BSearchX(Left(P),X)
        
# AddX: BinSearchTree, elemen → PohonBiner 
# { AddX(P,X) Menghasilkan sebuah pohon Binary Search Tree P dengan tambahan simpul 
# X. Belum ada simpul P yang bernilai X } 
def AddX(P,X):
    if isTreeEmpty(P):
        return makePb(X, None, None)
    elif Akar(P) <= X:
        return makePb(Akar(P), Left(P), AddX(Right(P),X))
    else:
        return makePb(Akar(P), AddX(Left(P),X), Right(P))
 
# MakeBinSearchTree: list of elemen → PohonBiner 
# { MakeBinSearchTree(Ls) Menghasilkan sebuah pohon Binary Search Tree P yang 
# elemennya berasal dari elemen list Ls yang dijamin unik. } 
def MakeBinSearchTree(L):
    if IsEmpty(L):
        return None
    else:
        return AddX(MakeBinSearchTree(Tail(L)),Akar(L))
    
# DelBtree: BinSearchTree tidak kosong, elemen  → PohonBiner 
# {DelBTree(P,X) menghasilkan sebuah pohon binary search P tanpa node  yang bernilai X. 
# X pasti ada sebagai salah satu node  Binary Search Tree. Menghasilkan Binary 
# SearchTree yang “kosong” jika P hanya terdiri dari X }
def DelBTree(P,X):
    if isTreeEmpty(P):
        return None
    else:
        if Akar(P) == X:
            if isTreeEmpty(Left(P)) and isTreeEmpty(Right(P)):
                return None
            else:
                if isTreeEmpty(Left(P)):
                    return makePb(Akar(Right(P)), Left(P), Right(Right(P)))
                else:
                    return makePb(Akar(Left(P)), Left(Left(P)), Right(P))
        elif X > Akar(P):
            return makePb(Akar(P), Left(P), DelBTree(Right(P), X))
        else:
            return makePb(Akar(P), DelBTree(Left(P), X), Right(P))

print(f"BSearchX:{BSearchX(p,7)}")
print(f"AddX:{AddX(p,5)}")
print(f"MakeBinSearchTree:{MakeBinSearchTree([10, 5, 20, 15, 25])}")
print(f"DelBTree:{DelBTree(p,6)}")