print("\n----------------------------------------------------------------------------\n")
# {SigI(a,b) adalah fungsi untuk menghitung Sigma(i) untuk nilai i pada 
# interval a dan b: a + (a+1) + (a+1+1) + ..... + b, atau 0 jika interval "kosong"  }
# REALISASI
def SigI(a,b):
    if a > b:
        return 0
    else:
        return a + SigI(a+1, b)
# APLIKASI
if __name__ == "__main__":
    print("SigI(a,b)")
    print(" a=1 & b=1 :",(SigI(1,1)))
    print(" a=1 & b=3 :",(SigI(1,3)))
    print(" a=2 & b=3 :",(SigI(2,3)))


# {SigI3(a,b) adalah fungsi untuk menghitung Sigma(i3) untuk nilai i pada 
# interval a dan b: a3 + (a+1)3 + (a+1+1)3 + ..... + b3, atau 0 jika interval "kosong"  }
# REALISASI
def Sig3(a,b):
    if a > b:
        return 0
    else:
        return (a*a*a) + Sig3(a+1,b)
# APLIKASI
if __name__ == "__main__":
    print("\nSig3(a,b)")
    print(" a=1 & b=1 :",(Sig3(1,1)))
    print(" a=1 & b=3 :",(Sig3(1,3)))
    print(" a=2 & b=3 :",(Sig3(2,3)))

#  {SP8(a,b) adalah fungsi untuk menghitung deret konvergen ke π /8 pada 
#  interval a dan b atau 0 jika interval "kosong". Rumus :  /
#   1/(1*3) + 1/(5*7) + 1/(9*11) + ...  } 
# REALISASI
def SP8(a,b):
    if a>b:
        return 0
    else:
        return (1/((a)*(a+2)) + SP8((a+4),b))
# APLIKASI
if __name__ == "__main__":
    print("\nSP8(a,b)")
    print(" a=1 & b=1 :",(SP8(1,1)))
    print(" a=1 & b=3 :",(SP8(1,3)))
    print(" a=2 & b=3 :",(SP8(2,3)))

print("\n----------------------------------------------------------------------------\n")
#  { Id(i) mengirimkan nilai i) 
#  Id(i) : i 
def Id (i: int):
    return i

# { P1(i) mengirimkan nilai i+1)  
# P1(i) : i+1
def P1 (i: int):
    return i + 1

#  { P4(i) mengirimkan nilai i+4)  
# P4(i) : i+4
def P4 (i: int):
    return i+4

#  { Cube(i) mengirimkan nilai i3)  
# Id(i) : i3
def Cube(i: int):
    return i * i * i

# { T(i) mengirimkan nilai 1/((i+1)+(i+3))  
#  T(i) : 1/((i+1)+(i+3))
def T (i: int):
    return 1/((i)*(i+2))

# Sigma : integer, integer,(integer →  numerik),(integer → numerik)  → numerik 
# {Sigma (a,b,f,s) adalah penjumlahan dari deret/serie f(i), dengan 
#  mengambil nilai subseri a, s(a), s(s(a)),.... 
#  pada interval [a..b] atau 0 jika interval kosong }
# REALISASI
def Sigma(a,b,f,s):
    if a > b:
        return 0
    else:
        return f(a) + Sigma(s(a), b, f, s)
# APLIKASI
if __name__ == "__main__":
    print("Sigma(a,b,f,s)")
    print("\nidentik dengan SigI")
    print(" menggunakan Id & P1 untuk a=1 & b=1 :",(Sigma(1,1,Id,P1)))
    print(" menggunakan Id & P1 untuk a=1 & b=3 :",(Sigma(1,3,Id,P1)))
    print(" menggunakan Id & P1 untuk a=2 & b=3 :",(Sigma(2,3,Id,P1)))
    print("\nidentik dengan SigI3")
    print(" menggunakan Cube & P1 untuk a=1 & b=1 :",(Sigma(1,1,Cube,P1)))
    print(" menggunakan Cube & P1 untuk a=1 & b=3 :",(Sigma(1,3,Cube,P1)))
    print(" menggunakan Cube & P1 untuk a=2 & b=3 :",(Sigma(2,3,Cube,P1)))
    print("\nidentik dengan SP8")
    print(" menggunakan T & P4 untuk a=1 & b=1 :",(Sigma(1,1,T,P4)))
    print(" menggunakan T & P4 untuk a=1 & b=3 :",(Sigma(1,3,T,P4)))
    print(" menggunakan T & P4 untuk a=2 & b=3 :",(Sigma(2,3,T,P4)))

print("\n----------------------------------------------------------------------------\n")

# # APLIKASI MENGGUNAKAN LAMBDA
if __name__ == "__main__":
    print("\nAplikasi fungsi Sigma dengan lambda")
    print("identik dengan SigI")
    # Untuk SigI : Sigma(a,b, λ x.x, λ x.x+1)
    print(" menggunakan Sigma(a,b, λ x.x, λ x.x+1) untuk a=1 & b=1 :",(Sigma(1,1,lambda x: x,lambda x: x+1)))
    print(" menggunakan Sigma(a,b, λ x.x, λ x.x+1) untuk a=1 & b=3 :",(Sigma(1,3,lambda x: x,lambda x: x+1)))
    print(" menggunakan Sigma(a,b, λ x.x, λ x.x+1) untuk a=2 & b=3 :",(Sigma(2,3,lambda x: x,lambda x: x+1)))
    print("\nidentik dengan SigI3")
    # Untuk SigI3 : Sigma(a,b, λx.x3, λx.x+1)
    print(" menggunakan Sigma(a,b, λx.x3, λx.x+1) untuk a=1 & b=1 :",(Sigma(1,1,lambda x: x*x*x, lambda x: x+1)))
    print(" menggunakan Sigma(a,b, λx.x3, λx.x+1) untuk a=1 & b=3 :",(Sigma(1,3,lambda x: x*x*x, lambda x: x+1)))
    print(" menggunakan Sigma(a,b, λx.x3, λx.x+1) untuk a=2 & b=3 :",(Sigma(2,3,lambda x: x*x*x, lambda x: x+1)))
    print("\nidentik dengan SP8")
    # Untuk SP8 : Sigma(a,b, λx.1/(x*(x+2)), λx.x+4)
    print(" menggunakan λx.1/(x*(x+2)), λx.x+4 untuk a=1 & b=1 :",(Sigma(1,1,lambda x: 1/(x*(x+2)),lambda x: x+4)))
    print(" menggunakan λx.1/(x*(x+2)), λx.x+4 untuk a=1 & b=3 :",(Sigma(1,3,lambda x: 1/(x*(x+2)),lambda x: x+4)))
    print(" menggunakan λx.1/(x*(x+2)), λx.x+4 untuk a=2 & b=3 :",(Sigma(2,3,lambda x: 1/(x*(x+2)),lambda x: x+4)))
    
print("\n----------------------------------------------------------------------------\n")


# ekspresi lambda tidak boleh rekursif. 

