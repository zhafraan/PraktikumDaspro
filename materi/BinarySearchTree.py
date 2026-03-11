#NAMA: Raffi Arditama
#NIM : 24060124120020

# DEFINISI DAN SPESIFIKASI KONSTRUKTOR
# MakePB: integer, 2 PohonBiner --> PohonBiner
# MakePB(A, L, R) membuat Pohon Biner yang terdiri dari akar yang berupa elemen, 
# L dan R adalah Pohon Biner yang merupakan sub pohon kiri dan sub pohon kanan
# REALISASI
def MakePB(A, L, R):
    return [A, L, R]

# DEFINISI DAN SPESIFIKASI SELEKTOR
# Akar: PohonBiner --> integer
# Akar(P) mengembalikan akar dari sebuah PohonBiner
# REALISASI
def Akar(P):
    return P[0]

# DEFINISI DAN SPESIFIKASI SELEKTOR
# Left: PohonBiner --> PohonBiner
# Left(P) mengembalikan subpohon kiri dari sebuah PohonBiner
# REALISASI
def Left(P):
    return P[1]

# DEFINISI DAN SPESIFIKASI SELEKTOR
# Right: PohonBiner --> PohonBiner
# Right(P) mengembalikan subpohon kanan dari sebuah PohonBiner
# REALISASI
def Right(P):
    return P[2]

# DEFINISI DAN SPESIFIKASI PREDIKAT
# DEFINISI DAN SPESIFIKASI
# IsTreeEmpty: T --> boolean
# IsTreeEmpty Mengecek apakah Tree kosong
def IsTreeEmpty(T):
    return T == [] 

# DEFINISI DAN SPESIFIKASI
# IsOneElmt: Binary Tree --> boolean
# IsOneElmt Cek apakah Tree hanya satu elemen
def IsOneElmt(T):
    return not IsTreeEmpty(T) and IsTreeEmpty(Left(T)) and IsTreeEmpty(Right(T))

# DEFINISI DAN SPESIFIKASI
# IsUnerLeft: Binary Tree --> boolean
# IsUnerLeft Cek apakah sebuah tree Hanya mengandung sub pohon kiri
def IsUnerLeft(P):
    return not IsTreeEmpty(Left(P)) and IsTreeEmpty(Right(P))

# DEFINISI DAN SPESIFIKASI
# IsUnerRight: Binary Tree --> boolean
# IsUnerRight Cek apakah sebuah tree hanya mengandung sub pohon kanan
def IsUnerRight(P):
    return not IsTreeEmpty(Right(P)) and IsTreeEmpty(Left(P))

# DEFINISI DAN SPESIFIKASI
# IsBiner: Binary Tree --> boolean
# IsBiner Cek apakah Tree mengandung sub pohon kiri dan kanan
def IsBiner(P):
    return not IsTreeEmpty(Right(P)) and not IsTreeEmpty(Left(P))

# DEFINISI DAN SPESIFIKASI
# IsExistLeft: Binary Tree --> boolean
# IsExistLeft Cek apakah Tree memiliki sub pohon kiri
def IsExistLeft(P):
    return not IsTreeEmpty(Left(P))

# DEFINISI DAN SPESIFIKASI
# IsExistRight: Binary Tree --> boolean
# IsExistRight Cek apakah Tree memiliki sub pohon kanan
def IsExistRight(P):
    return not IsTreeEmpty(Right(P))

# DEFINISI DAN SPESIFIKASI SEARCH

# DEFINISI DAN SPESIFIKASI
# NBElmtTree: Binary Tree --> Integer
# NBElmtTree Menghitung jumlah dari elemen Binary Tree
def NBElmtTree(T):
    if IsTreeEmpty(T):  # Tambahkan kasus untuk pohon kosong
        return 0
    elif IsOneElmt(T):
        return 1
    elif IsBiner(T):
        return 1 + NBElmtTree(Left(T)) + NBElmtTree(Right(T))
    elif IsUnerLeft(T):
        return 1 + NBElmtTree(Left(T))
    elif IsUnerRight(T):
        return 1 + NBElmtTree(Right(T))


