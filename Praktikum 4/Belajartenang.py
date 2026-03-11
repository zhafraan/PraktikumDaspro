# Nama file : Belajartenang.py
# Pembuat   : Aqiatillah Rezi Zhafran
# NIM       : 24060124140124 
# Tanggal   : 24 September 2024
# Deskripsi : Belajar tenang

# Definisi dan spesifikasi 
# BelajarTenang : 2 int -> string
#   [BelajarTenang (dB,m) adalah fungsi yang menyatakan berapa meter yang Shibusawa minimal harus tempuh atau bensin Shibusawa tidak cukup]
#Realisasi
def calculate(dB, m):
  return 15 * 10 ** ((dB-40)/ 20)

def BelajarTenang(dB,m):
  if calculate(dB, m) > m:
     return "Isi bensin dulu, bang"
  else:
     return f"{calculate(dB,m):.3f} meter"
  
print(BelajarTenang(102, 20000))
    
# Aplikasi
BelajarTenang(102, 20000)
BelajarTenang(100, 1300)