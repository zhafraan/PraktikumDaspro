# Nama File : Binertree _24060124140124.py
# Deskripsi : berisi type dan operasi pohon biner
# Pembuat   : Aqiatillah Rezi Zhafran
# NIM       : 24060124140124
# Tanggal   : 27 November 2024(Dimulai di vs code)

from List_24060124140124 import*

# DEFINISI DAN SPESIFIKASI KONSTRUKTOR
def makePb(A, L, R):
    return [A,L,R]

#DEFINISI DAN SPESIFIKASI SELEKTOR
#Akar :PohonBiner tidak kosong -> Elemen
# { Akar(Pb) adalah Akar dari P. Jika P adalah (A, PN)Akar(P) adalah A }
def Akar(Pb):
    return Pb[0]
#Left: PohonBiner tidak kosong -> PohonBiner
# {Left(Pb) adalah sub pohon kiri dari Pb. Jika P adalah /L,A,R\ = Left (Pb) adalah L }
def Left(Pb):
    return Pb[1]
#Right: PohonBiner tidak kosong -> PohonBiner
# {Right(Pb) adalah sub pohon Kanan dari Pb. Jika P adalah /L,A,R\ = Right (Pb) adalah L }
def Right(Pb):
    return Pb[2]

# DEFINISI DAN SPESIFIKASI PREDIKAT
# isTreeEmpty(Pb) : PohonBiner-> boolean
# {IsTreeEmpty(Pb) true jika P adalah Pohon biner kosong : (//\\) }
def isTreeEmpty(Pb):
    if Pb == None:
        return True
    else:
        return False
# isOneElmt(Pb) : PohonBiner -> boolean
#  {IsOneElement(Pb) true jika Pb hanya mempunyai satu elemen, yaitu akar (//A\\) }
def isOneElmt(Pb):
    if not isTreeEmpty(Pb) and isTreeEmpty(Left(Pb)) and isTreeEmpty(Right(Pb)):
        return True
    else:
        return False
# IsUnerLeft : PohonBiner -> boolean
#  {IsUnerLeft(Pb) true jika Pb hanya mengandung sub pohon kiri tidak kosong: (//L A \\) }  
def IsUnerLeft(Pb):
    if not isTreeEmpty(Pb) and not isTreeEmpty(Left(Pb)) and isTreeEmpty(Right(Pb)):
        return True
    else:
        return False
# IsUnerRight : PohonBiner -> boolean
#  {IsUnerRight(Pb) true jika Pb hanya mengandung sub pohon kanan tidak kosong: (//A R\\) }     
def IsUnerRight(Pb):
    if not isTreeEmpty(Pb) and isTreeEmpty(Left(Pb)) and not isTreeEmpty(Right(Pb)):
        return True
    else:
        return False
# IsBiner : PohonBiner tidak kosong —> boolean
# IsBiner(Pb) true jika Pb mengandung sub pohon kiri dan sub pohon kanan://L A R\\)}  
def IsBiner(Pb):
    if not isTreeEmpty(Pb) and not isTreeEmpty(Left(Pb)) and not isTreeEmpty(Right(Pb)):
        return True
    else:
        return False 
# IsExistLeft:Pohon Biner-> boolean
# IsExistLeft Cek apakah Tree memiliki sub pohon kiri
def IsExistLeft(Pb):
    return not isTreeEmpty(Left(Pb))
# IsExistRight:Pohon Biner-> boolean
# IsExistRight Cek apakah Tree memiliki sub pohon kanan
def IsExistRight(Pb):
    return not isTreeEmpty(Right(Pb))

# DEFINISI DAN SPESIFIKASI PREDIKAT
# NBElmtTree:Pohon Biner--> Integer
# NBElmtTree Menghitung jumlah dari elemen Binary Tree
def NBElmtTree(Pb):
    if isTreeEmpty(Pb):  # Tambahkan kasus untuk pohon kosong
        return 0
    elif isOneElmt(Pb):
        return 1
    elif IsBiner(Pb):
        return 1 + NBElmtTree(Left(Pb)) + NBElmtTree(Right(Pb))
    elif IsUnerLeft(Pb):
        return 1 + NBElmtTree(Left(Pb))
    elif IsUnerRight(Pb):
        return 1 + NBElmtTree(Right(Pb))