# DEFINISI DAN SPESIFIKASI
# NBDaunTree: Binary Tree --> Integer
# NBDaunTree Menghitung daun dari sebuah binary tree
def NBDaunTree(T):
    if IsTreeEmpty(T):
        return 0
    elif IsOneElmt(T):
        return 1
    elif IsBiner(T):
        return NBDaunTree(Left(T)) + NBDaunTree(Right(T))
    elif IsUnerLeft(T):
        return NBDaunTree(Left(T))
    elif IsUnerRight(T):
        return NBDaunTree(Right(T))

# DEFINISI DAN SPESIFIKASI
# IsMember: Binary Tree, integer --> boolean
# IsMember Mengecek apakah X ada di dalam Binary Tree
def IsMember(P, X):
    if IsTreeEmpty(P):
        return False
    elif IsOneElmt(P):
        return Akar(P)==X
    elif IsBiner(P):
        if Akar(P)==X:
            return True
        else:
            return IsMember(Left(P),X) or IsMember(Right(P),X)
    elif IsUnerLeft(P):
        if Akar(P)==X:
            return True
        else:
            return IsMember(Left(P),X)
    elif IsUnerRight(P):
        if Akar(P)==X:
            return True
        else:
            return IsMember(Right(P),X)


# DEFINISI DAN SPESIFIKASI
# IsSkewLeft: Binary Tree --> booelan
# IsSkewLeft Cek apakah Binary Tree hanya memiliki node kiri untuk setiap sub pohonya
def IsSkewLeft(P):
    if IsTreeEmpty(P):
        return False
    elif IsOneElmt(P):
        return True
    elif IsBiner(P):
        return False
    elif IsUnerLeft(P):
        return IsSkewLeft(Left(P))
    elif IsUnerRight(P):
        return False

# DEFINISI DAN SPESIFIKASI
# IsSkewRight: Binary Tree --> booelan
# IsSkewRight Cek apakah Binary Tree hanya memiliki node kanan
def IsSkewRight(P):
    if IsTreeEmpty(P):
        return False
    elif IsOneElmt(P):
        return True
    elif IsBiner(P):
        return False
    elif IsUnerLeft(P):
        return False
    elif IsUnerRight(P):
        return IsSkewRight(Right(P))

# DEFINISI DAN SPESIFIKASI
# LevelOfX: Binary Tree, Integer --> Integer
# LevelOfX Mencari level dari X yang dijamin ada di dalam binary tree
def LevelOfX(P, X):
    if IsTreeEmpty(P):
        return 0
    elif IsOneElmt(P) and Akar(P)==X:
        return 1
    elif IsBiner(P):
        if Akar(P)==X:
            return 1
        elif IsMember(Left(P),X):
            return 1 + LevelOfX(Left(P),X) 
        elif IsMember(Right(P),X):
            return 1 + LevelOfX(Right(P),X)
    elif IsUnerLeft(P):
        if Akar(P)==X:
            return 1
        else :
            return 1+LevelOfX(Left(P),X)
    elif IsUnerRight:
        if Akar(P)==X:
            return 1
        else :
            return 1+LevelOfX(Right(P),X)

# DEFINISI DAN SPESIFIKASI
# AddDaunTerkiri: Binary Tree, Integer --> Binary Tree
# AddDaunTerkiri Menambahkan daun terkiri dari Binary Tree
def AddDaunTerkiri(P, X):
    if IsTreeEmpty(P):
        return MakePB(X,[],[])
    elif IsOneElmt(P):
        return MakePB(Akar(P),MakePB(X,[],[]))
    elif IsBiner(P):
        return MakePB(Akar(P),AddDaunTerkiri(Left(P),X),Right(P))
    elif IsUnerLeft(P):
        return MakePB(Akar(P),AddDaunTerkiri(Left(P),X),[])
    elif IsUnerRight(P):
        return MakePB(Akar(P),MakePB(X, [], []),Right(P))

