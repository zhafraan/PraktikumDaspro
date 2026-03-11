# Kamu adalah seorang petualang yang memasuki dunia ajaib bernama Lumerion, 
# tempat di mana setiap keputusan dihitung dengan rumus matematika yang tersembunyi dalam bentuk ekspresi ajaib. 
# Ekspresi ini tersembunyi di dalam list dan mungkin List of List yang rumit, dan hanya petualang cerdas yang bisa memecahkannya.
# Raja Lumerion, Raja Arithmos, memberi kamu misi untuk mengevaluasi ekspresi ini agar dapat membuka gerbang ke ruang harta karun.
# Setiap ekspresi berisi operasi matematika sederhana yang ditulis dalam bentuk list ajaib dengan format: [operator, operand1, operand2]
# Operator yang tersedia:
# '+' untuk membuka pintu dengan penjumlahan kekuatan. '-' untuk menutup jebakan dengan pengurangan energi. '*' untuk menggandakan perlengkapan dengan perkalian sihir. '/' untuk membagi kekuatan secara merata. Operand bisa berupa:
# Sebuah bilangan ajaib (numerik, integer). Sebuah ekspresi list ajaib lainnya (rekursif). Kamu harus membuat fungsi ajaib EvaluateExpression(S) untuk mengevaluasi ekspresi ini. Fungsi tersebut akan memecahkan ekspresi secara rekursif, menavigasi setiap level list untuk menemukan hasil akhir.
# Bantuan: Bila list kosong, keluarkan []
# Input Format
# EvaluateExpression(S)
# Constraints
# -
# Output Format
# integer hasil operasi
# Sample Input 0
# EvaluateExpression(['+', 3, 5])
# Sample Output 0
# 8
# Sample Input 1
# EvaluateExpression(['-', 10, 4])
# Sample Output 1
# 6
def isempty(P):
    return P == []
def operasi(P):
    return P[0]
def angka1(P):
    return P[1]
def angka2(P):
    return P[2]
def EvaluateExpression(S):
    if isempty(S):
        return []
    else:
            if operasi(S) == '+':
                 return angka1(S)+angka2(S)
            elif operasi(S) == '-':
                return angka1(S)-angka2(S)
            elif operasi(S) == '*':
                return angka1(S)*angka2(S)
            elif operasi(S) == '/':
                return angka1(S)/angka2(S)
    
print(eval(input()))

print("============================================================================================================================================================================================================================")
# Pak Tani sedang memanen mangga. Ia mengumpulkan mangga yang matang dalam sebuah wadah besar.
#  Mangga-mangganya selalu dijual ke dua agen. Agen A suka mangga yang memiliki berat ganjil, sedangkan agen B suka mengga yang memiliki berat genap.
#  Bantulah Pak Tani menimbang berat keseluruhan mangga yang akan disetorkan ke agen A atau B.
# Input Format
# Sebuah fungsi sebagai berikut.
# BeratMangga(mangga, agen)
# mangga: list of integer yang elemennya merepresentasikan berat sebuah mangga
# agen: character A atau B
# Constraints
# agen selalu salah satu dari 'A' dan 'B'.
# elemen mangga selalu positif
# Output Format
# Sebuah integer yang merepresentasikan berat mangga yang diterima oleh agen A atau B.
# Sample Input 0
# BeratMangga([1, 2, 4, 5, 7], 'A')
# Sample Output 0
# 13
# Explanation 0
# Agen A (ganjil) sehingga berat total mangganya adalah 1 + 5 + 7 = 13.
# Sample Input 1
# BeratMangga([1, 2, 4, 5, 7], 'B')
# Sample Output 1
# 6
# Explanation 1
# Agen B (genap) sehingga berat total mangganya 2 + 4 = 6.
def Tail(P):
    return P[1:]
def First(P):
    return P[0]
def Last(P):
    return P[-1]
def Buah(P):
    return P[0]
def Agen(P):
    return P[1]
def Isempty(P):
    return P == []

def BeratMangga(mangga, agen):
    if Isempty(mangga):
        return 0
    elif agen == 'A':
        if mangga[0]%2 != 0:
            return mangga[0] + BeratMangga(Tail(mangga),agen)
        else :
            return BeratMangga(Tail(mangga),agen)
    elif agen == 'B':
        if mangga[0]%2 == 0:
            return mangga[0] + BeratMangga(Tail(mangga),agen)
        else :
            return BeratMangga(Tail(mangga),agen)
        