# NBDaunTree: Pohon Biner--> Integer
# NBDaunTree Menghitung daun dari sebuah binary tree
def NBDaunTree(Pb):
    if isTreeEmpty(Pb):
        return 0
    elif isOneElmt(Pb):
        return 1
    elif IsBiner(Pb):
        return NBDaunTree(Left(Pb)) + NBDaunTree(Right(Pb))
    elif IsUnerLeft(Pb):
        return NBDaunTree(Left(Pb))
    elif IsUnerRight(Pb):
        return NBDaunTree(Right(Pb))

# DEFINISI DAN SPESIFIKASI PREDIKAT LAIN
# IsMember: PohonBiner, elemen → boolean
# {IsMember(Pb,X) mengirimkan true jika ada node dari Pb yang bernilai X }
def IsMember(Pb, X):
    if isTreeEmpty(Pb):
        return False
    elif Akar(Pb) == X:
        return True
    else:
        return IsMember(Left(Pb), X) or IsMember(Right(Pb), X)
# IsSkewLeft: PohonBiner → boolean
# {IsSkewLeft(Pb) mengirimkan true jika Pb adalah pohon condong kiri }
def IsSkewLeft(Pb):
    if isTreeEmpty(Pb):
        return True
    else:
        if isOneElmt(Pb):
            return True
        else:
            if IsUnerLeft(Pb):
                return IsSkewLeft(Left(Pb))
            else:
                return False

# IsSkewRight: PohonBiner → boolean
# {IsSkewRight(Pb) mengirimkan true jika Pb adalah pohon condong kanan }
def IsSkewRight(Pb):
    if isTreeEmpty(Pb):
        return True
    else:
        if isOneElmt(Pb):
            return True
        else:
            if IsUnerRight(Pb):
                return IsSkewRight(Right(Pb))
            else:
                return False
# DEFINISI DAN SPESIFIKASI FUNGSI LAIN
# LevelOfX: PohonBiner, elemen → integer
# {LevelOfX(Pb,X) Mengirimkan level dari node X yang merupakan salah satu simpul dari pohon biner P}
def LevelOfX(Pb, X):
   if isTreeEmpty(Pb):
        return 0
   elif Akar(Pb) == X:
        return 0 #basis 0
   else:
      if IsMember(Left(Pb), X):
        return 1 + LevelOfX(Left(Pb), X)
      else:
        return 1 + LevelOfX(Right(Pb), X)

# DEFINISI DAN SPESIFIKASI FUNGSI OPERASI LAIN
# AddDaunTerkiri: PohonBiner, elemen→ PohonBiner
# { AddDaunTerkiri(P,X): mengirimkan Pohon Biner P yang telah bertambah simpulnya, dengan X sebagai simpul daun terkiri }
def AddDaunTerkiri(Pb, X):
    if isTreeEmpty(Pb):
        return makePb(X, None, None)  # Jika pohon kosong, buat pohon baru dengan X sebagai akar
    else:
        return makePb(Akar(Pb), AddDaunTerkiri(Left(Pb),X), Right(Pb))

