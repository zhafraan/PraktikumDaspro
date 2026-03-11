# Nama file : Jalansemut.py
# Pembuat   : Aqiatillah Rezi Zhafran
# NIM       : 24060124140124 
# Tanggal   : 24 September 2024
# Deskripsi : Jalan Semut

# Definisi dan spesifikasi 
# bidang : 3 int -> real
#   [bidang (x,y,z) adalah fungsi untuk mencari jarak terpendek yg dapat ditempuh oleh semut pada bidang (x,y,z)]
# jalanSemut : 3 int -> real
#   [jalanSemut (x,y,z) adalah fungsi untuk mencari jalan terpendek dan mebulatkan hasil ke 3 angka desimal]

#Realisasi
def bidang(x,y,z):
    if x>y and x>z:
     return((y+z)**2+x**2)**0.5
    elif  y>x and y>z:
     return((x+z)**2+y**2)**0.5
    elif  z>x and z>y:
     return((x+y)**2+z**2)**0.5

def jalanSemut(x,y,z):
 return round(bidang(x,y,z), 3)

print(eval(input()))

#Aplikasi
jalanSemut(3,4,5)
jalanSemut(1,2,7)