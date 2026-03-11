# Nama file : Lalulintaslangit.py
# Pembuat   : Aqiatillah Rezi Zhafran
# NIM       : 24060124140124 
# Tanggal   : 24 September 2024
# Deskripsi : Lalu lintas langit

# Definisi dan spesifikasi 
# monitor_pesawat : 3 int -> string
#  [monitor_pesawat (x,y,z) adalah funsgi untuk menganalisis data dan mengeluarkan status operasional pesawat berdasarkan kondisi berikut: "Kecepatan Berbahaya": Jika kecepatan melebihi 900 km/h atau di bawah 200 km/h. "Terlalu Tinggi": Jika ketinggian pesawat melebihi 12.000 meter. "Bahan Bakar Rendah": Jika status bahan bakar kurang dari 20%. "Aman untuk Mendarat": Jika ketinggian kurang dari 5.000 meter, kecepatan antara 200 hingga 900 km/h, dan bahan bakar lebih dari 50%. "Berjalan Normal": Jika tidak ada kondisi di atas yang terpenuhi]

# Realisasi
def monitor_pesawat(t,k,f) :
    if t<5000 and 200<k<900 and f>=50:
       return 'Aman untuk Mendarat'
    elif k<200 or k>900:
       return "Kecepatan Berbahaya"
    elif t>12000:
       return "Terlalu Tinggi"
    elif f<20:
       return 'Bahan Bakar Rendah'
    else:
       return 'Berjalan Normal'
    
print(eval(input()))

# Aplikasi
monitor_pesawat(4000,850,55)
monitor_pesawat(5000,950,70)