# AddDaun: PohonBiner tidak kosong, elemen, elemen, boolean → PohonBiner
#{ AddDaun (P,X,Y,Kiri): P bertambah simpulnya, dengan Y sebagai anak kiri X (jika Kiri), atau sebagai anak Kanan X (jika not Kiri) {Prekondisi: X adalah salah satu daun Pohon Biner P }
def AddDaun(P, X, Y, Kiri):
    if isTreeEmpty(P):
        raise ValueError("Pohon tidak boleh kosong")  # Prekondisi: P tidak boleh kosong 
    if Akar(P) == X:
        # Jika X adalah akar, tambahkan Y sebagai anak kiri atau kanan
        if Kiri:
            return makePb(Akar(P), makePb(Y, None, None), Right(P))  # Tambah sebagai anak kiri
        else:
            return makePb(Akar(P), Left(P), makePb(Y, None, None))  # Tambah sebagai anak kanan
    else:
        # Jika X bukan akar, cari X di subpohon
        if Left(P) is not None and Akar(Left(P)) == X:
            # Jika X ditemukan di subpohon kiri
            if Kiri:
                raise ValueError("Node sudah memiliki anak kiri")  # Cek jika sudah ada anak kiri
            else:
                return makePb(Akar(P), Left(P), makePb(Y, None, None))  # Tambah sebagai anak kanan
        elif Right(P) is not None and Akar(Right(P)) == X:
            # Jika X ditemukan di subpohon kanan
            if Kiri:
                return makePb(Akar(P), makePb(Y, None, None), Right(P))  # Tambah sebagai anak kiri
            else:
                raise ValueError("Node sudah memiliki anak kanan")  # Cek jika sudah ada anak kanan
        else:
            # Jika X tidak ditemukan di subpohon
            if Left(P) is not None:
                left_child = AddDaun(Left(P), X, Y, Kiri)
            else:
                left_child = None
            if Right(P) is not None:
                right_child = AddDaun(Right(P), X, Y, Kiri)
            else:
                right_child = None
            return makePb(Akar(P), left_child, right_child)

# DelDaunTerkiri: PohonBiner tidak kosong→ <PohonBiner,elemen >
# { DelDaunTerkiri(Pb) menghasilkan sebuah pohon yang dihapus daun terkirinya, dengan X adalah info yang semula disimpan pada daun terkiri yang dihapus }
def DelDaunTerkiri(Pb):
    if isTreeEmpty(Pb):
        raise ValueError("Pohon tidak boleh kosong")  # Prekondisi: P tidak boleh kosong
    elif isOneElmt(Pb):
        return None, Akar(Pb) 
    elif Left(Pb) is not None:
        return makePb(Akar(Pb), DelDaunTerkiri(Left(Pb)), Right(Pb)), DelDaunTerkiri(Left(Pb))
    else:
        return Right(Pb), Akar(Pb) 

# DelDaun: PohonBiner tidak kosong, elemen→ PohonBiner
# { DelDaun(P,X) dengan X adalah salah satu daun, menghasilkan sebuah pohon tanpa X yang semula adalah daun dari P }
def DelDaun(Pb, X):
    if isTreeEmpty(Pb):
        raise ValueError("Pohon tidak boleh kosong")  # Prekondisi: P tidak boleh kosong
    elif isOneElmt(Pb) and Akar(Pb) == X:
        return None  
    elif Akar(Pb) == X:
        return None   
    elif not isTreeEmpty(Left(Pb)):
        if Akar(Left(Pb)) == X and isOneElmt(Left(Pb)):
            return makePb(Akar(Pb), Left(Left(Pb)), Right(Pb))  
        else:
            return makePb(Akar(Pb), DelDaun(Left(Pb), X), Right(Pb))
    else:
        if not isTreeEmpty(Right(Pb)):
            if Akar(Right(Pb)) == X and isOneElmt(Right(Pb)):
                return makePb(Akar(Pb), Left(Pb), Right(Right(Pb))) 
            else:
              return makePb(Akar(Pb), Left(Pb), DelDaun(Right(Pb), X))


# MakeListDaun : PohonBiner  → list Of Node  
# {MakeListDaun(P) : } 
# {Jika P adalah pohon kosong, maka menghasilkan list kosong.  
# {Jika  P  bukan  pohon  kosong:  menghasilkan  list  yang  elemennya  adalah  semua  daun  
# pohon P} 
def MakeListDaun(Pb):
    if isTreeEmpty(Pb):
        return []
    elif isOneElmt(Pb):
        return [Akar(Pb)]
    else:
      return MakeListDaun(Left(Pb)) + MakeListDaun(Right(Pb))

