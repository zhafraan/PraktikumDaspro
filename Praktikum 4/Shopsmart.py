# Nama file : Shopsmart.py
# Pembuat   : Aqiatillah Rezi Zhafran
# NIM       : 24060124140124
# Tanggal   : 24 September 2024
# Deskripsi : Mencari jawaban dari soal shop smart

# Definisi dan spesifikasi 
# harga_after_some_variables : 3 int -> int
#   [harga_after_some_variables (harga,kategori,VIP) adalah fungsi untuk menghitungharga sebuah barang setelah dikenakan diskon berdasarkan kategori dan membership VIP]
# pajak_lokasi : 2 int -> int
#   [pajak_lokasi (lokasi,harga) adalah fungsi untuk mencari harga setelah dikenakan pajak berdasarkan lokasi "dalam negeri" maupun "luar negeri"]
# kondisi_hari : 4 int -> int
#   [kondisi hari (harga,hari,VIP,kategori) adalah fungsi untuk mencari harga barang setelah dikenakan pajak atau diskon pada hari hari tertentu "Rabu", "Jumat", "Sabtu", dan "Minggu"]
# hargaAkhir : 5 int -> int
#   [hargaAkhir (harga, kategori, VIP, lokasi, hari) adalah fungsi untuk mencari harga akhir dari barang setelah dikenakan bermacam tipe diskon dan pajak]

# Realisasi
def harga_after_some_variables (harga, kategori, VIP) :
    
   if kategori == "elektronik" :
        if VIP == True :
            return harga - (harga * (3/10))
        elif VIP == False :
            return harga - (harga * (1/10))
   elif kategori == "pakaian" :
        if VIP == True :
            return harga - (harga * (2/10))
        elif VIP == False :
            return harga - (harga * (5/100))
   elif kategori == "makanan" :
        if VIP == True :
            return harga - (harga * (15/100))
        elif VIP == False :
            return harga - (harga * (2/100))
   else :
        return harga 

def pajak_lokasi (lokasi, harga) :
  if lokasi == "luar negeri" :
     return harga + (harga * 20/100)
  elif lokasi == "dalam negeri" :
     return harga + (harga * 10/100)
    
def kondisi_hari (harga, hari, VIP, kategori) :
  if (hari == 'Jumat' or hari == 'Sabtu') and VIP == True :
        return harga - (harga * 5/100)
  elif hari == 'Minggu' :
        return harga + (harga * 5/100)
  elif hari == 'Rabu' and kategori == "pakaian": 
        return harga - (harga * 5/100)
  else : 
        return harga

def hargaAkhir(harga, kategori, VIP, lokasi, hari) :
   a = harga_after_some_variables (harga, kategori, VIP)
   b = pajak_lokasi (lokasi, a)
   c = kondisi_hari (b, hari, VIP, kategori)
   return int(c)

print(int(eval(input())))

#Aplikasi
hargaAkhir(1000000, "elektronik", True, "dalam negeri", "Senin")
hargaAkhir(500000, "pakaian", False, "luar negeri", "Rabu")