print(eval(input()))
print("=================================================================================================================================================================================================================")
# Senku sedang membuat sebuah robot yang dapat bermain tebak huruf. Jika sebuah huruf terdapat dalam suatu nama, robot tersebut akan mengatakan "YA". 
# Sebaliknya, robot akan mengatakan "TIDAK" jika huruf tersebut tidak berada dalam suatu nama yang diberikan.
#  Bantulah Senku membuat robot tersebut!
# Input Format
# Sebuah fungsi sebagai berikut
# TebakHuruf(huruf, nama)
# huruf terdiri dari sebuah karakter nonkapital.
# nama adalah sebuah list of character yang nonkapital.
# Constraints
# huruf dan nama tidak kosong.
# Output Format
# "YA" jika sebuah huruf ada di dalam suatu nama.
# "TIDAK" jika sebuah huruf tidak ada di dalam suatu nama.
# Sample Input 0
# TebakHuruf('k', ['s', 'e', 'n', 'k', 'u'])
# Sample Output 0
# YA
# Sample Input 1
# TebakHuruf('a', ['b', 'o', 'r', 'u', 't', 'o'])
# Sample Output 1
# TIDAK
def isempty(L):
    return L == []
def firstElmt(L):
    return L[0]
def Tail(L):
    return L[1:]

def TebakHuruf(huruf,nama):
    if isempty(huruf) and isempty(nama):
        return "YA"
    elif isempty(huruf) and not isempty(nama):
        return "TIDAK"
    elif not isempty(huruf) and isempty(nama):
        return "TIDAK"
    elif not isempty(huruf) and not isempty(nama):
        if huruf == firstElmt(nama):
            return "YA"
        else:
            return TebakHuruf(huruf , Tail(nama))
print(eval(input()))
print("=================================================================================================================================================================================================================")
# Terdapat beberapa butir gula yang terjatuh ke lantai. Seperti kata pepatah, "ada gula, ada semut". 
# Sebuah barisan semut menghampiri bongkahan-bongkahan gula tersebut. Barisan semut yang siap menyantap gula ternyata cukup unik. 
# Semut-semut itu dinomori dengan aturan khusus. Semut yang di depan selalu bernomor lebih kecil daripada semut yang di belakangnya.
# Nomor-nomor tersebut adalah kelipatan x yang bukan kelipatan y di mana ada sebanyak n ekor semut berbaris dari depan hingga belakang.
# Input Format
# Sebuah fungsi sebagai berikut
# BarisanSemut(x, y, n)
# x: nomor semut yang paling depan
# y: nomor kelipatan yang dihindari
# n: banyaknya semut
# Constraints
# x, y, n > 0
# x != y
# Output Format
# list of integer yang diurutkan secara ascending dari x hingga sebanyak n dengan semua elemennya bukan kelipatan y.
# Sample Input 0
# BarisanSemut(2, 3, 5)
# Sample Output 0
# [2, 4, 8, 10, 14]
# Explanation 0
# Sebuah barisan dimulai dari 2 dan kelipatannya, tetapi kelipatan 2 dan 3 dilewati.
# Tampak bahwa tidak ada nomor 6 dan 12 karena keduanya adalah kelipatan 2 dan 3.
# Sample Input 1
# BarisanSemut(1, 2, 10)
# Sample Output 1
# [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
def FirstElmt(L):
    return L[0]
def Tail(L):
    return L[1:]
def IsEmpty(L):
    return L == []

def Angka(x, y, n, z):
    if n == 0:
        return []
    elif z % y == 0:
        return Angka(x, y, n, z + x)
    else:
        return [z] + Angka(x, y, n - 1, z + x)
    
def BarisanSemut(x, y, n):
    return Angka(x, y, n, x)
        