# DEFINISI DAN SPESIFIKASI
# DelDaunTerkiri: Binary Tree --> Binary Tree
# DelDaunTerkiri Menghapus Daun Terkiri dari Binary Tree
def DelDaunTerkiri(P):
    if IsOneElmt(P):
        return []
    elif IsBiner(P):
        return MakePB(Akar(P),DelDaunTerkiri(Left(P)),Right(P))
    elif IsUnerLeft(P):
        return MakePB(Akar(P),DelDaunTerkiri(Left(P)),[])
    elif IsUnerRight(P):
        return MakePB(Akar(P),[],DelDaunTerkiri(Right(P)))

# DEFINISI DAN SPESIFIKASI
# DelDaun: Binary Tree --> Binary Tree
# DelDaun Menghapus Daun X dari Binary Tree jika ada
def DelDaun(P, X):
    if IsOneElmt(P):
        if Akar(P)==X:
            return []
        else:
            return MakePB(Akar(P),[],[])
    elif IsBiner(P):
        return MakePB(Akar(P),DelDaun(Left(P),X),DelDaun(Right(P),X))
    elif IsUnerLeft(P):
        return MakePB(Akar(P),DelDaun(Left(P),X),[])
    elif IsUnerRight(P):
        return MakePB(Akar(P),[],DelDaun(Right(P),X))


# DEFINISI DAN SPESIFIKASI
# RepPrefix: Binary Tree --> List of List
# RepPrefix Mengubah struktur Binary Tree menjadi list of list
def RepPrefix(T):
    return T

# DEFINISI DAN SPESIFIKASI
# MakeListDaun: Binary Tree --> List
# MakeListDaun Membuat List yang berisi elemen dari daun
def MakeListDaun(P):
    if IsTreeEmpty(P):
        return []
    elif IsOneElmt(P):
        return [Akar(P)]
    elif IsBiner(P):
        return MakeListDaun(Left(P))+MakeListDaun(Right(P))
    elif IsUnerLeft(P):
        return MakeListDaun(Left(P))
    elif IsUnerRight(P):
        return MakeListDaun(Right(P))

# DEFINISI DAN SPESIFIKASI
# MakeListPreOrder: Binary Tree --> List
# MakeListPreOrder Mencetak Tree dengan posisi elemen PreOrder
def MakeListPreOrder(P):
    if IsTreeEmpty(P):
        []
    elif IsOneElmt(P):
        return [Akar(P)]
    elif IsBiner(P):
        return [Akar(P)]+MakeListPreOrder(Left(P))+MakeListPreOrder(Right(P))
    elif IsUnerLeft(P):
        return [Akar(P)]+MakeListPreOrder(Left(P))
    elif IsUnerRight(P):
        return [Akar(P)]+MakeListPreOrder(Right(P))

# DEFINISI DAN SPESIFIKASI
# MakeListInOrder: Binary Tree --> List
# MakeListInOrder Mencetak Tree dengan posisi elemen InOrder 
def MakeListInOrder(P):
    if IsTreeEmpty(P):
        return []
    elif IsOneElmt(P):
        return [Akar(P)]
    elif IsBiner(P):
        return MakeListInOrder(Left(P))+[Akar(P)]+MakeListInOrder(Right(P))
    elif IsUnerLeft(P):
        return MakeListInOrder(Left(P))+[Akar(P)]
    elif IsUnerRight(P):
        return [Akar(P)]+MakeListInOrder(Right(P))

# DEFINISI DAN SPESIFIKASI
# MakeListPostOrder: Binary Tree --> List
# MakeListPostOrder Mencetak Tree dengan posisi elemen PostOrder 
def MakeListPostOrder(P):
    if IsTreeEmpty(P):
        return []
    elif IsOneElmt(P):
        return [Akar(P)]
    elif IsBiner(P):
        return MakeListPostOrder(Left(P))+MakeListPostOrder(Right(P))+[Akar(P)]
    elif IsUnerLeft(P):
        return MakeListPostOrder(Left(P))+[Akar(P)]
    elif IsUnerRight(P):
        return MakeListPostOrder(Right(P))+[Akar(P)]

