class Mahasiswa:
    def __init__(self, nama, nim):
        self.nama = nama
        self.nim = nim
    def belajar(self):
        print(self.nama, "sedang belajar")
class Pekerja:
    def __init__(self, nama, pekerjaan):
        self.nama = nama
        self.pekerjaan = pekerjaan
    def bekerja(self):
        print(self.nama, "sedang membuat program")
class MahasiswaPekerja(Mahasiswa, Pekerja):
    def __init__(self, nama, nim, pekerjaan):
        Mahasiswa.__init__(self, nama, nim)
        Pekerja.__init__(self, nama, pekerjaan)
    def presentasi(self):
        print(self.nama, "sedang presentasi")
mhs_pekerja = MahasiswaPekerja("Mahdi", "210511030", "Programmer")
mhs_pekerja.belajar() # output: Mahdi sedang belajar
mhs_pekerja.bekerja() # output: Mahdi sedang bekerja
mhs_pekerja.presentasi() # output: Mahdi sedang presentasi
