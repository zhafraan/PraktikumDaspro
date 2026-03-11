# RamuanKeabadian
def buatRamuan(a, b, c, d):
    if a==b==c==d :
     return 'terjadi ledakan'
    elif a==0.3*(a+b+c+d) and b==0.3*(a+b+c+d) and c==0.15*(a+b+c+d) and d==0.25*(a+b+c+d):
     return'ramuan berhasil di dapatkan'
    elif (abs(a - b) <= 5 and abs(a - c) <= 5 and abs(a - d) <= 5 and 
          abs(b - c) <= 5 and abs(b - d) <= 5 and abs(c - d) <= 5):
     return 'hampir terjadi ledakan'
    elif a < 0.3*(a+b+c+d) :
     return 'larutan a terlalu sedikit'
    elif b <  0.3*(a+b+c+d):
     return 'larutan b terlalu sedikit'
    elif c < 0.15*(a+b+c+d):
     return 'larutan c terlalu sedikit'
    elif d < 0.25*(a+b+c+d):
     return 'larutan d terlalu sedikit'
    
print(buatRamuan(30, 30, 15, 25))
print(buatRamuan(29, 30, 15, 25))
print(buatRamuan(30, 30, 30, 26))
print(buatRamuan(28, 29, 15, 25))