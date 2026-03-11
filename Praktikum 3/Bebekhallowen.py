# Bebek Halloween
def BebekHalloween(N,B):
    if N < B:
     return 'bebek marah'
    elif N % B==0:
     return 'bebek gembira dan Pak Dengklek tidak bingung'
    elif N>B:
     return 'bebek gembira tetapi Pak Dengklek bingung'
    
print(BebekHalloween(0,3))
print(BebekHalloween(24,7))
print(BebekHalloween(70, 7))