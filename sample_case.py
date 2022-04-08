import sys

class Kendaraan:
    bensin = 'Pertamax'
    def __init__(self, kapasitas, nama):
        self.kapasitas = kapasitas
        self.nama = nama
    
    ## cls adalah class method
    def get_bensin(cls):
        print(cls.bensin)
    
    def get_kapasitas(self):
        print(self.kapasitas)

    def get_nama(self):
        print(self.nama)

class Mobil(Kendaraan): 
    ## pass adalah untuk uspaya class tsb ada isinya
   def belok(self, arah=None):
       if arah is None:
           print("arah lurus")
       else:
            print("arah",arah)
   pass

class Motor(Kendaraan):
    bensin = 'Pertalite'
    pass

#mobil1 = Mobil('6', sys.argv[1])
#motor1 = Motor('2', sys.argv[2])

Mobil.belok(sys.argv[1] = '')
#print(mobil1.get_bensin())
#print(motor1.get_bensin())
