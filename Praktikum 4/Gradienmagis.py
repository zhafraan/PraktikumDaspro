# Nama file : Gradientmagis.py
# Pembuat   : Aqiatillah REzi Zhafran
# NIM       : 24060124140124 
# Tanggal   : 24 September 2024
# Deskripsi : Gradient magis

# Definisi dan spesifikasi 
# f(x) : int -> int
#   [f(x) adalah fungsi untuk mencari nilai pada sebuah titik]
# gradien (a,b) : 2 int -> int
#   [gradien (a,b) adalah fungsi untuk menghitung gradien]

#Realisasi
def f(x) :
 return (3*(x**2) +2*x - 5)

def gradien(a,b) :
 return (f(a)-f(b))/(a-b) 

print(eval(input()))

#Aplikasi
gradien(3,1)