# MakeListPreOrder :  PohonBiner) →list Of Node  
# {MakeListPreOrder(P) : } 
# {Jika P adalah pohon kosong, maka menghasilkan list kosong. } 
# {Jika  P  bukan  pohon  kosong:  menghasilkan  list  yang  elemennya  adalah  semua  node   
# pohon P dengan urutan Preorder} 
def MakeListPreOrder(Pb):
    if isTreeEmpty(Pb):
        return []
    else:
     return [Akar(Pb)] + MakeListPreOrder(Left(Pb)) + MakeListPreOrder(Right(Pb))
    
# MakeListPostOrder :  PohonBiner →list Of Node  
# {MakeListPostOrder(P) : } 
# {Jika P adalah pohon kosong, maka menghasilkan list kosong. } 
# {Jika  P  bukan  pohon  kosong:  menghasilkan  list  yang  elemennya  adalah  semua  node   
# pohon P dengan urutan PostOrder} 
def MakeListPostOrder(Pb):
    if isTreeEmpty(Pb):
        return []
    else:
       return MakeListPostOrder(Left(Pb)) + MakeListPostOrder(Right(Pb)) + [Akar(Pb)]

# MakeListInOrder :  PohonBiner →list Of Node  
# {MakeListInOrder(P) : } 
# {Jika P adalah pohon kosong, maka menghasilkan list kosong. } 
# {Jika  P  bukan  pohon  kosong:  menghasilkan  list  yang  elemennya  adalah  semua  node   
# pohon P dengan urutan InOrder} 
def MakeListInOrder(Pb):
    if isTreeEmpty(Pb):
        return []
    else:
        return MakeListInOrder(Left(Pb)) + [Akar(Pb)] +  MakeListInOrder(Right(Pb))

# MakeListLevel : PohonBiner, integer →list Of Node  
# {MakeListLevel(P,N) : } 
# {Jika P adalah pohon kosong, maka menghasilkan list kosong. } 
# {Jika  P  bukan  pohon  kosong:  menghasilkan  list  yang  elemennya  adalah  semua  node   
# pohon P yang levelnya=N}
def MakeListLevel(Pb, N):
    if isTreeEmpty(Pb):
        return []
    elif N == 0:
        return [Akar(Pb)]
    else:
        return MakeListLevel(Left(Pb), N - 1)+ MakeListLevel(Right(Pb), N - 1)
    
#APLIKASI
p = makePb(5,   
            (makePb(3,
                    makePb(2,
                            None,
                            None),
                    makePb(4,
                            None,
                            None))), 
            (makePb(7,
                    makePb(6,
                            None,
                            None),
                    makePb(8,
                            None,
                            makePb(9,
                                   None,
                                   None)))))

print(f"isTreeEmpty: {isTreeEmpty(p)}")
print(f"isOneElmt: {isOneElmt(p)}")
print(f"IsUnerLeft: {IsUnerLeft(p)}")
print(f"IsUnerRight: {IsUnerRight(p)}")
print(f"IsBiner: {IsBiner(p)}")
print(f"IsExistLeft: {IsExistLeft(p)}")
print(f"IsExistRight: {IsExistRight(p)}")
print(f"NBElmtTree: {NBElmtTree(p)}")
print(f"NBDaunTree: {NBDaunTree(p)}")
print(f"IsMember: {IsMember(p,7)}")
print(f"IsSkewLeft: {IsSkewLeft(p)}")
print(f"IsSkewRight: {IsSkewRight(p)}")
print(f"LevelOfX: {LevelOfX(p,6)}")
print(f"MakeListDaun: {MakeListDaun(p)}")
print(f"MakeListPreOrder: {MakeListPreOrder(p)}")
print(f"MakeListPostOrder: {MakeListPostOrder(p)}")
print(f"MakeListInOrder: {MakeListInOrder(p)}")
print(f"MakeListLevel: {MakeListLevel(p,2)}")