# DEFINISI DAN SPESIFIKASI
# AddX: Tree, integer --> BST
# AddX Menambahkan elemen x ke dalam Tree
def AddX(P, X):
    if IsTreeEmpty(P):
        return MakePB(X,[],[])
    elif IsOneElmt(P):
        if Akar(P)<X:
            return MakePB(Akar(P),[],MakePB(X,[],[]))
        else:
            return MakePB(Akar(P),MakePB(X,[],[]),[])
    elif IsBiner(P):
        if Akar(P)<X:
            return MakePB(Akar(P),Left(P),AddX(Right(P),X))
        else:
            return MakePB(Akar(P),AddX(Left(P),X),Right(P))
    elif IsUnerLeft(P):
        if Akar(P)<X:
            return MakePB(Akar(P),Left(P),MakePB(X,[],[]))
        else:
            return MakePB(Akar(P),AddX(Left(P),X),[])
    elif IsUnerRight(P):
        if Akar(P)<X:
            return MakePB(Akar(P),[],AddX(Right(P),X))
        else:
            return MakePB(Akar(P),MakePB(X,[],[]),Right(P))

def MaxBST(P):
    if IsTreeEmpty(Left(P)): 
        return Akar(P)
    else:
        return MaxBST(Right(P))

# DEFINISI DAN SPESIFIKASI
# DelX: Binary Search Tree, Integer --> BST
# DelX Menghapus elemen X dari Binary Search Tree
def DelX(P, X):
    if IsTreeEmpty(P):  # Pohon kosong
        return P
    elif Akar(P) == X:  
        if IsTreeEmpty(Left(P)) and IsTreeEmpty(Right(P)):
            return [] 
        elif IsTreeEmpty(Right(P)):
            return Left(P)  
        elif IsTreeEmpty(Left(P)):
            return Right(P)
        else:
            return MakePB(MaxBST(Left(P)), DelX(Left(P), MaxBST(Left(P))),Right(P))
    elif X < Akar(P):  # Elemen yang dihapus lebih kecil dari akar
        return MakePB(Akar(P), DelX(Left(P), X), Right(P))
    else:  # Elemen yang dihapus lebih besar dari akar
        return MakePB(Akar(P), Left(P), DelX(Right(P), X))


# DEFINISI DAN SPESIFIKASI
# FindX: BST, integer --> integer
# FindX Mencari jarak dari akar sampai dengan x, x selalu ada di dalam tree
def FindX(P, x):
    if IsOneElmt(P):
        return 0
    elif IsBiner(P):
        if Akar(P)==x:
            return 0
        else:
            if x >= Akar(P):
                return 1+ FindX(Right(P),x)
            else:
                return 1+ FindX(Left(P),x)
    elif IsUnerLeft(P):
        if Akar(P)==x:
            return 0
        else:
            return 1+ FindX(Left(P),x)
    elif IsUnerRight(P):
        if Akar(P)==x:
            return 0
        else:
            return 1+ FindX(Right(P),x) 

# DEFINISI DAN SPESIFIKASI
# MencariSepuh: PohonBiner, 2 integer --> integer
# MencariSepuh(P, ID1, ID2) mengecek lowest common ancestor dari ID1 dan ID2
# REALISASI
def MencariSepuh(P, ID1, ID2):
    if IsOneElmt(P):
        return Akar(P)
    elif ID1<Akar(P) and ID2<Akar(P):
        return MencariSepuh(Left(P),ID1,ID2)
    elif ID1>Akar(P) and ID2>Akar(P):
        return MencariSepuh(Right(P),ID1,ID2)
    elif ID1<Akar(P) and ID2>Akar(P) or ID1>Akar(P) and ID2<Akar(P):
        return Akar(P)
    


print(IsTreeEmpty([]))
print(IsOneElmt(MakePB(10,[],[])))
print(IsUnerLeft(MakePB(10,MakePB(5,[], []), [])))
print(IsUnerRight(MakePB(10,[],MakePB(5,[],[]))))
print(IsBiner(MakePB(10, MakePB(11, [], []), MakePB(12, [], []))))
print(IsExistLeft(MakePB(10, MakePB(11, [], []), MakePB(12, [], []))))
print(IsExistRight(MakePB(10, MakePB(11, [], []), MakePB(12, [], []))))