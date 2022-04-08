import sys

class guru:
    def __init__(self, nama, usia, pelajaran):
        self.nama = nama
        self.usia = usia
        self.pelajaran = pelajaran
        self.point = 0

    def input_poin(self, point):
        self.point = self.point + point

    def status_guru(self):
        print ('guru {}, pelajaran {}, total poin {}'.format(self.nama, self.pelajaran, self.point))

    @staticmethod
    def cek_usia(usia):
        if usia > 10 :
            print('cukup')
        else : 
            print('belum')

#guru_print = guru(sys.argv[1], sys.argv[2], sys.argv[3])
#print(guru_print.nama)

#a, b = 10, 5
#if a + b:
#    print('true')
#else :
#    print('false')

x = 0
while (x < 100) :
    x+=2
    break
print(x)

n = [10, 20]
i = ['kursi','meja']
for x in n :
    for z in i :
        print(x,z)

