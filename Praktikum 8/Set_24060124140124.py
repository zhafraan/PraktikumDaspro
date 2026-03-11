# Nama File : Set_24060124140124.py
# Deskripsi : berisi type dan operasi set yang menggunakan list
# Pembuat   : Aqiatillah Rezi Zhafran
# NIM       : 24060124140124
# Tanggal   : 4 November 2024(dimulai di vs code)

# DEFINISI DAN SPESIFIKASI TYPE
# Set adalah sebuah list dengan syarat setiap elemen harus unik
# Semua konstruktor, selektor, dan operasi yang telah didefinisikan
#   untuk list juga berlaku pada set

from List_24060124140124 import*

# DEFINISI DAN SPESIFIKASI OPERASI LIST YANG DIPERLUKAN UNTUK HIMPUNAN
# Rember: elemen, list -> list
# Rember(x,L) menghapus sebuah elemen x dari list L
#   Jika x ada di list L, maka elemen L berkurang 1.
#   Jika x tidal( ada di list L maka L tetap.
#   List kosong tetap menjadi list kosong.

def rember(x,L):
    if(IsEmpty(L)):
        return []
    else:
        if(FirstElmt(L)== x):
         return Tail(L)
        else:
           return Konso(FirstElmt(L),rember(x,Tail(L)))
        
# APLIKASI
print(f"rember: {rember(2, [])}")
print(f"rember: {rember(2, [3])}")
print(f"rember: {rember(5, [3, 4, 5, 2, 3, 5, 7, 8, 2])}")

print("===============================================================================================================================================")


# DEFINISI DAN SPESIFIKASI OPERASI LIST YANG DIPERLUKAN UNTUK HIMPUNAN
# Rember: elemen, list -> list
# Rember(x,L) menghapus sebuah elemen x dari list L
# Jika x ada di list L, maka elemen L berkurang 1. 
# Jika x tidak ada di list L maka L tetap.
# List kosong tetap menjadi list kosong.
def Rember2(x,L):
   if IsEmpty(L):
      return[]
   else:
      if LastElmt(L)== x:
         return Head(L)
      else:
         return Konsi(Rember2(x,Head(L)),LastElmt(L))

# MultiRember: elemen, list -> list
# MultiRember(x,L) menghapus semua kemunculan elemen x dari list L. 
# List baru yang dihasilkan tidak lagi memiliki elemen x. 
# List kosong tetap menjadi list kosong.
def MultiRamber(x,L):
   if IsEmpty(L):
      return[]
   else:
      if (FirstElmt(L)== x):
         return MultiRamber(x,Tail(L))
      else:
         return Konso(FirstElmt(L),MultiRamber(x,Tail(L)))

# DEFINISI DAN SPESIKASI KONSTRUKTOR SET DARI LIST
# MakeSet: list -> set 
# MakeSet(L) membuat set dari list L dengan menghapus semua kemunculan lebih dari satu kali
# list kosong tetap menjadi himpunan kosong
def MakeSet1(L):
        if IsEmpty(L):
            return []
        else :
            if IsMember(FirstElmt(L), Tail(L)):  
                return MakeSet1(Tail(L))
            else:
                return Konso(FirstElmt(L),MakeSet1(Tail(L)))
def MakeSet2(L):
   if IsEmpty(L):
      return []
   else:
      return Konso(FirstElmt(L),MakeSet2(MultiRamber(FirstElmt(L),Tail(L))))

# DEFINISI DAN SPESIKASI KONSTRUKTOR SET 
# KonsoSet: elemen,set -> set 
# konsoSet(e,H) menambahkan sebuah elemen e sebagai elemen pertama set H 
# dengan syarat e belum ada di dalam himpunan H
def Konsoset(e,H):
   if IsMember(e,Tail(H)):
      return H
   else:
      return Konso(e,H)

# DEFINISI DAN SPESIFIKASI PREDIKAT
# IsSet: list -> boolean
# IsSet(L) mengembalikan true jika L adalah sebuah set
def IsSet(L):
   if IsEmpty(L):
      return True
   else:
      if IsMember(FirstElmt(L),Tail(L)):
         return False
      else:
         return IsSet(Tail(L))


# IsSubset: 2 set -> boolean
# IsSubset(H1,H2) mengembalikan true jika H1 merupakan subset dari H2
def IsSubset(H1,H2):
   if IsEmpty(H1):
      return True
   else:
     if not IsMember(FirstElmt(H1),H2):
      return False
     else:
      return IsSubset(Tail(H1),H2)


# IsEqualSet: 2 set -> boolean
# IsEqualSet(H1,H2) benar jika H1 adalah set yang sama dengan H2
# if A then B else false
def IsEqualSet(H1,H2):
   if IsSubset(H1,H2) and IsSubset(H2,H1):
      return True
   else:
      return False

