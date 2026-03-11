# Pembuat: Aqiatillah Rezi Zhafran
# Tanggal: 3 November 2024

# REALISASI {manfaatkan fungsi yang telah dipelajari, fungsi2 di bawah tidak harus digunakan semua}
def Tail(x):
  	return x[1:]

# def IsEmpty(x):
# 	if x == []:
#         return True
#     else:
#         return False

def Konsi(y,x):
    return y + [x]

def Konso(x,y):
    return [x] + y
  
# tulis jawaban di sini
def tobinary(n):
    if n == 0:
        return []
    else:
        return tobinary(n // 2) + [n % 2]
    
def pad_or_trim(binary_list, b):
    if len(binary_list) < b:
        return pad_or_trim(Konso(0, binary_list), b)  
    elif len(binary_list) > b:
        return binary_list[-b:]
    else:
        return binary_list

def mainBiner(a, b):
    return pad_or_trim(tobinary(a), b)


  	
# APLIKASI
print(eval(input()))

# Nama : Aqiatillah Rezi Zhafran
# Tanggal : 28 Oktober 2024

def FirstElmt(L):
    return L[0]

def LastElmt(L):
    return L[-1]

def Head(L):
    return L[:-1]

def Tail(L):
    return L[1:]

def Konso(e, L):
    return [e] + L

def Konsi(e, L):
    return L + [e]

def isEmpty(L):
    return L == []

def isMember(x, L):
    if isEmpty(L):
        return False
    else:
        if FirstElmt(L) == x:
            return True
        else:
            return isMember(x, Tail(L))
        
def PulauAngka(D, M):
  # tulis algoritma di sini
    if isEmpty(D) :
         return []
    else :
        if isMember(FirstElmt(D), M):
            return PulauAngka(Tail(D),M)
        else :
            return Konso(FirstElmt(D), PulauAngka(Tail(D),M))
   

print(eval(input()))

# Nama : Aqiatillah Rezi Zhafran
# Tanggal : 2 November 2024

def FirstElmt(L):
    return L[0]

def LastElmt(L):
    return L[-1]

def Head(L):
    return L[:-1]

def Tail(L):
    return L[1:]

def Konso(e, L):
    return [e] + L

def isEmpty(L):
    return L == []

def dimensi(L): # atau NbElmt()
    if isEmpty(L):
        return 0
    else:
        return 1 + dimensi(Tail(L))
      
  # Tulis algoritma di sini
def dimensi(L1,L2):
    if isEmpty(L1) :
        return 0
    else:
        if(FirstElmt(L1) > FirstElmt(L2)):
            return 1+(dimensi(Tail(L1),Tail(L2)))
        else:
            return dimensi(Tail(L1),Tail(L2))
        
def DuelSihir(S, M):
    if dimensi(S,M) == dimensi(M,S):
        return"Keduanya Seri"
    elif dimensi(S,M) > dimensi(M,S):
        return"Snape Menang"
    elif dimensi(S,M) < dimensi(M,S):
        return"McGonagall Menang"
    
# PRINT
print(eval(input()))


# Selamat Menikmati
# Pembuat: Aqiatillah Rezi Zhafran
# Tanggal: 3 November 2024

# REALISASI {manfaatkan fungsi yang telah dipelajari, fungsi2 di bawah tidak harus digunakan semua}
def Konsi(y,x):
    return y + [x]

def FirstElmt(x):
    if x != []:    
        return x[0]

def Tail(x):
    if x != []:
        return x[1:]

def Head(x):
    if x != []:
        return x[:-1]

def IsEmpty(x):
    if x == []:
        return True
    else:
        return False
    
def LastElmt(x):
    if x != []:
        return x[-1]


def NbElmnt(x):
    if IsEmpty(x):
        return 0
    else:
        return 1 + NbElmnt(Tail(x))
  
# tulis jawaban di sini
def buatBit(a, b, pos=1):
    if a == 0 or b == 0: 
        return 0
    else:
         return (pos if a % 2 == 1 and b % 2 == 1 else 0) + buatBit(a // 2, b // 2, pos * 2)

def andBitInt(a, b):
    return buatBit(a, b)


  	
# APLIKASI
print(eval(input()))
# Nama File: matematika_gura.py
# Pembuat: Aqiatillah Rezi Zhafran
# Tanggal: 3 November 2024
# Deskripsi: Mengembalikan list hasil tambah-tambah dua buah list sebagai representasi integer.

# DEFINISI DAN SPESIFIKASI
# shrimp --> list: integer
# shrimp(X, Y) mengembalikan list hasil tambah-tambah dua buah list sebagai representasi integer.

# REALISASI
def konso(e, L):
    return [e] + L
    
def konsi(L, e):
    return L + [e]
  
def first_elmt(L):
    return L[0]
  
def last_elmt(L):
    return L[-1]
  
def head(L):
    return L[:-1]
  
def tail(L):
    return L[1:]

def is_empty(L):
    return len(L) == 0
  
def IsOneElmt(List):
    return Tail(List)==[]

def Change(List):
    if is_empty(List):
         return ''
    else:
        if  first_elmt(List)!='-':
            return str( first_elmt(List)) + (Change(tail(List)))
        else:
            return "-" + (Change(tail(List)))
def to_list(n):
    if n < 0:
        n = abs(n)
        return konso('-',to_list(n))
    elif n < 10:
        return [n]
    else:
        return konsi(to_list(n // 10) , n % 10)

def shrimp(L,L1):
    if is_empty(L) and is_empty(L1):
        return 0
    if is_empty(L) and not is_empty(L1):
        return shrimp([0],L1)
    if not is_empty(L) and is_empty(L1):
        return shrimp(L,[0])
    else:
        return to_list((int(Change(L))+int(Change(L1))))
      
# APLIKASI
print(eval(input()))


  	
