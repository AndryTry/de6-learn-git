class bangun:
    def __init__(self):
        pass

class persegi(bangun):
    def luas(p,l):
        return p*l
        
class persegi_panjang(bangun):
    def luas(s):
        return s*s

persegi_panjang = persegi_panjang()
print('Luas Persegi Panjang = {}'.format(persegi_panjang.luas(50,10)))
persegi = persegi()
print('Luas Persegi = {}'.format(persegi.luas(50)))

