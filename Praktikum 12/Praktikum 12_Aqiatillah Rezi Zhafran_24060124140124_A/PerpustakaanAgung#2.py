# Nama File : PerpustakaanAgung#2.py
# Deskripsi : SC Hackerrank Perpustakaan Agung 2
# Pembuat   : Aqiatillah Rezi Zhafran
# NIM       : 24060124140124
# Tanggal   : 2 Desember 2024

#DEFINISI DAN SPESIFIKASI KONSTRUKTOR
# MakeList: elemen -> List
# MakeList(a) mengembalikan list yang berisi elemen a sebagai satu-satunya elemen.
def MakeList(a):
    return [a]

# Konso: elemen, List -> List
# Konso(e, L) mengembalikan list baru yang dimulai dengan elemen e diikuti oleh semua elemen dari list L.
def Konso(e, L):
    return [e] + L

# Konsi: List, elemen -> List
# Konsi(L, e) mengembalikan list baru yang berisi semua elemen dari list L diikuti oleh elemen e.
def Konsi(L, e):
    return L + [e]

# concatList: List, List -> List
# concatList(L1, L2) mengembalikan list yang merupakan gabungan dari list L1 dan L2.
def concatList(L1, L2):
    return L1 + L2

# DEFINISI DAN SPESIFIKASI SELEKTOR
# DEFINISI DAN SPESIFIKASI OPERASI
# FirstElmt: List -> elemen
# FirstElmt(L) mengembalikan elemen pertama dari list L.
def FirstElmt(L):
    return L[0]

# LastElmt: List -> elemen
# LastElmt(L) mengembalikan elemen terakhir dari list L.
def LastElmt(L):
    return L[-1]

# Head: List -> List
# Head(L) mengembalikan list yang berisi semua elemen dari L kecuali elemen terakhir.
def Head(L):
    return L[:-1]

# Tail: List -> List
# Tail(L) mengembalikan list yang berisi semua elemen dari L kecuali elemen pertama.
def Tail(L):
    return L[1:]

# IsEmpty: List -> boolean
# IsEmpty(L) benar jika list L kosong.
def IsEmpty(L):
    return L == []

# FirstList: List of list -> List
# FirstList(LoL) mengembalikan list pertama dari list of lists LoL.
def FirstList(LoL):
    return LoL[0]

# LastList: List of list -> List
# LastList(LoL) mengembalikan list terakhir dari list of lists LoL.
def LastList(LoL):
    return LoL[-1]

# HeadList: List of list -> List
# HeadList(LoL) mengembalikan list yang berisi semua list dari LoL kecuali list terakhir.
def HeadList(LoL):
    return LoL[:-1]

# TailList: List of list -> List
# TailList(LoL) mengembalikan list yang berisi semua list dari LoL kecuali list pertama.
def TailList(LoL):
    return LoL[1:]

# IsEmpty: List of list -> boolean
# IsEmpty(LoL) benar jika list of lists LoL kosong.
def IsEmpty(LoL):
    return LoL == []

# DEFINISI PREDIKAT KHUSUS
# IsAtom: list of list -> boolean
# IsAtom(LoL) mengembalikan True jika LoL bukan list (yaitu, merupakan atom),
# dan False jika LoL adalah list.
def IsAtom(LoL):
    if type(LoL) == list:
        return False
    else:
        return True

# IsList: list of list -> boolean
# IsList(LoL) mengembalikan True jika LoL adalah list,
# dan False jika LoL bukan list (yaitu, merupakan atom).
def IsList(LoL):
    if IsAtom(LoL) == False:
        return True
    else:
        return False

# DEFINISI DAN SPESIFIKASI SELEKTOR
# getTag: shelf -> string
# getTag(shelf) mengembalikan elemen pertama dari list pertama dalam list of lists shelf.
# Fungsi ini digunakan untuk mendapatkan tag dari rak buku.
def getTag(shelf):
    return FirstElmt(FirstList(shelf))

# getBooks: shelf -> string
# getBooks(shelf) mengembalikan elemen terakhir dari list pertama dalam list of lists shelf.
# Fungsi ini digunakan untuk mendapatkan daftar buku dari rak buku.
def getBooks(shelf):
    return LastElmt(FirstList(shelf))

# FUNGSI KHUSUS
# bersifat opsional, tidak harus digunakan
# boleh buat fungsi antara sendiri

# makeShelf: string, list -> shelf
# fungsi ini membuat sebuah shelf baru dengan komponen tag dan book
def makeShelf(tag, book):
    return [[tag] + [book]]

# AddToShelf: string, list -> shelf
# fungsi ini menambahkan buku ke sebuah shelf dengan tag tertentu
def AddToShelf(tag, book):
    return [tag] + [book]

def cekTag(shelves,tag, book):
    if IsEmpty(shelves):
        return False
    else:
        if getTag(shelves) == tag:
            return True
        else:
            return cekTag(TailList(shelves), tag,book)
        
# AddBooks: shelves, string, list -> shelves
# fungsi ini mengeluarkan shelves yang sudah ada dengan menambahkan buku ke sebuah shelf dengan tag tertentu
def AddBooks(shelves, tag, book):
    if IsEmpty(book):
        return shelves
    elif IsEmpty(shelves):
        return []
    else:
        if not cekTag(shelves,tag, book):
            return Konsi(shelves, AddToShelf(tag, book))
        else:
            if cekTag(shelves,tag, book) and getTag(shelves) != tag:
                 return Konso(FirstList(shelves), AddBooks(TailList(shelves),tag,book))
            else:
                 return Konso([getTag(shelves),getBooks(shelves) + book], AddBooks(TailList(shelves),tag,[]))
# APLIKASI

print(AddBooks([['Cerita Anak', ['Matilda', 'Peter Pan']], ['Self Development', ['Atomic Habits', 'The 5 AM Club']]], "Self Development", ['Outliers']))
print(AddBooks([['Self Development', ['The 5 AM Club']], ['Biologi', ['Sobotta']], ['Novel', ['Bumi', 'Matahari']], ['Komputer', ['BCI', 'DSA', 'HCI']]], "Fisika", ['A Brief History of Time']))
print(AddBooks([['Novel', ['Toko Kelontong Namiya', 'Bumi', 'The Little Prince']], ['Komputer', ['Clean Code', 'Modern OS', 'Computer Network', 'DSA', 'Algorithms']], ['Biologi', ['Sobotta', 'The Selfish Gene', 'Kepunahan Keenam']], ['Fisika', ['A Brief History of Time', 'The Elegant Universe', 'Astrofisika untuk Orang Sibuk']]], "Komputer", ['Machine Learning', 'BCI']))
