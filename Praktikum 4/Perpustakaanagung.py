# Nama file : Perpustakaanagung.py
# Pembuat   : Aqiatillah Rezi Zhafran
# NIM       : 24060124140124 
# Tanggal   : 24 September 2024
# Deskripsi : Perpustakaan agung

# Definisi dan spesifikasi 
# call_day : string -> int
#   [call_day (x) untuk mencari rata rata]
# jangkauan : 3 int -> int
#   [jangakauan (AS, AM, AIP) untuk mencari jangkauan]
# EstimateGreatLib : str, int {0 <= 24}, int, int, int {0 <= 24}, int {0 <= n}, int, int {0...10000}, int {1 <= n <= 100}
#   [EstimateGreatLib (D, X, Y, SS, SR, AS, AM, AIP, R) untuk hasil dari soal (aku nggak tau mau dikasih apa disini)]


#Realisasi
def call_day(x):
    if x == "senin":
        return (5000 + 6000 + 4000) / 3
    elif x == "selasa":
        return (7000 + 5000 + 2000) / 3
    elif x == "rabu":
        return (4500 + 3500 + 3000) / 3
    elif x == "kamis":
        return (2900 + 2100 + 2000) / 3
    elif x == "jumat":
        return (3000 + 3000 + 3000) / 3
    elif x == "sabtu":
        return (2000 + 2500 + 2300) / 3
    elif x == "minggu":
        return (1100 + 900 + 1000) / 3


def jangkauan(AS, AM, AIP):
    return max(AS, AM, AIP) - min(AS, AM, AIP)


def EstimateGreatLib(D, X, Y, SS, SR, AS, AM, AIP, R):
       
        if SR <= X < Y <= SS:
            return (Y - X) * jangkauan(AS, AM, AIP) / call_day(D)
        elif (X >= SS and Y > SS):
            return (Y - X) * jangkauan(AS, AM, AIP) * (R / 100) / call_day(D)
        elif (X < SR and Y <= SR):
            return ((Y - X) * (max(AS, AM, AIP) - min(AS, AM, AIP)) / call_day(D) * R / 100)
        elif X >= SR and Y > SS:
            return ((SS - X) * jangkauan(AS, AM, AIP) / call_day(D) + (Y - SS) * jangkauan(AS, AM, AIP) * (R / 100) / call_day(D)) / 2
        elif X < SR and (Y > SR and Y <= SS):
            return ((SR - X) * jangkauan(AS, AM, AIP) * (R / 100) / call_day(D) + (Y - SR) * jangkauan(AS, AM, AIP) / call_day(D) )/ 2
        elif X < SR < SS < Y:
            return ((SR - X) * jangkauan(AS, AM, AIP) * (R / 100) / call_day(D) + (SS - SR) * jangkauan(AS, AM, AIP) / call_day(D) + (Y - SS) * jangkauan(AS, AM, AIP) * (R / 100) / call_day(D)) / 3

print(round(eval(input()), 5))

#Aplikasi    
EstimateGreatLib("senin", 12, 17, 18, 9, 6000, 5000, 4500, 50)
EstimateGreatLib("selasa", 8, 16, 20, 12, 7000, 5000, 2000, 75)

#Additional notes
# X = jam mulai buka / mulai bekerja
# Y = jam tutup
# D = hari tertentu
# SR = waktu sunrise
# SS = waktu sunset
# AS = ahli statistika
# AM = ahli matematika
# AIP = ahli ilmu perpustakaan
# R = persentase