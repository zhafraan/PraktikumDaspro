# Nama file : Jampasirajaib.py
# Pembuat   : Aqiatillah Rezi Zhafran
# NIM       : 24060124140124
# Tanggal   : 24 September 2024
# Deskripsi : Jam pasir ajaib

# Definisi dan spesifikasi
# jam : 3 int -> 3 string
#   [jam (j,m,s) adalah fungsi untuk menentukan waktu yang tepat dengan format: j menunjukkan jumlah jam dalam rentang 0 hingga 24 m menunjukkan jumlah menit dalam rentang 0 hingga 59. s menunjukkan jumlah detik dalam rentang 0 hingga 59]

#Realisasi
def jam(j,m,s):
    if 0<=j<=24 and 0<=m<=59 and 0<=s<=59:
     return (f"Jam: {j}, Menit: {m}, Detik: {s}")
    else :
     return 'Waktu tidak valid'
    


# aplikasi
print(jam(12,30,45))
print(jam(12,45,60))