print(eval(input()))
print("=================================================================================================================================================================================================================")
# Halo, berjumpa lagi dengan Alexio, ilmuwan terkemuka di Negeri Ufuk Timur!
# Ia sangat senang karena perhitungan kuantitas pengunjung ternyata cukup akurat. 
# Berdasarkan fungsi EstimateGreatLib yang hingga saat ini masih ia gunakan, pengunjung perpustakaan dari hari ke hari selalu naik.
# Semakin ramai, semakin banyak pula kritik dan saran dari pengunjung. Masukan yang paling sering Alexio terima ialah stok buku. 
# Beberapa pengunjung mengeluhkan ada buku yang sangat ingin mereka baca, tetapi belum disediakan di rak buku perpustakaan.
# Kabar keresahan Alexio terdengar oleh Raja Ufuk Timur.
# Baginda Raja yang sangat dermawan menyisihkan sebagian koleksi bukunya untuk Perpustakaan Agung.
# Pagi ini, pegawai dari Istana Raja datang mengirimkan beberapa kardus dengan tag tulisan sebuah genre buku tertentu.
# Kardus tersebut berisi buku-buku yang sesuai dengan tag di kulit kardus. 
# Alexio yang sangat bahagia atas sumbangan buku pun bergegas meletakkan buku-buku ke dalam rak buku.
# Bantulah Alexio meletakkan buku di rak yang sesuai. 
# Hati-hati, Alexio tahu kadang-kadang Baginda Raja bersifat usil, bisa saja ada kardus yang tidak ada isinya. 
# Asumsikan kapasitas rak tidak terbatas.
# Jika ternyata ada tag genre yang belum ada rak bukunya, Alexio perlu membuat rak baru dan meletakkan buku dengan tag genre tersebut.
# Sebuah rak dapat dibentuk dengan syarat minimal ada satu buku. Tidak ada rak tanpa buku.
# Input Format
# AddBooks(shelves, tag, book)
# type shelf: < tag: string, book: list of string >
# type shelves: < rakbuku: list of shelf >
# shelves adalah koleksi objek dari tipe bentukan shelf.
# Constraints
# tag pasti unik
# Output Format
# shelves setelah ditambahkan buku
# Sample Input 0
# AddBooks([['Cerita Anak', ['Matilda', 'Peter Pan']], ['Self Development', ['Atomic Habits', 'The 5 AM Club']]], "Self Development", ['Outliers'])
# Sample Output 0
# [['Cerita Anak', ['Matilda', 'Peter Pan']], ['Self Development', ['Atomic Habits', 'The 5 AM Club', 'Outliers']]]
# Explanation 0
# Shelves terdiri dari dua shelf: Cerita Anak dan Self Development
# Buku yang akan ditambahkan ke dalam rak berjudul 'Outliers' dengan tag 'Self Development' sehingga buku 'Outliers' diletakkan sebagai elemen terakhir dari book dari shelf 'Self Development'. Dengan demikian, dalam shelves terdapat buku 'Outliers' di shelf 'Self Development'.
# Sample Input 1
# AddBooks([['Self Development', ['The 5 AM Club']], ['Biologi', ['Sobotta']], ['Novel', ['Bumi', 'Matahari']], ['Komputer', ['BCI', 'DSA', 'HCI']]], "Fisika", ['A Brief History of Time'])
# Sample Output 1
# [['Self Development', ['The 5 AM Club']], ['Biologi', ['Sobotta']], ['Novel', ['Bumi', 'Matahari']], ['Komputer', ['BCI', 'DSA', 'HCI']], ['Fisika', ['A Brief History of Time']]]
# Explanation 1
# Shelves input tidak memiliki tag "Fisika", sedangkan terdapat kardus berisi buku 'A Brief History of Time' dengan tag tersebut. Alexio perlu membuat shelf/rak baru dengan tag 'Fisika' yang berisi buku dalam kardus tersebut.
# Sample Input 2
# AddBooks([['Novel', ['Toko Kelontong Namiya', 'Bumi', 'The Little Prince']], ['Komputer', ['Clean Code', 'Modern OS', 'Computer Network', 'DSA', 'Algorithms']], ['Biologi', ['Sobotta', 'The Selfish Gene', 'Kepunahan Keenam']], ['Fisika', ['A Brief History of Time', 'The Elegant Universe', 'Astrofisika untuk Orang Sibuk']]], "Komputer", ['Machine Learning', 'BCI'])
# Sample Output 2
# [['Novel', ['Toko Kelontong Namiya', 'Bumi', 'The Little Prince']], ['Komputer', ['Clean Code', 'Modern OS', 'Computer Network', 'DSA', 'Algorithms', 'Machine Learning', 'BCI']], ['Biologi', ['Sobotta', 'The Selfish Gene', 'Kepunahan Keenam']], ['Fisika', ['A Brief History of Time', 'The Elegant Universe', 'Astrofisika untuk Orang Sibuk']]]
def MakeList(a):
    return [a]

def Konso(e, L):
    return [e] + L

def Konsi(L, e):
    return L + [e]

def concatList(L1, L2):
    return L1 + L2

def FirstElmt(L):
    return L[0]

def LastElmt(L):
    return L[-1]

def Head(L):
    return L[:-1]

def Tail(L):
    return L[1:]

def IsEmpty(L):
    return L == []

def FirstList(LoL):
    return LoL[0]

def LastList(LoL):
    return LoL[-1]

def HeadList(LoL):
    return LoL[:-1]

def TailList(LoL):
    return LoL[1:]

def IsEmpty(LoL):
    if LoL == []:
        return True
    else:
        return False

def IsAtom(LoL):
    if type(LoL) == list:
             return False
    else:
        return True

def IsList(LoL):
    if IsAtom(LoL) == False:
        return True
    else:
        return False

# --------------- FUNCTION USED IN ADDBOOKS --------------

# SELEKTOR
def getTag(shelf):
    return FirstElmt(FirstList(shelf))

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

# ----------------- FUNCTION ------------------------

# AddBooks: shelves, string, list -> shelves
# fungsi ini mengeluarkan shelves yang sudah ada dengan menambahkan buku ke sebuah shelf dengan tag tertentu
def AddBooks(shelves, tag, book):
    if IsEmpty(shelves) == True:
        return makeShelf(tag, book)
    else:
        return shelves + [AddToShelf(tag, book)]


# ----------------- APLIKASI ------------------------