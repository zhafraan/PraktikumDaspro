# Nama File   = Tanggal.py
# Nama        = Aqiatillah Rezi Zhafran
# NIM         = 24060124140124
# Tanggal     = 30 September 2024 
# Deskripsi   = menjawab soal penanggalan

# DEFINISI TYPE
# type Hr: <x:integer[1..31]>
#   {<x> menamakan tipe integer dengan daerah nilai tertentu supaya mewakili hari}
# type Bln: <x:integer[1..12]>
#   {<x> menamakan tipe integer dengan daerah nilai tertentu supaya mewakili Bulan}
# type Thn: <x:integer[> 0]>
#   {<x> menamakan tipe integer dengan daerah nilai tertentu supaya mewakili Tahun}
# type Date: <d:Hr, m:Bln, y:Thn>
#   {<d,m,y> adalah tanggal d bulan m tahun y}

# DEFINISI DAN SPESIFIKASI KONSTRUKTOR
# Make_Date: Hr,Bln,Thn --> Date
#   {Make_Date (d,m,y) membentuk Date dari hr,Bln,Thn yang saling bersangkutan}

# REALISASI
def Make_Date(d,m,y):
    return [d,m,y]

# DEFINISI DAN SPESIFIKASI SELECTOR
# Day   : Date --> Hr
#   {Date(D) memberikan hari d dari D yang terdiri dari <d,m,y>}
# Month : Date --> Bln
#   {Date(D) memberikan bulan m dari D yang terdiri dari <d,m,y>}
# Year  : Date --> Thn
#   {Year(D) memberikan tahun y dari D yang terdiri dari <d,m,y>}

# REALISASI
def Day(D):
    return D[0]

def Month(D):
    return D[1]

def Year(D):
    return D[2]

# DEFINISI DAN SPESIFIKASI OPERATOR TERHADAP DATE
# NextDay: 2 Date --> Date
#   {NextDay(D) menghitung keesokan hari dari Date D}
# Yesteday: 2 Date --> Date
#   {Yesteday(D) menghitung hari kemarin dari Date D}

# REALISASI
def NextDay(D):
    # bulan yang terdiri dari 30 hari kecuali desember
    if Month(D) == 1 or Month(D) == 3 or Month(D) == 5 or Month(D) == 7 or Month(D) == 8 or Month(D) == 10:
        if Day(D) < 31:
            return Make_Date(Day(D) + 1, Month(D), Year(D))
        else:
            return Make_Date(1, Month(D) + 1, Year(D))
    # bulan februari
    elif Month(D) == 2:
        if Day(D)< 28:
            return Make_Date(Day(D) + 1, Month(D), Year(D))
        else:
            if IsKabisat(Year(D)):
                if Day(D) == 28:
                    return Make_Date(Day(D) + 1, Month(D), Year(D))
                else:
                    return Make_Date(1, Month(D) + 1, Year(D))
            else:
                return Make_Date(1, Month(D) + 1, Year(D))
    # Bulan yang terdiri dari 30 hari
    elif Month(D) == 4 or Month == 6 or Month == 9 or Month == 11:
        if Day(D) < 30:
            return Make_Date(Day(D) + 1, Month(D), Year(D))
        else:
            return Make_Date(1, Month(D) + 1, Year(D))
    # bulan desember
    elif Month(D) == 12:
        if Day(D) < 31:
            return Make_Date(Day(D) + 1, Month(D), Year(D))
        else:
            return Make_Date(1,1,Year(D) + 1)
            
def Yesteday(D):
    if Day(D) == 1:
        if  Month(D) == 12 or Month(D) == 5 or Month(D) == 7 or Month(D) == 10:
            return Make_Date(30, Month(D) + 1, Year(D))
        elif Month(D) == 3:
            if IsKabisat(Year(D)):
                return Make_Date(29, 2, Year(D))
            else:
                return Make_Date(28, 2, Year(D))
        elif Month(D) == 2 or Month(D) == 4 or Month(D) == 6 or Month(D) == 8 or Month(D) == 9 or Month(D) == 11:
            return Make_Date(31, Month(D) + 1, Year(D))
        elif Month(D) == 1:
            return Make_Date(31,12,Year(D) - 1)
    else:
        return Make_Date(Day(D) - 1, Month(D), Year(D))
    
# DEFINISI DAN SPESIFIKASI PREDIKAT
# isEqD: Date --> Boolean
#   {isEqD(G1,G2) benar jika D1 sama dengan D2}
# IsBeafore: Date --> Boolean
#   {IsBeafore(G1,G2) benar jika D1 sebelum D2}
# IsAfter: Date --> Boolean
#   {IsAfter(G1,G2) benar jika D1 sesudah D2}
# IsKabisat: Date --> Boolean
#   {IsKabisat(G1,G2) benar jika thn tesebut merupakan tahun kabisat}

# REALISASI
def isEqD(D1,D2):
    return Day(D1) == Day(D2) and Month(D1) == Month(D2) and Year(D1) == Year(D2)

def IsBefore(D1,D2):
    if Year(D1) != Year(D2):
        return  Year(D2) < Year(D1)
    else:
        if Month(D1) != Month(D2):
            return Month(D2) < Month(D1)
        else:
            return Day(D2) < Day(D1)

def IsAfter(D1,D2):
    if Year(D1) != Year(D2):
        return  Year(D2) > Year(D1)
    else:
        if Month(D1) != Month(D2):
            return Month(D2) > Month(D1)
        else:
            return Day(D2) > Day(D1)
        
def IsKabisat(T):
    return T % 4 == 0 and (T % 100 != 0 or T % 400 == 0)


# APLIKASI
print(NextDay(Make_Date(5,1,2006)))
print(Yesteday(Make_Date(29,3,2024)))

print(isEqD(Make_Date(24,10,2024),Make_Date(24,10,2024)))
print(IsBefore(Make_Date(24,10,2024),Make_Date(23,10,2024)))
print(IsAfter(Make_Date(24,10,2024),Make_Date(25,10,2024)))