def IsEqualset2(H1,H2):
   if IsEmpty(H1) and IsEmpty(H2):
      return True
   elif not IsEmpty(H1) and IsEmpty(H2):
      return False
   elif IsEmpty(H1) and not IsEmpty(H2):
      return False
   else:
      if IsMember(FirstElmt(H1),H2):
         return IsEqualset2(Tail(H1),rember(FirstElmt(H1),H2))
      else:
         return False

# IsIntersect: 2 set -> boolean
# IsIntersect(H1,H2) benar jika H1 beririsan dengan H2
def IsIntersect(H1,H2):
   if IsEmpty(H1) and  IsEmpty(H2):
      return False
   elif not IsEmpty(H1) and IsEmpty(H2):
      return False
   elif IsEmpty(H1) and not IsEmpty(H2):
      return False
   elif  not IsEmpty (H1) and not IsEmpty(H2):
      return IsMember(FirstElmt(H1),H2) or IsIntersect(Tail(H1),H2)

            

# DEFINISI DAN SPESIFIKASI OPERASI TERHADAP HIMPUNAN
# MakeIntersect: 2 set -> set
# MakeIntersect(H1,H2) menghasilkan set baru yang merupakan hasil irisan antara H1 dan H2
def MakeIntersect(H1,H2):
   if IsEmpty(H1) and  IsEmpty(H2):
      return []
   elif not IsEmpty(H1) and IsEmpty(H2):
      return []
   elif IsEmpty(H1) and not IsEmpty(H2):
      return []
   else:
      if IsMember(FirstElmt(H1),H2):
         return Konso(FirstElmt(H1),MakeIntersect(Tail(H1),H2))
      else:
         return MakeIntersect(Tail(H1),H2)

# MakeUnion: 2 set -> set
# MakeUnion(H1,H2) menghasilkan set baru yang merupakan hasil gabungan antara H1 dan H2
def  MakeUnion(H1,H2):
   if IsEmpty(H1) and IsEmpty(H2):
      return []
   elif not IsEmpty(H1) and IsEmpty(H2):
      return H1
   elif IsEmpty(H1) and not IsEmpty(H2):
      return H2
   else:
      if IsMember(FirstElmt(H1),H2):
         return MakeUnion(Tail(H1),H2)
      else:
         return Konso(FirstElmt(H1),MakeUnion(Tail(H1),H2))

# NBIntersect: 2 set -> integer
# NBIntersect(H1,H2) menghasilkan jumlah elemen yang beririsan pada H1 dan H2
# tanpa memanfaatkan fungsi MakeIntersect(H1,H2).
def NBIntersect(H1,H2) :
    if IsEmpty(H1) :
        return 0
    else : 
        if IsMember(FirstElmt(H1), H2):
              return NBIntersect(Tail(H1), H2)
        else :
           return 1 + NBIntersect(Tail(H1), H2)



# NBUnion: 2 set -> integer
# NBUnion(H1,H2) menghasilkan jumlah elemen hasil gabungan antara H1 dan H2
# tanpa memanfaatkan fungsi MakeUnion(H1,H2).
def NBUnion(H1, H2):
    if IsEmpty(H1):
       return NbElmt(H2)
    elif IsMember(FirstElmt(H1), H2):
       return NBUnion(Tail(H1), H2)
    else:
       if not IsMember(FirstElmt(H1), H2):
          return 1 + NBUnion(Tail(H1), H2)
             
# APLIKASI
print(f"Rember2: {Rember2(2, [3, 4, 5, 2, 3, 5, 7, 8, 2])}")
print(f"MultiRamber: {MultiRamber(5, [3, 4, 5, 2, 3, 5, 7, 8, 2])}")
print(f"MakeSet1: {MakeSet1([3, 4, 5, 2, 3, 5, 7, 8, 2])}") 
print(f"MakeSet2: {MakeSet2([3, 4, 5, 2, 3, 5, 7, 8, 2])}")
print(f"Konsoset: {Konsoset([9, 10], [5, 3, 9, 7, 2])}")
print(f"IsSet: {IsSet([5, 3, 9, 7, 2])}")
print(f"IsSubset: {IsSubset([1, 2, 3], [3, 2, 1])}")
print(f"IsEqualSet: {IsEqualSet([1, 2, 3], [3, 2, 1])}")
print(f"IsEqualset2: {IsEqualset2([1, 2, 3], [3, 2, 1])}")
print(f"IsIntersect: {IsIntersect([1, 2, 3], [3, 4, 2])}")
print(f"MakeIntersect: {MakeIntersect([9, 8, 6, 4, 5], [8, 4, 2, 9])}")
print(f"MakeUnion: {MakeUnion([1, 2, 3, 4], [5, 6, 7, 8])}")
print(f"NBIntersect: {NBIntersect([1, 2, 3, 4], [3, 4])}")
print(f"NBUnion: {NBUnion([1, 2, 3, 4], [5, 6, 7, 8])}")
