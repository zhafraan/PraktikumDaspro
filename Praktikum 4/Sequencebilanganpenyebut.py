# Nama file : Sequencebilanganpenyebut.py
# Pembuat   : Aqiatillah Rezi Zhafran
# NIM       : 24060124140124     
# Tanggal   : 24 September 2024
# Deskripsi : Mencari jawaban soal sequence bilangan penyebut

# Definisi dan spesifikasi 
# denumeratirSeq : int -> string
#   [denumeratorSeq (x) untuk menentukan apakah urutan angka x terulang tersebut sesuai dengan desimal hasil pembagian 1 dengan sebuah bilangan bulat]

#Realisasi
def denumeratorSeq(x):
    if ((10 ** len(x))-1) % int(x) == 0:
        return f"Ada: {(10**len(x)-1) // int(x)}"
    else :
        return f"Tidak ada"

print(eval(input()))

#Aplikasi
denumeratorSeq('3')
denumeratorSeq('166')

 