class Hewan :
    nama_latin = ""
    
    def __init__(self, nama, umur):
        self.nama=nama
        self.umur=umur

    def bangun(self):
        pass
    
    @staticmethod
    def tidur(self):
        print(self.nama)

    @classmethod
    def makan(cls):
        print(cls.nama_latin)

class Kucing(Hewan):
    nama_latin = "Cat"
    def tidur(self):
        print("{} sedang tidur".format(self.nama))
    
    def kecepatan(self, val=10):
        if val > 10:
            print('cepat sekali')
        else:
            print('lambat sekali')

class Kelinci(Hewan):
    nama_latin = "Rabbit"
    def tidur(self):
        print("{} sedang tidur".format(self.nama))

    def kecepatan(self, val=10):
        if val > 10:
            print('cepat sekali')
        else:
            print('lambat sekali')


kucingku = Kucing('moli','2 th')
print(kucingku.nama_latin)
kucingku.tidur()
kucingku.kecepatan(30)

kelinciku = Kelinci('unyu','1 th')
print(kelinciku.nama_latin)
kelinciku.tidur()
kelinciku.kecepatan()

